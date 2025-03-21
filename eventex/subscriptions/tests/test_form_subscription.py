from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm

class SuscriptionFormTest(TestCase):
        def test_form_has_filds(self):
            """Form must have 4 fields"""
            form = SubscriptionForm()
            expected = ['name','cpf','email','phone']
            self.assertSequenceEqual(expected,list(form.fields))
            
        def test_is_digit(self):
            """CPF must only accept numbers"""
            form = self.make_validated_form(cpf = "213ssffd123")
            field = 'cpf'
            code = 'digits'
            self.assertFormErrorCode(form,code,field)
        
        def test_cpf_has_11_digits(self):
            """CPF must have 11 digits"""
            form =self.make_validated_form(cpf="1243")
            field = 'cpf'
            code = 'length'
            self.assertFormErrorCode(form,code,field)
        
        def test_name_must_be_captalized(self):
            """Name must be capitalized"""
            form = self.make_validated_form(name = "LUCAS mantelli")
            self.assertEqual('Lucas Mantelli', form.cleaned_data['name'])            

        def test_email_is_optional(self):
            form = self.make_validated_form(email ='')            
            self.assertFalse(form.errors)
        
        def test_phone_is_optional(self):
            form = self.make_validated_form(phone ='')            
            self.assertFalse(form.errors)
        
        def test_must_inform_email_or_phone(self):
            """Email and phone is optionl, but at least one must be informed"""
            form = self.make_validated_form(phone ='', email='')
            self.assertListEqual(['__all__'],list(form.errors))
                    
        def assertFormErrorCode(self,form,code,field):
            errors = form.errors.as_data()
            errors_list = errors[field]
            exeption = errors_list[0]
            self.assertEquals(code,exeption.code)
        
        def make_validated_form(self,**kwargs):
            valid = dict(name = "Lucas",cpf = '12345678901', 
                    phone = '111',email='lucasmmantelli@gmail.com')
            
            data = dict(valid,**kwargs)
            form = SubscriptionForm(data)
            form.is_valid()
            
            return form