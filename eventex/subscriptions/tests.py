from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from django.core import mail
class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """Get /inscricao/ must return statuscode 200"""
        self.assertEqual(200,self.response.status_code)


    def test_template(self):
        """Must use subscriptions/subscription.html as template"""
        self.assertTemplateUsed(self.response,'subscriptions/subscription_form.html')
    
    def test_html(self):
        """HTML must contain input tags"""
        self.assertContains(self.response,'<form')
        self.assertContains(self.response,'<input',6)
        self.assertContains(self.response,'type="text"',3)
        self.assertContains(self.response,'type="email"')
        self.assertContains(self.response,'type="submit"')
        
    def test_csrf(self):
        """HTML must contain csrf"""
        self.assertContains(self.response,'csrfmiddlewaretoken')
    
    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form,SubscriptionForm)
    
    def test_form_has_filds(self):
        """Form must have 4 fields"""
        form = self.response.context['form']
        self.assertSequenceEqual(['name','cpf','email','phone'],list(form.fields))

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name = "Lucas",cpf = '1234567890', 
                    phone = '111',email='lucasmmantelli@gmail.com')
        self.response = self.client.post('/inscricao/',data)
    
    def test_post(self):
        self.assertEqual(302,self.response.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1,len(mail.outbox))
    
    def test_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect,email.subject)

    def test_email_from(self):
        email = mail.outbox[0]
        expect = 'Contato@eventex.com'

        self.assertEqual(expect,email.from_email)

    def test_email_to(self):
        email = mail.outbox[0]
        expect = ['L@L,K@K,B@B']

        self.assertEqual(expect,email.to)

    def test_subscription_email_body(self):
        email = mail.outbox[0]
        self.assertIn("Lucas",email.body)
        self.assertIn("1234567890",email.body)
        self.assertIn("111",email.body)
        self.assertIn("lucasmmantelli@gmail.com",email.body)

class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/',{})
    def test_post(self):
        self.assertEqual(200,self.response.status_code)
    
    def test_template(self):
        """Must use subscriptions/subscription.html as template"""
        self.assertTemplateUsed(self.response,'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form,SubscriptionForm)
    
    def test_form_has_errors(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

class SubscribeSuccessMesage(TestCase):
    def test_message(self):
        data = dict(name = "Lucas",cpf = '1234567890', 
                    phone = '111',email='lucasmmantelli@gmail.com')
        response = self.client.post('/inscricao/',data,follow=True)
        self.assertContains(response,'Inscrição Realizada com sucesso!')