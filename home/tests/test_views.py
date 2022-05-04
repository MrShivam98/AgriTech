from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()
class TestViews(TestCase):

    def setUp(self):
        user1 = User(username='user1', email='user1@agritech.com')
        user1_pw = 'user123'
        self.user1_pw = user1_pw
        user1.is_staff = False
        user1.is_superuser = False
        user1.set_password(user1_pw)
        user1.save()
        self.user1 = user1
        self.client = Client()
        self.home_url = reverse('home')
        self.technologies_url = reverse('technologies')
        self.about_url = reverse('about')
        self.contact_url = reverse('contact')
        self.services_url = reverse('services')
        self.login_url = reverse('handlelogin') 
        self.signup_url = reverse('signup') 
    
    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
    
    def test_user_password(self):
        self.assertTrue(self.user1.check_password(self.user1_pw))

    def test_login(self):
        data = {'phone': 'user1', 'password': self.user1_pw}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.request.get('PATH_INFO'), self.login_url)

    def test_home(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_technologies(self):
        response = self.client.get(self.technologies_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/technologies.html')

    def test_about(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_contact_get(self):
        response = self.client.get(self.contact_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_contact_post(self):
        response = self.client.post(self.contact_url, {
            'name': 'user1',
            'email': 'user1@agritech.com',
            'phone': '1234567890',
            'content': 'this is a issue'
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_services(self):
        response = self.client.get(self.services_url)
        self.assertEquals(response.status_code, 302)

    def test_services_login(self):
        self.client.login(username=self.user1.username, password=self.user1_pw)
        response = self.client.get(self.services_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/services.html')

    def test_signup_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/signup.html')

    def test_signup_post(self):
        response = self.client.post(self.signup_url, {
            'fname': 'user',
            'lname': '1',
            'email': 'user1@agritech.com',
            'phone': '123456789',
            'password': self.user1_pw,
            'conpassword': self.user1_pw
        })
        self.assertEqual(response.status_code, 302)
