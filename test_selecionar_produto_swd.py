# 1 - Bibliotecas
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (Opcional)
class Teste_Produtos():
    # 2.1 Atributos
    url = "https://www.saucedemo.com"
    # 2.2 Funçoes e Metodos
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
           self.driver.quit()


    def test_selecionar_produto(self):
         self.driver.get(self.url)
         self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
         self.driver.find_element(By.NAME,"password").send_keys("secret_sauce")
         self.driver.find_element(By.CSS_SELECTOR,"input.submit-button.btn_action").click