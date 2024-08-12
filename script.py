from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import json


for i in range(0, 150):

    # firefox_profile = webdriver.FirefoxProfile()
    # firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

    # driver = webdriver.Firefox(firefox_profile=firefox_profile)

    driver = webdriver.Firefox()
    driver.get("https://challenge-jlpt.com/")


    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 
    driver.execute_script('document.getElementById("08_n5grammar.csv").checked = true ')
    # driver.execute_script('document.getElementById("09_n5vocabulary.csv").checked = true ')



    driver.execute_script('document.getElementById("toggle").checked = true ')
    driver.execute_script('document.getElementsByTagName("button")[1].click()')


    time.sleep(4)

    result = driver.execute_script("""return document.getElementsByClassName("grid")[0].getElementsByTagName('div')[4].innerHTML""")


    answers = []
    for j in range(4):
        answer = driver.execute_script(f"""return document.getElementsByClassName("grid")[0].getElementsByClassName("normal")[0].getElementsByTagName("button")[{j}].innerHTML""")
        answers.append(answer)

    id = driver.execute_script("""return document.getElementsByTagName("span")[6].textContent""")


    result = result.strip()
    id = id.strip()

    print(result, answers,id )




    string = ""


    string = "{"
    string += f"question: `{result}`,"

    string +="answers: {"

    [q1, q2, q3, q4] = answers

    string +='"'+ q1 + '": false,"' + q2 + '": false,"' + q3 + '": false,"' + q4 + '": false,'

    string +="},"
    string += "id:'"+id+"',"
        # ", {q2}: false, {q3}: false, {q4}: false]",)
    string +=f"explanation : `TODO: ADD EXPLANATION AND SET`"

    string +="},"

    # obj = json.loads(string)


    # print(str(obj))

    full_text = ""
    with open("questions.txt", "r") as f:
        full_text = f.read()

    f = open("questions.txt", "a")


    f.write(string)


    f.close()

    driver.close()
    driver.quit()
    print(f"saved {i}")
    if id in full_text:
        print("duplicate")
    else:
        print('NEW!!!')

    # N5V0041 - rb in answers
