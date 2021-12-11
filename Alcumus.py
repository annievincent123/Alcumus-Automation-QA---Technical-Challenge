from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
ser = Service(r"C:\Users\anita.vincent\Downloads\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
import time

driver.get("https://computer-database.gatling.io/computers?p=0&n=10&s=name&d=asc")
print(driver.title)
driver.maximize_window()
#Testing if cancel button works
driver.find_element_by_xpath("/html/body/section/div[1]/form/a").click()
driver.find_element_by_xpath("/html/body/section/form/fieldset/div[1]/div/input").send_keys("ASUS-4") # adding the values for a computer
driver.find_element_by_xpath("/html/body/section/form/fieldset/div[2]/div/input").send_keys("2017-01-23")
driver.find_element_by_xpath("/html/body/section/form/fieldset/div[3]/div/input").send_keys("2020-01-23")
sel = Select(driver.find_element_by_xpath("/html/body/section/form/fieldset/div[4]/div/select"))
sel.select_by_visible_text("ASUS")
driver.find_element_by_xpath("/html/body/section/form/div/a").click()
#Testing if Create this computer works
driver.find_element_by_xpath("/html/body/section/div[1]/form/a").click()
driver.find_element_by_xpath("/html/body/section/form/fieldset/div[1]/div/input").send_keys("ASUS-4") # adding the values for a computer
driver.find_element_by_xpath("/html/body/section/form/fieldset/div[2]/div/input").send_keys("2017-01-23")
driver.find_element_by_xpath("/html/body/section/form/fieldset/div[3]/div/input").send_keys("2020-01-23")
sel = Select(driver.find_element_by_xpath("/html/body/section/form/fieldset/div[4]/div/select"))
sel.select_by_visible_text("ASUS")
driver.find_element_by_xpath("/html/body/section/form/div/input").click()




#Testing if Filter by name works
driver.find_element_by_xpath("/html/body/section/div[2]/form/input[1]").send_keys("ASUS")
driver.find_element_by_xpath("/html/body/section/div[2]/form/input[2]").click()

#Testing if number of computers has increased from 574
driver.get("https://computer-database.gatling.io/computers?p=0&n=10&s=name&d=asc")

#print(driver.find_element_by_id("main").text)

if driver.find_element_by_xpath("/html/body/section/h1").text =="574 computers found" :
    print("Error: New computer not added")
else:
    print("New computer successfully added")
#Error new computer is not being added

#Testing if updation works
driver.find_element_by_xpath("/html/body/section/table/tbody/tr[1]/td[1]/a").click()
driver.find_element_by_xpath("/html/body/section/form[1]/fieldset/div[2]/div/input").send_keys("2017-01-23")
driver.find_element_by_xpath("/html/body/section/form[1]/div/input").click()
if driver.find_element_by_xpath("/html/body/section/table/tbody/tr[1]/td[2]").text =="-" :
    print("Error: Updation not added")
else:
    print("Updation successfully added")

#Testing pagination
driver.get("https://computer-database.gatling.io/computers?p=0&n=10&s=name&d=asc")
driver.find_element_by_xpath("/html/body/section/div[2]/ul/li[3]/a").click()
if driver.find_element_by_xpath("/html/body/section/div[2]/ul/li[2]/a").text =="Displaying 11 to 20 of 574" :
    print("Pagination successfully added")
else:
    print("Error: Pagination not successful")

#Testing if 'previous' button works (Automatically comes to 'Homepage' if 'previous' button works
driver.find_element_by_xpath("/html/body/section/div[2]/ul/li[1]/a").click()

# Testing if deleting a computer works
#driver.get("https://computer-database.gatling.io/computers?p=0&n=10&s=name&d=asc")
driver.find_element_by_xpath("/html/body/section/table/tbody/tr[1]/td[1]/a").click()
driver.find_element_by_xpath("/html/body/section/form[2]/input").click()

if driver.find_element_by_xpath("/html/body/section/h1").text == "574 computers found":
    print("Error: Computer not deleted")
else:
    print("Computer successfully deleted")

driver.quit()