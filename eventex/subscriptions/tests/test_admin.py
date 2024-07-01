from unittest.mock import Mock
from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin , Subscription, admin

class SubcriptionModelAdiminTest(TestCase):
    def setUp(self):
        self.model_adimin = SubscriptionModelAdmin(Subscription, admin.site)
        Subscription.objects.create(name = "Lucas", 
                                    cpf = '1234567890', 
                                    phone = '111',
                                    email='lucasmmantelli@gmail.com',
                                    paid= False)
        
    def test_has_action_mark_as_paid(self):
        """Action mark_as_paid must be installed"""
        self.assertIn("mark_as_paid", self.model_adimin.actions)
        
    def test_has_action_mark_as_not_paid(self):
        self.assertIn("mark_as_not_paid",self.model_adimin.actions)
        
    def test_mark_all_as_paid(self):
        """It should mark all selected subscriptions as paid"""
        self.call_action(act='paid')        
        self.assertEqual(1,Subscription.objects.filter(paid = True).count())
        
    def test_mark_all_as_not_paid(self):
        """It should mark all selected subscriptions as paid"""
        self.call_action(act='not paid')
        self.assertEqual(1,Subscription.objects.filter(paid = False).count())
        
    def test_send_message_paid(self):        
        mock = self.call_action(act='paid')
        mock.assert_called_once_with(None,'1 inscrição foi marcada como paga.')
    
    def test_send_message_not_paid(self):        
        mock = self.call_action(act='not paid')
        mock.assert_called_once_with(None,'1 inscrição foi marcada como não paga.')
   
   
    def call_action(self,act):
        queryset = Subscription.objects.all()
    
        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock 
        if(act=='paid'):
            self.model_adimin.mark_as_paid(None,queryset)
        else:
            Subscription.objects.update(paid=True)
            self.model_adimin.mark_as_not_paid(None,queryset)
        SubscriptionModelAdmin.message_user = old_message_user
        
        return mock