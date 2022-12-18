import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class TestMyTime(unittest.TestCase): 

    def setUp(self): 
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    def test_submit_mytimesheet(self):   
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
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click() # klik menu time
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() # klik dropdown time
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a").click() # klik mytimesheet
        time.sleep(5)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button[2]").click() # klik submit mytimesheet
        time.sleep(1)

    def test_edit_mytimesheet(self):   
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click() # klik menu time
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() # klik dropdown time
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a").click() # klik mytimesheet
        time.sleep(5)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button").click() # klik edit mytimesheet
        time.sleep(5)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div/div/input").send_keys("Ac") # input Project mytimesheet
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div/div[2]/div[1]/span").click() # input Project mytimesheet
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[2]/i").click() # klik dropdown Project mytimesheet
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div[2]/div[2]").click() # klik value dropdown Project mytimesheet
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button[3]").click() # klik save edit mytimesheet
        time.sleep(1)        


    def test_reset_mytimesheet(self):   
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click() # klik menu time
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() # klik dropdown time
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a").click() # klik mytimesheet
        time.sleep(5)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button").click() # klik edit mytimesheet
        time.sleep(5)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div/div/input").send_keys("Ac") # input Project mytimesheet
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div/div[2]/div[1]/span").click() # input Project mytimesheet
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[2]/i").click() # klik dropdown Project mytimesheet
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div[2]/div[2]").click() # klik value dropdown Project mytimesheet
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button[2]").click() # klik save edit mytimesheet
        time.sleep(1)

    def test_cancel_mytimesheet(self):   
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click() # klik menu time
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() # klik dropdown time
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a").click() # klik mytimesheet
        time.sleep(5)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button").click() # klik edit mytimesheet
        time.sleep(5)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button[1]").click() # klik cancel mytimesheet
        time.sleep(5)

    def test_submit_empty_mytimesheet(self):   
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click() # klik menu time
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() # klik dropdown time
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a").click() # klik mytimesheet
        time.sleep(5)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button").click() # klik edit mytimesheet
        time.sleep(5)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button[3]").click() # klik sumbit mytimesheet
        time.sleep(5)

        #validasi
        assert browser.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[1]/div/span")
       
      
    
if __name__ == "__main__": 
    unittest.main()