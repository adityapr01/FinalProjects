import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Job(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())   

    def test_l_Success_Add_Jobtitle(self):
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() #klik sub menu Job
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a").click() #klik JobTitle
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button/i").click() #klik Add
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys("SQA") #input Job Title
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]") #save

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_m_Success_Edit_Jobtitle(self):
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() #klik sub menu Job
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a").click() #klik JobTitle
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[23]/div/div[4]/div/button[2]/i").click() #klik button edit SQA
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys(Keys.BACKSPACE)
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys("Soft QA")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]") #save

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_n_success_delete_Job(self):
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() #klik sub menu Job
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a").click() #klik JobTitle
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[24]/div/div[4]/div/button[1]").click() #klik button delete di SQA
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div[3]/button[2]").click() #konfirmasi delete

        #validasi
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")



    def test_o_Success_Add_Paygrade(self):
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() #klik sub menu Job
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]").click() #klik PayGrade
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button/i").click() #klik Add
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys("grade 6") #input grade 6
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]") #save

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_p_Failed_Add_Paygrade(self):
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() #klik sub menu Job
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]").click() #klik PayGrade
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button/i").click() #klik Add
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]") #save

        #validationn
        response_message = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/span").text

        self.assertEqual('Required', response_message)

    def test_q_Success_Edit_Paygrade(self):
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() #klik sub menu Job
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]").click() #klik PayGrade
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[6]/div/div[4]/div/button[2]/i").click() #klik Edit button gambar pena (grade 6)
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[1]/div/form/div[1]/div/div/div/div[2]/input").send_keys(Keys.CONTROL,"a") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[1]/div/form/div[1]/div/div/div/div[2]/input").send_keys(Keys.BACKSPACE) 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[1]/div/form/div[1]/div/div/div/div[2]/input").send_keys("grade 8") #edit menjadi grade 8
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[1]/div/form/div[2]/button[2]") #save

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_r_Success_Delete_Paygrade(self):
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() #klik sub menu Job
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]").click() #klik PayGrade
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[6]/div/div[4]/div/button[1]/i").click() #klik delete button (grade 8)
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div[3]/button[2]").click() #konfirmasi delete
        
        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")


    def test_s_Success_Add_EmployeeStatus(self):
        
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() #klik sub menu Job
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]/a").click() #klik EmploymentStatus
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button").click() #klik Add
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button").click() #klik 
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys("Freelancer") #input Employment Status
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]") #save

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_t_Success_Edit_EmployeeStatus(self):
        
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() #klik sub menu Job
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]/a").click() #klik EmploymentStatus
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div[3]/div/button[2]").click() #klik button edit gambar pena Freelancer
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys(Keys.CONTROL,"a") 
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys(Keys.BACKSPACE) 
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys("Freelancer2") #edit menjadi Freelancer2
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]") #save

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def test_u_Success_Delete_EmployeeStatus(self):
        
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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() #klik sub menu Job
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]/a").click() #klik EmploymentStatus
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div[3]/div/button[1]").click() #klik button delete dari Freelancer
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div[3]/button[2]").click() #konfirmasi delete
        

        #validationn
        assert driver.find_element(By.XPATH, "/html/body/div/div[2]")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__": 
     unittest.main()