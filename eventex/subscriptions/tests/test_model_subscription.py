from datetime import datetime
from eventex.subscriptions.models import Subscription
from django.test import TestCase

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