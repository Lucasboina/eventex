from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm

class SuscriptionFormTest(TestCase):
        def setUp(self):
            self.form = SubscriptionForm()

        def test_form_has_filds(self):
            """Form must have 4 fields"""
            expected = ['name','cpf','email','phone']
            self.assertSequenceEqual(expected,list(self.form.fields))