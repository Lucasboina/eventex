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
            kind = Contact.EMAIL,
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