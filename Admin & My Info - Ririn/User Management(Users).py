import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_login_success(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(3) 

        # validasi 
        assert driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a") #masuk ke dashboard

class UserManagementTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_Success_Add_User(self):
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
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() # klik add 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div").click() #arrow job role
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[3]").click() #pilih ESS
        time.sleep(3) 
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[1]").click() #arrow status
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]").click() #pilih enable
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("Lisa Andrews") #input employee name
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div").click() #klik Lisa Andrews
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Lisa1234") #input username
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Lisa1234!") #input password
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Lisa1234!") #confirm password
        time.sleep(1)
        driver.find_element(By. XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
        
        #validasi
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]") 

    def test_b_Failed_Add_User(self):
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
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() # klik add 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div").click() #arrow job role
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[3]").click() #pilih ESS
        time.sleep(3) 
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[1]").click() #arrow status
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]").click() #pilih enable
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("Lisa") #input employee name invalid
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Lisa12345") #input username
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Lisa1234!") #input password
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Lisa1234!") #confirm password
        time.sleep(1)
        driver.find_element(By. XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
        time.sleep(1)
        
        #validation
        assert driver.find_element(By. XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/span")

    def test_c_Success_search_username(self):
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys('Lisa1234') #search using username
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click #klik search

        #validation
        assert driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div")

    def test_d_Success_search_userrole(self):
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
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div").click() #klik dropdown user role
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]").click() #pilih dan klik ESS
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click #klik search

        #validation
        assert driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[3]/div")
        
    def test_e_Success_search_Employeename(self):
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input").send_keys('Lisa Andrews') #search using Employeename
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div").click() #klik Lisa Andrews
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click #klik search

        #validation
        assert driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[4]/div")

    def test_f_Success_search_status(self):
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[1]").click() #klik dropdown status
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]").click() #pilih dan klik Enable
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click #klik search

        #validation
        assert driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[5]/div")
        
    def test_g_Success_search_using_allrequirem(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # log in
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() # klik admin menu
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys('Lisa1234') #search using username
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div").click() #klik dropdown user role
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]").click() #pilih dan klik ESS
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input").send_keys('Lisa Andrews') #search using Employeename
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div").click() #klik Lisa Andrews
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[1]").click() #klik dropdown status
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]").click() #pilih dan klik Enable
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click #klik search

        #validation
        assert driver.find_element(By.XPATH, "//html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div")
        
    def test_h_Failed_search_username(self):
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys('Lisa') #search using username
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click #klik search

        #validation
        assert driver.find_element(By. XPATH, "/html/body/div/div[2]")

    def test_i_Success_search_Employeename(self):
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input").send_keys('Andrews') #search using Employeename
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click #klik search

        #validation
        assert driver.find_element(By. XPATH, "/html/body/div/div[2]")

    def test_j_Success_Edit_Employeename(self):
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
        driver.find_element(By. XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[28]/div/div[6]/div/button[2]/i").click() #klik button pena edit Lisa1234
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys(Keys.CONTROL,"a")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys(Keys.BACKSPACE) 
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Lisa12345") #edit menjadi Lisa12345
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click() #save
        time.sleep(1)

        #validation
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

        
    def test_k_Success_Delete_Employeename(self):
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
        driver.find_element(By. XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[25]/div/div[6]/div/button[1]/i").click() #klik button delete (Lisa12345)
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div[3]/button[2]").click() #konfirmasi delete
        
        #validation
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")


    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__": 
     unittest.main()