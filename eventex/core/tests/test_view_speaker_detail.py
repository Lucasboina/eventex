from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Speaker

class SpeakerDetailGet(TestCase):
    def setUp(self):
        Speaker.objects.create(
                name = 'Grace Hopper',
                description=  'Programadora e almirante',
                photo ='http://hbn.link/hopper-pic',
                website='http://hbn.link/hopper-site',
                slug = "grace-hopper"
        )
        self.response = self.client.get(r('speaker_detail', slug ='grace-hopper'))
        
    def test_get(self):
        """Get should return status code 200"""
        self.assertEqual(200,self.response.status_code)
        
    def test_template_used(self):
        self.assertTemplateUsed(self.response,'core/speaker_detail.html')
        
    def test_html(self):
        contents = [
            'Grace Hopper',
            'Programadora e almirante',
            'http://hbn.link/hopper-pic',
            'http://hbn.link/hopper-site',
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response,expected)
    
    def test_context(self):
        """Speaker must be in content"""
        speaker= self.response.context['speaker']
        self.assertIsInstance(speaker,Speaker)
        
class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('speaker_detail', slug = 'not-found'))
        self.assertEqual(404,response.status_code)
        