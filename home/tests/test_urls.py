from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home, technologies, about, services, contact, signup, handlelogin, handlelogout


class TestUrls(SimpleTestCase):

    def test_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_technologies(self):
        url = reverse('technologies')
        self.assertEquals(resolve(url).func, technologies)

    def test_about(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_services(self):
        url = reverse('services')
        self.assertEquals(resolve(url).func, services)

    def test_contact(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)

    def test_signup(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

    def test_handlelogin(self):
        url = reverse('handlelogin')
        self.assertEquals(resolve(url).func, handlelogin)

    def test_handlelogout(self):
        url = reverse('handlelogout')
        self.assertEquals(resolve(url).func, handlelogout)
