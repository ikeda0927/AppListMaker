from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import openpyxl as px
import sys
import requests
from bs4 import BeautifulSoup
import re
import time

driver=None
chromedriverPath=None
query=None
waitTime=10
scrollTime=20
contentSum=245
contentMax=252
name=''
# contents=0

def Read(q):
    #https://play.google.com/store/search?q=duckduckgo&c=apps
    driver.get('https://play.google.com/store/search?q='+q+'&c=apps')
    # WebDriverWait(driver,waitTime).until(EC.presence_of_element_located((By.ID,'gbqfq')))
    # driver.find_element_by_id('gbqfq').send_keys(q)
    # driver.find_element_by_id('gbqfq').send_keys(Keys.ENTER)
    time.sleep(2)
    #下へスクロール
    # WebDriverWait(driver,waitTime).until(EC.presence_of_element_located((By.CLASS_NAME,'Vpfmgd')))
    WebDriverWait(driver,waitTime).until(EC.presence_of_element_located((By.CLASS_NAME,'poRVub')))
    # driver.find_element_by_class_name('WpDbMd').send_keys(Keys.END)
    startTime=time.time()
    contents=0
    while time.time()-startTime<scrollTime and contents<contentSum:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # contents=len(driver.find_elements_by_class_name('Vpfmgd'))
        contents=len(driver.find_elements_by_class_name('poRVub'))
        # print(contents)
        if contentMax<contents:
            return None
    # return driver.find_elements_by_class_name('Vpfmgd')
    return driver.find_elements_by_class_name('poRVub')

def GetData(url):
    data=requests.get(url+'&hl=ja')
    soup=BeautifulSoup(data.text,"html.parser")
    spans=soup.find_all('span', class_="htlgb")
    if soup.find('title',id="main-title") ==None:
        return None
    tuple=(soup.find('title',id="main-title").contents[0],soup.find('a', class_="hrTbp R8zArc").contents[0],spans[7].contents[0],spans[5].contents[0],spans[1].contents[0].replace('年','/').replace('月','/').replace('日',''))
    return tuple

def WriteToExcel(appList):
    exelFile='./android_applist.xlsx'
    book = px.load_workbook(exelFile)
    sheet= book['調査対象リスト']
    columnNum=1
    rowAlp=65
    counter=0
    startIndex=0
    # ## DEBUG
    # max=15
    # limitCounter=0
    # ## DEBUG
    for i in appList:
        link=str(i.get_attribute('href'))
        while True:
            # print(link)
            # print(str(sheet[chr(rowAlp+1)+str(columnNum+counter)].value))
            if link==str(sheet[chr(rowAlp+1)+str(columnNum+counter)].value):
                # print(link)
                # print(str(sheet[chr(rowAlp+1)+str(columnNum+counter)].value))
                break
            elif sheet[chr(rowAlp+1)+str(columnNum+counter)].value==None:
                print(link)
                tuple=GetData(link)
                if tuple ==None:
                    print('######### PAGE NOT FOUND -> '+link+'#########')
                    break;
                sheet[chr(rowAlp+0)+str(columnNum+counter)].value=tuple[0]
                sheet[chr(rowAlp+1)+str(columnNum+counter)].value=link
                sheet[chr(rowAlp+2)+str(columnNum+counter)].value=tuple[1]
                sheet[chr(rowAlp+3)+str(columnNum+counter)].value=tuple[2]
                sheet[chr(rowAlp+4)+str(columnNum+counter)].value=tuple[3]
                sheet[chr(rowAlp+5)+str(columnNum+counter)].value=tuple[4]
                sheet[chr(rowAlp+6)+str(columnNum+counter)].value=query
                sheet[chr(rowAlp+8)+str(columnNum+counter)].value=name
                book.save(exelFile)
                if startIndex==0:
                    startIndex=counter
                break
            counter+=1
        # ## Debug
        # limitCounter+=1
        # if limitCounter>max:
        #     break
        # ## DEbug
    # book.save(exelFile)
    if startIndex!=0:
        print('追加されたindexは '+str(startIndex)+' から '+str(counter)+'です。')

def ShowHelp():
    print('-c [str]\n\tchromedriverへのパスを指定（必須）\n-q [str]\n\t検索クエリを指定\n\t検索が終了したら、結果をExcelに出力するか聞かれるので、検索クエリを確認してyかnを入力する。\n\tyを入力した場合は名前を聞かれるので名前を入力するとexcelに出力される。')

if __name__=='__main__':
    if len(sys.argv)>=2:
        for i in range(1,len(sys.argv),2):
            if sys.argv[i]=='-c':
                if len(sys.argv)>=i+2:
                    temp=sys.argv[i+1]
                    chromedriverPath=temp
            elif sys.argv[i]=='-q':
                if len(sys.argv)>=i+2:
                    query=sys.argv[i+1]
        print('len '+str(len(sys.argv)))
    else:
        ShowHelp()
    if query != None and chromedriverPath != None:
        driver = webdriver.Chrome(chromedriverPath)
        appList=Read(query)
        if appList != None:
            print('Query is ['+query+']')
            print('Export to Excel? y/n')
            ans=input()
            if ans=='y':
                print('Enter your Name')
                name=input()
                WriteToExcel(appList)
            elif ans=='n':
                print('Not exported')
            else:
                print('Enter \'y\' or \'n\'')
        #     for i in appList:
        #         print(str(i.get_attribute('href')))
        # print()
    else:
        ShowHelp()
