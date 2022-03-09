from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/gilunix/Documentos/Projetos/Alura/Python/TDD_busca_animal/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_abre_janela_do_chrome(self):
        self.browser.get(self.live_server_url)

    def test_exemplo_de_erro(self):
        '''Teste de exemplo de falha.'''
        self.fail()

