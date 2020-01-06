from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm # new
from .views import SignupPageView # new
# Create your tests here.


class CustomUserTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        
        user = User.objects.create_user(
            username='will',
            email='will@gmail.com',
            password="testpass123"
        )
        
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        
        admin_user = User.objects.create_superuser(
            username = 'superadmin',
            email= 'super@gmail.com',
            password = 'testpass123'
        )
        
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'super@gmail.com')
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)
        

    def test_create_staff(self):
        User = get_user_model()

        admin_user = User.objects.create_user(
            username = 'superadmin',
            email= 'super@gmail.com',
            password = 'testpass123'
        )
        admin_user.is_staff = True
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'super@gmail.com')
        self.assertFalse(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)

class SignupTests(TestCase):
    '''test user signup requirements are met'''
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')

        
    def test_signup_form(self):
        '''Tests CustomUserCreationform is used'''
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
        
    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )