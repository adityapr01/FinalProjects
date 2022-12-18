import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class TestRecruitment(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_successful_add(self):   
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
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() # klik tombol add
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input").send_keys("Jonas") # isi first name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input").send_keys("Stacey") # isi middle name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[3]/div[2]/input").send_keys("Johnson") # isi last name name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div[2]/i").click() #klik dropwdown vacancy
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[2]/div[2]").click() #pilih item dropdown vacancy
        time.sleep(3)   
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input").send_keys("test123@gmail.com") # isi email
        time.sleep(1) 
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]").click() # klik tombol save
        time.sleep(5)
        

        # # validasi
        assert browser.find_element(By.XPATH, "/html/body/div/div[2]")
        

    def test_unsuccessfull_add(self):   
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
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() # klik tombol add
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]").click() # klik tombol save
        time.sleep(5)
        

         # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[1]/span").text

        self.assertIn('Required', response_data)


    def test_successfull_edit(self):   
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
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[7]/div/button[1]").click() # klik tombol view
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div/div/label/span").click() # klik toggle edit
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input").click() # klik first name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input").send_keys(Keys.CONTROL + "a") # ctrl+a first name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input").send_keys(Keys.BACKSPACE) # del first name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input").send_keys("Atha") # isi first name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[2]/div/form/div[8]/button").click() # klik tombol save
        time.sleep(3)
        
        # # validasi
        assert browser.find_element(By.XPATH, "/html/body/div/div[2]")


    def test_successfull_view(self):   
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
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[1]").click() # klik tombol view
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div/h6").text

        self.assertIn('Candidate Profile', response_data)
    

    def test_successfull_delete(self):   
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
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[4]/div/div[7]/div/button[2]").click() # klik tombol delete
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div/div/div[3]/button[2]").click() # klik confirm delete
        time.sleep(5)
        
        # validasi
        assert browser.find_element(By.XPATH, "/html/body/div/div[2]")
    


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
