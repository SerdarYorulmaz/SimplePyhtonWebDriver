from selenium import webdriver
import time
browser=webdriver.Chrome()

browser.get("https://www.instagram.com")
#//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a -->giris butuonu xpat yolu
#time.sleep(10) baslangic icin sayafaya yenilemek gerek hata alabiliriz -- xpat id gore islem yapar
time.sleep(10)
giris_yap=browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a") #id gore giris yaptik

giris_yap.click() # giris yap  tikladik
time.sleep(5) # 5 bekliyoruz

username=browser.find_element_by_name("username")
password=browser.find_element_by_name("password")

username.send_keys("--------")
password.send_keys("----------")
time.sleep(5) # 5 bekliyoruz
giris_yap2=browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/button")
giris_yap2.click()
time.sleep(10) # 5 bekliyoruz
browser.close() # browser kapatiyoruz
