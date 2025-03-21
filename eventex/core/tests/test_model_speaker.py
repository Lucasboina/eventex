from django.test import TestCase
from eventex.core.models import Speaker
from django.shortcuts import resolve_url as r

class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name = 'Grace Hopper',
            description=  'Programadora e almirante',
            photo ='http://hbn.link/hopper-pic',
            website='http://hbn.link/hopper-site',
            slug='grace-hopper'
        )
        
    def test_create(self):
        self.assertTrue(Speaker.objects.exists())
        
    def test_description_can_be_blanck(self):
        field = Speaker._meta.get_field('description')
        self.assertTrue(field.blank)
        
    def test_website_can_be_blank(self):
        field = Speaker._meta.get_field('website')
        self.assertTrue(field.blank)
    
    def test_str(self):
        self.assertEqual("Grace Hopper",str(self.speaker))
    
    def test_get_absolute_url(self):
        url = r('speaker_detail', slug = self.speaker.slug)
        self.assertEqual(url,self.speaker.get_absolute_url())