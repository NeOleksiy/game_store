from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.urls import reverse_lazy, reverse
import time
from users.models import Users


class RegistrationsTestCase(LiveServerTestCase):
    fixtures = ['fixtures/users.json']

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.user = Users.objects.first()
        super(RegistrationsTestCase, self).setUp()

    def tearDown(self) -> None:
        self.driver.quit()
        super(RegistrationsTestCase, self).tearDown()

    def test_register(self):
        selenium = self.driver
        path = '%s%s' % (self.live_server_url, reverse('users:registration'))
        selenium.get(path)
        selenium.find_element(By.NAME, 'first_name').send_keys('test')
        selenium.find_element(By.NAME, 'last_name').send_keys('test')
        selenium.find_element(By.NAME, 'username').send_keys('test')
        selenium.find_element(By.NAME, 'email').send_keys('alyefim@gmail.com')
        selenium.find_element(By.NAME, 'password1').send_keys('1m2m3m4+')
        selenium.find_element(By.NAME, 'password2').send_keys('1m2m3m4+')
        selenium.find_element(By.XPATH, '//input[@value="Создать аккаунт"]').send_keys(Keys.RETURN)
        redirect = '%s%s' % (self.live_server_url, reverse('users:login'))
        self.assertEquals(selenium.current_url, redirect)
        self.assertNotEquals(selenium.current_url, path)

    def test_login(self):
        selenium = self.driver
        selenium.implicitly_wait(5)
        path = '%s%s' % (self.live_server_url, reverse('users:login'))
        selenium.get(path)
        selenium.find_element(By.NAME, 'username').send_keys(self.user.username)
        selenium.find_element(By.NAME, 'password').send_keys('12345')
        selenium.find_element(By.XPATH, '//input[@value="Авторизоваться"]').send_keys(Keys.RETURN)
        redirect = '%s%s' % (self.live_server_url, reverse('products'))
        self.assertEquals(selenium.current_url, redirect)
        self.assertNotEquals(selenium.current_url, path)



