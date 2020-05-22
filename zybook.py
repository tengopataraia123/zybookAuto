from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome("C:/chromedriver.exe")

# In[2]:
def log_in(username,password,chapter):
	global driver
	driver.get("https://learn.zybooks.com/#/signin")
	driver.find_element_by_xpath('//*[@id="ember936"]').send_keys(username)
	driver.find_element_by_xpath('//*[@id="ember942"]').send_keys(password)
	driver.find_element_by_xpath('//*[@id="ember944"]').click()
	sleep(3)
	driver.get("https://learn.zybooks.com/zybook/SDSUCompE271DavitashviliSummer2020/chapter/"+chapter+"/section/1")


# In[8]:


def do_short():
    for elem in driver.find_elements_by_class_name("short-answer-question"):
        elem.find_element_by_class_name("show-answer-button").click()
        elem.find_element_by_class_name("show-answer-button").click()
        answer = elem.find_element_by_class_name("forfeit-answer").text
        elem.find_element_by_class_name("zb-text-area").send_keys(answer)
        elem.find_element_by_class_name("check-button").click()
        sleep(2)


# In[9]:


def do_multiple():
    for elem in driver.find_elements_by_class_name("multiple-choice-question"):
        for i in elem.find_elements_by_class_name("zb-radio-button"):
            i.find_element_by_tag_name("label").click()
            sleep(0.3)
            if(elem.find_element_by_class_name("message").text == 'Correct'):
                break
            sleep(0.1)


# In[12]:


def write():
    while True:
        do_short()
        do_multiple()
        sleep(10)
        driver.find_element_by_class_name("next").find_element_by_tag_name("a").click()
        sleep(3)

def main():
	username = input("Enter your zybook email: ")
	password = input("Enter your zybook password : ")
	chapter = input("What chapter you what to be done: ")

	log_in(username,password,chapter)
	sleep(10)
	write()

if __name__ == "__main__":
	main()

