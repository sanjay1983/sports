'''import requests 
from bs4 import BeautifulSoup 
URL = "https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2019/matches"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') 

table = soup.findAll('h1', attrs = {'class':'content-heading'}) 

for row in table:
    print(row.text)'''

'''
from selenium import webdriver
import time

g=open("ipl_seasons.txt","r")
for line in g:
    browser = webdriver.Chrome('/home/sanjay/Downloads/chromedriver_linux64/chromedriver')
    url=line
    print(line)
    browser.get(url)
    links = browser.find_elements_by_class_name('text-hvr-underline')
    f=open("url_links.txt","a")
    f.write("\n")
    for link in links:
        f.write(link.get_attribute("href"))
        f.write("\n")
    f.close()
    browser.close()
g.close()
'''


## For no balls, wides, leg byes, byes, count to team score
## Extract team names
## For no balls + runs , count to player score



import requests 
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
f=open("url_links.txt","r")
g=open("ball_data.csv",'w',newline='')
ct=0
for line in f:
    change=0
    ct+=1
    URL = line
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('span', attrs = {'class':'cb-col cb-col-8 text-bold'})
    table2 = soup.findAll('p', attrs = {'class':'cb-col cb-col-90 cb-com-ln'})
    team1 = soup.findAll('div', attrs = {'class':'cb-col cb-col-100 cb-min-tm cb-text-gray'})
    team2 = soup.findAll('div', attrs = {'class':'cb-col cb-col-100 cb-min-tm'})
    year = soup.findAll('span', attrs = {'class':'text-hvr-underline text-gray'})
    #print(team1[0].text)
    #print(team2[0].text)
    #print(year[0].text)
    
    player1_team = ""
    player2_team = ""
    for i in range(len(team1[0].text)):
        if team1[0].text[i]!=" ":
            player1_team += team1[0].text[i]
        if team1[0].text[i]==" ":
            break
    for i in range(len(team2[0].text)):
        if team2[0].text[i]!=" ":
            player2_team += team2[0].text[i]
        if team2[0].text[i]==" ":
            break
    len_year = len(year[0].text)
    yr = year[0].text[len_year-4]+year[0].text[len_year-3]+year[0].text[len_year-2]+year[0].text[len_year-1]
    #print(batting_first)
    #print(bowling_first)
    #print(yr)
    #print(type(teams),len(teams))
    #print(type(year),len(year))
    for i in range(len(table)):
        nb=0
        wide=0
        byes="0"
        leg_byes="0"
        ball_no = (float)(table[i].text)
        ball_desc = table2[i].text.split()
        bowler=""
        batsman=""
        batsman_final=""
        result=""
        position=0
        position2=0
        position3=0
        
        if (ball_no==0.1):
            change=1
        if (change==1 and ball_no==5.6):
            temp = player1_team
            player1_team = player2_team
            player2_team = temp 
        for j in range(len(ball_desc)):
            if ball_desc[j]!="to":
                if position==0:
                    bowler=bowler+ball_desc[j]
                    position+=1
                else:
                    bowler=bowler+" "+ball_desc[j]
                    position+=1
            if ball_desc[j]=="to":
                position+=1
                break
        for k in range(position,len(ball_desc)):
            if ',' not in ball_desc[k]:
                if position2==0:
                    batsman=batsman+ball_desc[k]
                    position2+=1
                else:
                    batsman=batsman+" "+ball_desc[k]
                    position2+=1
            if ',' in ball_desc[k]:
                batsman=batsman+" "+ball_desc[k]
                position2+=1
                break
        position3=position+position2
        if ball_desc[position3]=='no':
            if ball_desc[position3+1]=='run,' or ball_desc[position3+1]=='run':
                result = "0"
            else:
                result = ball_desc[position3+2]
                nb=1
        elif ball_desc[position3]=="wide,":
            result = "0"
            wide=1
        elif ((len(ball_desc)-1) > (position3+1)) and ball_desc[position3+1]=="wides,":
            result="0"
            wide = (int)(position3)
        #result=ball_desc[position3]
        elif ball_desc[position3]=='leg':
            result="0"
            if ((len(ball_desc)-1) > (position3+2)):
                leg_byes = ball_desc[position3+2]
        elif ball_desc[position3]=='byes,':
            result="0"
            byes = ball_desc[position3+1]
        else:
            result=ball_desc[position3]
        sz = len(batsman)
        if batsman[0]==" ":
            for h in range(1,sz-1):
                batsman_final+=batsman[h]
        if batsman[0]!=" ":
            for h in range(0,sz-1):
                batsman_final+=batsman[h]
        if (ball_no<=5.6):
            
            #g=1
            #print(ball_no)
            ls=[str(ball_no), bowler, batsman_final, result, player1_team, player2_team, yr, str(nb), str(wide), byes, leg_byes]
            #wr = csv.writer(g, quoting=csv.QUOTE_ALL)
            #wr.writerow(ls)
            if "run out" in table2[i].text and "Run Out!!" in table2[i].text:
                print(player1_team, player2_team, yr, str(ball_no))
                print("\n")
               
            #print(str(ball_no) + " " + bowler + " " + batsman + " " + result + " " + player1_team + " " + player2_team + " " + yr + " " + str(nb) + " " + str(wide) + " " + byes + " " + leg_byes)
          
            #print("\n")
    #print(ct)
g.close()
f.close()

