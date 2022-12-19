import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class MyInfo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def _Success_Edit_Personal_Details(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # log in
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span").click() #klik menu My info
        time.sleep(1)
        driver.find_element(By.NAME, "firstName").send_keys(Keys.CONTROL,"a", Keys.BACKSPACE) 
        time.sleep(2)
        driver.find_element(By.NAME, "firstName").send_keys("Sam") #edit nama depan
        time.sleep(1)
        driver.find_element(By.NAME, "middleName").send_keys(Keys.CONTROL,"a", Keys.BACKSPACE) 
        time.sleep(1)
        driver.find_element(By.NAME, "middleName").send_keys("Smith") #edit nama tengah
        time.sleep(1)
        driver.find_element(By.NAME, "lastName").send_keys(Keys.CONTROL,"a", Keys.BACKSPACE)
        time.sleep(1)
        driver.find_element(By.NAME, "lastName").send_keys("Jo") #edit nama belakang
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()

        #validation
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def _Success_Edit_Employeeid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # log in
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span").click() #klik menu My info
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.CONTROL,"a", Keys.BACKSPACE) 
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input").send_keys("123") #edit employee id
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()

        #validation
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def _Success_Edit_Nickname(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # log in
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span").click() #klik menu My info
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys(Keys.CONTROL,"a", Keys.BACKSPACE) 
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys("sammy") #edit nickname
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()

        #validation
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def _Failed_Edit_Personal_Details(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # log in
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span").click() #klik menu My info
        time.sleep(1)
        driver.find_element(By.NAME, "firstName").send_keys(Keys.CONTROL,"a", Keys.BACKSPACE) #hapus dan kosongi nama depan
        time.sleep(2)
        driver.find_element(By.NAME, "middleName").send_keys(Keys.CONTROL,"a", Keys.BACKSPACE) 
        time.sleep(1)
        driver.find_element(By.NAME, "middleName").send_keys("Smith") #input nama tengah
        time.sleep(1)
        driver.find_element(By.NAME, "lastName").send_keys(Keys.CONTROL,"a", Keys.BACKSPACE) ##hapus dan kosongi nama belakang
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()

        #validation
        response_message = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/span").text

        self.assertEqual('Required', response_message)

class ContactDetail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_Success_Edit_Contact_Details(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # log in
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span").click() #klik menu My info
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").click() #klik submenu Personal Details
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Santa") #edit Street 1
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("Paulo") #edit Street 2
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input").send_keys("Abracadabra") #edit City
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button").click() #save

        #validation
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]") 

    def test_Failed_Edit_Contact_Details_Emptying_Alldata(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # input username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # input password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # log in
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span").click() #klik menu My info
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").click() #klik submenu Personal Details
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys(Keys.CONTROL,"a", Keys.BACK_SPACE) #kosongi street 1
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(Keys.CONTROL,"a", Keys.BACK_SPACE) #kosongi street 2
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input").send_keys(Keys.CONTROL,"a", Keys.BACK_SPACE) #kosongi city
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input").send_keys(Keys.CONTROL,"a", Keys.BACK_SPACE) #kosongi work email
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input").send_keys(Keys.CONTROL,"a", Keys.BACK_SPACE) #kosongi work
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button").click() #save

        #validationn
        #tidak ada alert 'Required' yang muncul, jadi Status data tetap sukses diupdate. seharusnya FAILED



    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__": 
     unittest.main()