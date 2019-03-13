from django.test import TestCase
from .models import Company, Employee
from django.contrib.auth import get_user_model

#Create your tests here
class CompanyTestCase(TestCase):

    def test_company_homepage(self):
        response = self.client.get('/company/homepage/', follow=True)
        self.assertEqual(response.status_code, 200)
