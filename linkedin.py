from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag

def login(driver):
    username = driver.find_element_by_id("username")
    username.send_keys("vikrant-pathak")
 
    password = driver.find_element_by_id("password")
    password.send_keys("Vikrant@2000!")
 
    driver.find_element_by_id("login-submit").click()         
  
def goto_network(driver):
    driver.find_element_by_id("mynetwork-tab-icon").click()
  
def send_requests():
    n = int(input("Number of requests: "))  # Convert input to int
   
    for _ in range(n):  # Use _ instead of unused variable i
        pag.click(880, 770)  
    print("Done !")
      
def main():
    url = "https://www.linkedin.com/"
    network_url = "https://www.linkedin.com/mynetwork/"
    driver = webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver_win32.zip\chromedriver.exe")
    driver.get(url)
    
    login(driver)
    goto_network(driver)
    send_requests()

if __name__ == '__main__':
    main()
