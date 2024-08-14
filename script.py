from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import json


driver = webdriver.Firefox()
driver.get("https://challenge-jlpt.com/")

for i in range(0, 300):

    # firefox_profile = webdriver.FirefoxProfile()
    # firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

    # driver = webdriver.Firefox(firefox_profile=firefox_profile)



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

    correct_index = -1
    for j in range(4):
        driver.execute_script(f"""document.getElementsByClassName("grid")[0].getElementsByClassName("normal")[0].getElementsByTagName("button")[{j}].click()""")
        time.sleep(3)
        spans = driver.execute_script(f"""return document.getElementsByTagName("span")""")
        for span in spans:
            if "Correct!" in span.get_attribute("innerHTML"):
                print("CORRECT")
                correct_index = j
                break
            elif "Wrong!" in span.get_attribute("innerHTML"):
                print("INCORRECT")
            print('looping again')
        else:
            continue
        break

    result = result.strip()
    id = id.strip()

    print(result, answers,id )

    string = ""


    string = "{"
    string += f"question: `{result}`,"

    string +="answers: {"

    [q1, q2, q3, q4] = answers

    string +='"'+ q1 + f'": {str(correct_index==0).lower()},"' + q2 + f'": {str(correct_index==1).lower()},"' + q3 + f'": {str(correct_index==2).lower()},"' + q4 + f'": {str(correct_index==3).lower()},'

    string +="},"
    string += "id:'"+id+"',"
    string += "confirmed:true, "
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

   



    print(f"saved {i}")
    if id in full_text:
        print("duplicate")
    else:
        print('NEW!!!')

    # N5V0041 - rb in answers

    # change site insteas of closing
    driver.execute_script("""window.location.replace("https://challenge-jlpt.com/")""")
    time.sleep(4)


    
    # driver.close()
    # driver.quit()
