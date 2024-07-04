from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name = "Lucas mantelli",
            slug="lucas-mantelli",
            photo = "http/hbn.link/lc-pic"
        )
    
    def test_email(self):
        contact = Contact.objects.create(
            speaker = self.speaker,
            kind = Contact.EMAIL,
            value = 'lucasmmantelli@gmail.com'
        )
        
        self.assertTrue(Contact.objects.exists())
        
    def test_phone(self):
        contact = Contact.objects.create(
            speaker = self.speaker,
            kind = Contact.PHONE,
            value = '00-000000000'
        )
        
        self.assertTrue(Contact.objects.exists())
    
    def test_choices(self):
        """Contact kind must bem E o P ONLY"""
        contact = Contact.objects.create(
            speaker = self.speaker,
            kind = 'Y',
            value = 'B'
        )
        self.assertRaises(ValidationError, contact.full_clean)
        
    def test_str(self):
        contact = Contact(
            speaker = self.speaker,
            kind = Contact.EMAIL,
            value = 'lucasmmantelli@gmail.com'
        )
        self.assertEqual('lucasmmantelli@gmail.com',str(contact))

class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name = "Lucas Mantelli",
            slug="lucas-mantelli",
            photo = "http/hbn.link/lc-pic"
        )
        
        s.contact_set.create(kind=Contact.EMAIL, value='lucasmmantelli@gmail.com')
        s.contact_set.create(kind=Contact.PHONE, value='00-000000000')
    
    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['lucasmmantelli@gmail.com']
        self.assertQuerySetEqual(qs,expected,lambda o: o.value)
        
    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['00-000000000']
        self.assertQuerySetEqual(qs,expected,lambda o: o.value)