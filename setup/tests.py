from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/gilunix/Documentos/Projetos/Alura/Python/TDD_busca_animal/chromedriver')

    def tearDown(self):
        self.browser.quit()
