from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.subscriptions.models import Subscription

class SubscriptionDetaiGet(TestCase):
    
    def setUp(self):
        self.obj = Subscription.objects.create(
            name = "Lucas", 
            cpf = '1234567890', 
            phone = '111',
            email='lucasmmantelli@gmail.com')
        
        self.response = self.client.get(r('subscriptions:detail',self.obj.pk))
        
    def test_get(self):
        self.assertEqual(200,self.response.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.response,"subscriptions/subscription_detail.html")
        
    def test_context(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription,Subscription)
    
    def test_html(self):
        contents = (
            self.obj.name,
            self.obj.cpf,
            self.obj.phone,
            self.obj.email,
        )
        for content in contents:
            with self.subTest():
                self.assertContains(self.response,content)

class SubscriptionDetaiNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('subscriptions:detail',0))
        self.assertEqual(404,response.status_code)