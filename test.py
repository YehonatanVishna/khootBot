from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
import threading
import names

game_id =input("game id:")
def chouse_random(browser):
    while(browser.current_url!= "https://kahoot.it/gameblock" and browser.current_url!= "https://kahoot.it/ranking"):
        time.sleep(1)
    if(browser.current_url == "https://kahoot.it/ranking"):
        return None
    print(111)
    listOptions = ["ejIHBZ","kUObYJ", "duxqxQ", "cGdwlw"]
    try:
    	elem2 = browser.find_element(By.CLASS_NAME, listOptions[random.randint(0,3)])
    	elem2.click()
    finally:
    	print()
    chouse_random(browser)
def boom_quiz():
    # browser = webdriver.Chrome()
    op = webdriver.ChromeOptions()
    op.add_argument('--headless')
    browser = webdriver.Chrome(options=op)
    browser.get('https://kahoot.it/')
    elem = browser.find_element(By.ID, 'game-input')
    elem.send_keys(game_id + Keys.RETURN)
    time.sleep(1)
    # time.sleep(random.uniform(2.5,5))
    while(browser.current_url!= "https://kahoot.it/join"):
        time.sleep(0.1)
    elem1 = browser.find_element(By.NAME, "nickname")
    elem1.send_keys(names.get_full_name() + Keys.RETURN)
    print ("im in")
    time.sleep(1)
    browser.minimize_window()
    chouse_random(browser)
    browser.quit()

# Start test
N = int(input("num of bots: "))
thread_list = list()
for i in range(N):
    t = threading.Thread(name='Test {}'.format(i), target=boom_quiz)
    thread_list.append(t)
for i in range(N):
    thread_list[i].start()




