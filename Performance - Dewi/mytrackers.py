from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestPIM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_view_my_tracker(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #klik button login
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() #klik menu performance
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #klik button menu mytrackers
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div[4]/div/button").click() #klik button view
        time.sleep(2)

        # validasi
        response_data = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/h5").text
        self.assertIn('Tracker Logs', response_data)

    def test_success_add_log_my_trackers(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #klik button login
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() #klik menu performance
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #klik button menu mytrackers
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div[4]/div/button").click() #klik button view
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() #klik +Add
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[1]/div/div[2]/input").send_keys("good log") #input log
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[2]/div/button[1]").click() #positive
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[3]/div/div[2]/textarea").send_keys("good comment") #input comment
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[4]/button[2]").click() #button save
        time.sleep(3)

        #validasi
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_failed_add_log_my_trackers(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #klik button login
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() #klik menu performance
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #klik button menu mytrackers
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div[4]/div/button").click() #klik button view
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() #klik +Add
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[4]/button[2]").click() #button save
        time.sleep(3)

        #validasi
        assert driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[3]/div/span")


    def test_success_edit_log_my_trackers(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #klik button login
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() #klik menu performance
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #klik button menu mytrackers
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div[4]/div/button").click() #klik button view
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[1]/li/button").click() #button titik3
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[1]/li/ul/li[1]").click() #klik edit
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[1]/div/div[2]/input").send_keys(Keys.CONTROL + "a") #input log
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[1]/div/div[2]/input").send_keys(Keys.CONTROL + "a") #input log
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[1]/div/div[2]/input").send_keys(Keys.BACKSPACE) #input log
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[1]/div/div[2]/input").send_keys("not good") #input log
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[2]/div/button[2]").click() #negative
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[3]/div/div[2]/textarea").send_keys(Keys.CONTROL + "a") #input comment
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[3]/div/div[2]/textarea").send_keys(Keys.BACKSPACE) #input comment
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[3]/div/div[2]/textarea").send_keys("testing") #input comment
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[4]/button[2]").click() #input comment
        time.sleep(3)

        #validasi
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_success_delete_log_my_trackers(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #klik button login
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() #klik menu performance
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #klik button menu mytrackers
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div/div/div[4]/div/button").click() #klik button view
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[1]/li/button").click() #button titik3
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[1]/li/ul/li[2]").click() #klik delete
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click() #confirm delete
        time.sleep(3)

        #validasi
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")
        
    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()