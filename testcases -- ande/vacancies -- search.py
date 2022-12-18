import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class TestRecruitment(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_successfull_search_without_filter(self):   
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a").click() # klik menu recruitment
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click() # klik menu vacancies
        time.sleep(1)        
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text

        self.assertIn('Found', response_data)


    def test_successfull_search_with_filter(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a").click() # klik tombol recruitment
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click() # klik menu vacancies
        time.sleep(3) 
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i").click() #click dropdown vacancy
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[5]").click() #pilih item dropdown vacancy
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i").click() #click dropdown hiring manager
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[3]").click() #pilih item dropdown hiring manager
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i").click() #click dropdown status
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]").click() #pilih item dropdown status
        time.sleep(3)        
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(4)

     # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text

        self.assertIn('Found', response_data)
  

    def test_successfull_reset_filter(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a").click() # klik tombol recruitment
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click() # klik menu vacancies
        time.sleep(3) 
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i").click() #click dropdown vacancy
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[5]").click() #pilih item dropdown vacancy
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i").click() #click dropdown hiring manager
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[3]").click() #pilih item dropdown hiring manager
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i").click() #click dropdown status
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]").click() #pilih item dropdown status
        time.sleep(3)        
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(4)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]").click() # klik tombol reset
        time.sleep(4)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(4)
    
        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text

        self.assertIn('Found', response_data)



    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()