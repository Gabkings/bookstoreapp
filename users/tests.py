from django.test import TestCase
from django.contrib.auth import get_user_model
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
       
        