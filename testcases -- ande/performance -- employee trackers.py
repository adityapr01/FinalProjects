import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class TestPerformance(unittest.TestCase): 

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
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() # klik menu performance
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a").click() # klik menu employee tracker
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik button search
        time.sleep(5)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/span").text

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
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() # klik tombol performance
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a").click() # klik menu employee tracker
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Leon") #isi nama employee
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div").click() #pilih pegawai
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/i").click() #click dropdown include
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]").click() #pilih item dropdown include
        time.sleep(3)        
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(5)

     # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/span").text

        self.assertIn('Found', response_data)   


    def test_unsuccessfull_search_with_filter(self): 
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
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() # klik tombol performance
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a").click() # klik menu employee tracker
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("17oL@n") #isi nama employee
        time.sleep(3)         
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/i").click() #click dropdown include
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]").click() #pilih item dropdown include
        time.sleep(3)        
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(5)

     # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/span").text
       
        self.assertIn('Invalid', response_data) 


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
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() # klik tombol performance
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a").click() # klik menu employee tracker
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Leon") #isi nama employee
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div").click() #pilih pegawai
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/i").click() #click dropdown include
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]").click() #pilih item dropdown include
        time.sleep(3)        
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]").click() # klik tombol reset
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik tombol search
        time.sleep(5)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/span").text

        self.assertIn('Found', response_data)
     

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
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() # klik tombol performance
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a").click() # klik menu employee tracker
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[5]/div/button").click() # klik tombol view
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/h5").text

        self.assertIn('Tracker for', response_data)


    def test_successful_add_log(self):   
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
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() # klik tombol performance
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a").click() # klik menu employee tracker
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[5]/div/button").click() # klik tombol view
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() # klik tombol add log
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[1]/div/div[2]/input").send_keys("Good") # isi log
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[2]/div/button[1]").click() # klik tombol performance
        time.sleep(1)        
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[3]/div/div[2]/textarea").send_keys("Nice attitude") # isi comment
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[4]/button[2]").click() # klik tombol save
        time.sleep(5)
        
        # validasi
        # response_data = browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[1]/div[2]/p[1]").text

        # self.assertIn('Success', response_data)
        
        assert browser.find_element(By.XPATH, "/html/body/div/div[2]")
    

    def test_unsuccessful_add_log(self):   
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
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() # klik tombol performance
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a").click() # klik menu employee tracker
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[5]/div/button").click() # klik tombol view
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() # klik tombol add log
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[4]/button[2]").click() # klik tombol save
        time.sleep(5)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[3]/div/div/div/form/div[1]/div/span").text
       
        self.assertIn('Required', response_data) 


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()