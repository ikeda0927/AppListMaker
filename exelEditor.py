import openpyxl as px
import requests
from bs4 import BeautifulSoup
import re
import sys

pattern1   = "[0-9]+\s/store/"
repattern1 = re.compile(pattern1)
pattern2   = "[0-9]+\s"
repattern2 = re.compile(pattern2)

urlSchemeDomain='https://play.google.com'

def GetData(url):
    data=requests.get(urlSchemeDomain+url+'&hl=ja')
    soup=BeautifulSoup(data.text,"html.parser")
    spans=soup.find_all('span', class_="htlgb")
    if soup.find('title',id="main-title") ==None:
        return None
    tuple=(soup.find('title',id="main-title").contents[0],soup.find('a', class_="hrTbp R8zArc").contents[0],spans[7].contents[0],spans[5].contents[0],spans[1].contents[0].replace('年','/').replace('月','/').replace('日','/'))
    return tuple

if __name__ == '__main__':
    if len(sys.argv)>=2:
        sourceFileName=sys.argv[1]
        name=''
        if len(sys.argv)>=3:
            name=sys.argv[2]
        exelFile='./android_applist.xlsx'
        book = px.load_workbook(exelFile)
        sheet= book.active
        columnNum=1
        rowAlp=65
        with open(sourceFileName,'r')as f:
            lines=f.readlines()
            for line in lines:
                if str(line)=='\n':
                    None
                elif repattern1.match(line):
                    link=re.sub(repattern2,'',str(line).replace('\n',''))
                    counter=0
                    while True:
                        if link==str(sheet[chr(rowAlp+1)+str(columnNum+counter)].value).replace(urlSchemeDomain,''):
                            break
                        elif sheet[chr(rowAlp+1)+str(columnNum+counter)].value==None:
                            print(urlSchemeDomain+link)
                            tuple=GetData(link)
                            if tuple ==None:
                                print('######### PAGE NOT FOUND -> '+urlSchemeDomain+link+'#########')
                                break;
                            sheet[chr(rowAlp+0)+str(columnNum+counter)].value=tuple[0]
                            sheet[chr(rowAlp+1)+str(columnNum+counter)].value=urlSchemeDomain+link
                            sheet[chr(rowAlp+2)+str(columnNum+counter)].value=tuple[1]
                            sheet[chr(rowAlp+3)+str(columnNum+counter)].value=tuple[2]
                            sheet[chr(rowAlp+4)+str(columnNum+counter)].value=tuple[3]
                            sheet[chr(rowAlp+6)+str(columnNum+counter)].value=tuple[4]
                            sheet[chr(rowAlp+8)+str(columnNum+counter)].value=name
                            book.save(exelFile)
                            break
                        counter+=1
        book.save(exelFile)
