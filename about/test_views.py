from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About


class TestAboutViews(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com")
        
        self.about = About.objects.create(
            title="Olivia",
            profile_image="",
            content="A little bit about me."
        )
        self.about.save()

    def test_render_about_page_with_collaborate_form(self):
        self.client.login(
            username="myUsername", password="myPassword")
        response = self.client.get(reverse(
            'about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"A little bit about me.", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)
        
    def test_successful_collaboration_submission(self):
        """Test for posting a collaboration request"""
        post_data = {
            'name': 'Collaborator Name',
            'email': 'email@email',
            'message': 'I would like to collaborate.'
        }
        response = self.client.post(reverse(
            'about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Potato',
            response.content
        )