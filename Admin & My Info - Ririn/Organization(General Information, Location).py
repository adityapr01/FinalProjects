import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Organization(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_Success_Edit_Generalinfo(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # log in
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik admin menu
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #klik sub menu Organization
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a").click() #klik General Information
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div/label/span").click() #klik Edit
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input").send_keys(Keys.CONTROL,"a") 
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input").send_keys(Keys.BACKSPACE) 
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input").send_keys("MelonHRM") #edit menjadi MelonHRM
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[7]/button") #save

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_Failed_Edit_Generalinfo(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # log in
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik admin menu
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #klik sub menu Organization
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a").click() #klik General Information
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div/label/span").click() #klik Edit
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input").send_keys(Keys.CONTROL,"a") 
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input").send_keys(Keys.BACKSPACE) 
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[7]/button") #save

        #validationn
        response_message = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/span").text

        self.assertEqual('Required', response_message)

    def test_Success_Add_Location(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # log in
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik admin menu
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #klik sub menu Organization
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]").click() #klik Locations
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/button").click() #klik Add
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys("Jakarta") #input name 
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div").click() #klik arrow down
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div[2]/div[101]").click() #pilih indonesia
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]") #save

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_Failed_Add_Location(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # log in
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik admin menu
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #klik sub menu Organization
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]").click() #klik Locations
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/button").click() #klik Add
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys("Jakarta") #input name 
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]") #save
        time.sleep(3)

        #validationn
        response_message = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/span").text

        self.assertEqual('Required', response_message)

    def test_Success_Edit_Location(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # log in
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik admin menu
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #klik sub menu Organization
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]").click() #klik Locations
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/button").click() #klik button Edit gambar pena (Jakarta)
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys(Keys.CONTROL,"a") 
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys(Keys.BACKSPACE) 
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys("Solo") #Edit menjadi Solo 
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]") #save

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_Success_Delete_Location(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # log in
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik admin menu
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #klik sub menu Organization
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]").click() #klik Locations
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[4]/div/div[7]/div/button[1]").click() #klik button delete (Solo)
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div[3]/button[2]").click() #konfirmasi delete
        time.sleep(1)

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__": 
     unittest.main()