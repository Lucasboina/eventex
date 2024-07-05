from datetime import datetime
from eventex.subscriptions.models import Subscription
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = "Lucas", 
            cpf = '1234567890', 
            phone = '111',
            email='lucasmmantelli@gmail.com')
        self.obj.save()
          
    def test_create(self):      
        self.assertTrue(Subscription.objects.exists())
    
    def test_created_add(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at,datetime)
        
    def test_str(self):
        self.assertEqual('Lucas',str(self.obj))
        
    def test_paid_default_to_false(self):
        """By default paid must be false"""
        self.assertEqual(False,self.obj.paid)
        
    def test_get_absolute_url(self):
        url = r("subscriptions:detail",self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())