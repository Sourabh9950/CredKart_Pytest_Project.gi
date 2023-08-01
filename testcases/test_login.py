from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Credkart_Login():

    def test_pagetitle_001(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://automation.credence.in/")
        if driver.title == "CredKart":
            driver.save_screenshot(".\\screenshot\\test_pagetitle_001_pass.PNG")
            assert True
        else:
            driver.save_screenshot(".\\screenshot\\test_pagetitle_001_fail.PNG")
            assert False
        driver.close()


    def test_Credkart_Login_002(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH,"//input[@name='email']").send_keys("Credencetest@test.com")
        driver.find_element(By.CSS_SELECTOR,"input[id='password']").send_keys("Credence@123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        try:
            driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
            print("Login testcase is passed")
            driver.save_screenshot(".\\screenshot\\test_Credkart_Login_002_pass.PNG")
            assert True
        except:
            print("Login testcase is failed")
            driver.save_screenshot(".\\screenshot\\test_Credkart_Login_002_fail.PNG")
            assert False
        driver.close()
