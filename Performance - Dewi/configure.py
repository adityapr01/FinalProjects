from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestPIM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_add_KPIs(self):
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
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() #klik menu configure
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]").click() #sub menu KPIs
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() #klik button +Add
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Test2 KPIs") #klik button +Add
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/i").click() #select dropdown job title
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]").click() # input list select dropdown job title
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("50") # input min rating
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("") # input max rating
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div/label/span").click() # button onOff
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click() # button save
        time.sleep(5)

        #validasi
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_failed_add_KPIs(self):
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
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() #klik menu configure
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]").click() #sub menu KPIs
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() #klik button +Add
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Test2 KPIs") #klik button +Add
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/i").click() #select dropdown job title
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]").click() # input list select dropdown job title
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys(Keys.CONTROL + "a") # input min rating
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys(Keys.BACKSPACE) # input min rating
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("101") # input min rating
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys(Keys.CONTROL + "a") # input max rating
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys(Keys.BACKSPACE) # input max rating
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("99") # input max rating
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div/label/span").click() # button onOff
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click() # button save
        time.sleep(5)

        #validasi
        assert driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/span")

    def test_success_search_data_KPIs(self):
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
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() #klik menu configure
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]").click() #sub menu KPIs
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div[1]/div[2]/i").click() #select job title
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div[2]/div[3]").click() #select list job title
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() #button search
        time.sleep(2)

        #validasi
        response_data = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div").text
        self.assertIn('Test2 KPIs', response_data)

    def test_success_reset_data_KPIs(self):
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
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() #klik menu configure
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]").click() #sub menu KPIs
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div[1]/div[2]/i").click() #select job title
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div[2]/div[3]").click() #select list job title
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]").click() #button reset
        time.sleep(3)

        #validasi
        response_data = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text
        self.assertIn('(50) Records Found', response_data)

    def test_success_edit_data_KPIs(self):
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
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() #klik menu configure
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]").click() #sub menu KPIs
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[1]/i").click() #button edit
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div/label/span").click() #button onOff
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click() #button save
        time.sleep(6)

        #validasi
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_success_delete_data_KPIs(self):
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
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() #klik menu configure
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]").click() #sub menu KPIs
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[2]/i").click() #sub button delete
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click() #sub confirm button delete
        time.sleep(3)

        #validasi
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_success_add_trackers(self):
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
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() #klik menu configure
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]").click() #klik sub menu trackers
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() #klik button +Add
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys("test trackers") #input tracker name
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/input").send_keys("test") #input employee name
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]").click() #input list employee name
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[1]/input").send_keys("test") #input reviews
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div[3]").click() #input list reviews
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click() #button save
        time.sleep(5)

        #validasi
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_success_search_data_trackers(self):
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
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() #klik menu configure
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]").click() #klik sub menu trackers
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("test") #input employename
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div[2]/div[3]").click() #input list employe name
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() #button search
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div").text
        self.assertIn('Tester Test', response_data)

    def test_success_reset_data_trackers(self):
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
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() #klik menu configure
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]").click() #klik sub menu trackers
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("test") #input employename
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div[2]/div[3]").click() #input list employe name
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]").click() #button reset
        time.sleep(3)

        #validasi
        response_data = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text
        self.assertIn('(10) Records Found', response_data)

    def test_success_edit_data_trackers(self):
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
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() #klik menu configure
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]").click() #klik sub menu trackers
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[6]/div/button[2]/i").click() #button edit
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys(Keys.CONTROL + "a") #input trackers name
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys(Keys.BACKSPACE) #input trackers name
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys("Testing") #input trackers name
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click() #button saved
        time.sleep(5)

        #validasi
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_success_delete_data_trackers(self):
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
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() #klik menu configure
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]").click() #klik sub menu trackers
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[6]/div/button[1]/i").click() #klik button delete
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click() #klik button confirm delete
        time.sleep(5)

        #validasi
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()