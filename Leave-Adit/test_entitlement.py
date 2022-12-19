from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import unittest



class TestFinalprojects(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def testentitlement(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(10)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(4)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a').click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a").click()
        time.sleep(6)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/input").send_keys("Paul Collings")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div[2]/div[2]/span").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[3]/div/div[2]/input").send_keys("1")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/button[2]").click()
        time.sleep(6)
    
    def testEmployeeEntitlements(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(10)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(4)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a').click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Aaliyah Haq")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[2]/form/div[2]/button").click()
        time.sleep(2)

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()