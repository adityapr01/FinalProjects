from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import unittest
import pyautogui


class TestFinalprojects(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def testvalidlogin(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(4)
    
    def testopenleave(self):
        #driver.maximize_window()
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(10)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a').click()
        time.sleep(6)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(2)
        select_can = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div")
        self.assertEqual(select_can.text, "CAN - Bereavement")
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/input").send_keys("2022-12-02")
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/i').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/input').send_keys("2022-12-03")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div/div[2]/i").click()
        pyautogui.typewrite('Start Day Only')
        pyautogui.press('enter')
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/div[2]/i").click()
        pyautogui.typewrite('Half Day - Morning')
        pyautogui.press('enter')
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]").send_keys("Pengajuan untuk kunjungan berduka")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/button').click()
        time.sleep(6)       
        
    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()
