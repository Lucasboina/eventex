from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):
    
    def setUp(self):
        data = dict(name = "Lucas",cpf = '12345678901', 
                    phone = '111',email='lucasmmantelli@gmail.com')
        self.client.post(r('subscriptions:new'),data)
        self.email = mail.outbox[0]
    
    def test_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect,self.email.subject)

    def test_email_from(self):
        expect = 'Contato@eventex.com'

        self.assertEqual(expect,self.email.from_email)

    def test_email_to(self):
        expect = ['Contato@eventex.com','lucasmmantelli@gmail.com']

        self.assertEqual(expect,self.email.to)

    def test_subscription_email_body(self):
        contents = [
            "Lucas",
            "1234567890",
            "111",
            "lucasmmantelli@gmail.com",
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content,self.email.body)
       