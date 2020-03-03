from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import csv
st=time.time()
f=open("2130.txt", "r")
lines=f.read()
f.close()
h=open("chess_player_data.csv",'a',newline='')
browser = webdriver.Firefox(executable_path='/home/sanjay/Desktop/geckodriver')
browser.get("https://lichess.org/login")
browser.maximize_window()
username = browser.find_element_by_id('form3-username')
username.click()
username.send_keys('ToxicTerror')
passwd = browser.find_element_by_id('form3-password')
passwd.click()
passwd.send_keys('SAnj*$67')
browser.find_element_by_css_selector(".submit.button").click()
time.sleep(2)
action = ActionChains(browser)
act_1 = browser.find_element_by_xpath("//a[@href='/analysis']")
action.move_to_element(act_1).perform()
#time.sleep(2)
act_2 = browser.find_element_by_xpath("//a[@href='/paste']")
act_2.click()
#time.sleep(2)
paste_pgn = browser.find_element_by_id('form3-pgn')
paste_pgn.click()
paste_pgn.clear()
paste_pgn.send_keys(lines)
browser.find_element_by_css_selector(".submit.button.text").click()
browser.find_element_by_class_name("switch").click()
count=0
for gn in range(2131,2303):
    print(gn)
    f=open(str(gn)+".txt", "r")
    lines=f.read()
    f.close()
    f=open(str(gn)+".txt", "r")
    white=""
    black=""
    moves=[]
    for line in f:
        ct=8
        if len(line)>10 and (line[1]=='W' and line[2]=='h' and line[3]=='i' and line[4]=='t' and line[5]=='e' and line[6]==' '):
            while line[ct]!='"':
                white+=line[ct]
                ct+=1
        ct=8
        if len(line)>10 and (line[1]=='B' and line[2]=='l' and line[3]=='a' and line[4]=='c' and line[5]=='k' and line[6]==' '):
            while line[ct]!='"':
                black+=line[ct]
                ct+=1
        if "[" not in line:
            a = line.split()
            for i in range(len(a)):
                dot=0
                for j in range(len(a[i])):
                    if a[i][j]=='.':
                        val=""
                        for k in range(j+1,len(a[i])):
                            val+=a[i][k]
                        moves.append(val)
                        dot=1
                if (dot==0):
                    moves.append(a[i])
                
    f.close()   
    #browser.get(browser.current_url)
    if (count!=0):
        enter_not = browser.find_element_by_xpath("//textarea[contains(@class, 'copyable')]")
        enter_not.click()
        enter_not.send_keys(lines)
        #time.sleep(3)
        #impt = browser.find_element_by_css_selector(".button.button-thin.action.text")
        #impt = browser.find_element_by_xpath("//button[@data-icon='G']")
        impt = browser.find_element_by_xpath("//button[contains(@class, 'button-thin')]")
        impt.click()
        time.sleep(2)
        browser.find_element_by_xpath("//button[@data-act='first']").click()
    evaluation=[]
    for i in range (1, len(moves)):
        vals = 1
        while (vals==1):
            a = browser.find_element_by_css_selector(".ceval.enabled").get_attribute("innerHTML")
            ct = 0
            for i in range(len(a)):

                if a[i] == 'p' and a[i + 1] == 'e' and a[i + 2] == 'a' and a[i + 3] == 'r' and a[i + 4] == 'l':
                    ans = a[i + 6]
                    ct = i + 6
                    while (a[ct + 1] != '<'):
                        ans = ans + a[ct + 1]
                        ct += 1
                    break
            if (ans!='<i class="ddloader">'):
                #f=open
                evaluation.append(ans)
                vals=0
            else:
                vals=1
        browser.find_element_by_xpath("//button[@data-act='next']").click()
    for i in range(len(evaluation)):
        row = [white, black, moves[i], evaluation[i],gn]
        wr = csv.writer(h, quoting=csv.QUOTE_ALL)
        wr.writerow(row)
    #browser.execute_script("window.history.go(-1)")
    count+=1
    browser.find_element_by_xpath("//a[@href='/analysis']").click()
    #browser.find_element_by_class_name("site-title").click()
browser.close()
h.close()
b=time.time()
print("Time taken: " + str(b-st))













    #f.write()
#browser.find_element_by_css_selector(".cmn-toggle.cmn-toggle--subtle").click()
#browser.find_element_by_id('analyse-toggle-ceval').click()
#sb.click()

#toggle = browser.find_element_by_id("analyse-toggle-ceval")
#toggle.click()
#time.sleep(2)
#selenium.click("xpath=//a[contains(@href,'/paste') and @role='group']")
#browser.find_element_by_class_name("hover").click()
#browser.find_element_by_xpath("//*[text()[contains(.,'Tools')]]")
#browser.find_element_by_xpath("//a[contains(@href,'/paste') and @role='group']")
#browser.find_element_by_xpath("//a[@href='/analysis']").click()
#browser.get("https://lichess.org/paste")
#time.sleep(2)
#click_submit = browser.find_element_by_class_name("form-actions single")
#click_submit.click()
#browser.submit()
#browser.find_element_by_css_selector(".button_main").click()
#sb = browser.find_element_by_xpath('//div[@class="submit-buttons"]/button[@class="submit"]')
#sb = browser.find_element_by_xpath("//input[@type='submit']")
#browser.find_element(type = "submit").click()
#f=open(r"C:\Users\Sanjay\Desktop\and.txt", "a")
#browser.find_element_by_xpath("//button[@data-act='menu']").click()
#browser.find_element_by_id("abset-infinite").click()
#browser.find_element_by_xpath("//button[@data-act='menu']").click()
#browser.find_element_by_css_selector(".switch").click()
######clear
