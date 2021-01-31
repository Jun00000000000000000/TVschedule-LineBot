import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import MySQLdb

target_url = 'https://tv.yahoo.co.jp/search/?q=&g=&Submit.x=0&Submit.y=0'

driver = webdriver.Chrome('/Users/fujishitakana/Downloads/chromedriver')
driver.get(target_url)

search = driver.find_element_by_css_selector('input.generic_inputText')
search.send_keys("松本人志")

search.submit()

time.sleep(5)

html = driver.page_source.encode('utf-8')
#r = requests.get(target_url)
#soup = BeautifulSoup(r.text, "html.parser")
soup = BeautifulSoup(html,"lxml")

results = soup.find_all("p", class_="pb5p")
#elems = soup.select('a[class^=title]')
#elems = soup.select('a[href^=/program/]')

#links=[url.get('href') for url in soup.find_all('a')]
#print(elems)
for result in results:
    print(result.getText())

#driver.close()
#driver.quit()

cnct = MySQLdb.connect(  #Win,mac用
    host = "localhost",  #ホスト名
    user = "root",       #MySQLユーザ名
    password = "root",       #MySQLユーザパスワード
    db = "TV",         #データベース名
    charset = "utf8"     #文字コード
    )
TABLE = "talent"           #テーブル名

cur = cnct.cursor()

# ここでデータベースの操作を行う
cur.execute("SELECT * FROM " + TABLE + ";") #SQLのコマンド
results = cur.fetchall()                    #結果をresultに格納
print("全て表示")
print(results)
print("\n")

print("1行ずつ表示")
for r in results:
    print(r)


#---------
# 切断
#---------

cur.close()
cnct.close()
