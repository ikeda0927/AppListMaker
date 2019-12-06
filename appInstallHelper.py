from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import openpyxl as px
import sys
import time

# chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument('user-data-dir='+'')
# driver = webdriver.Chrome('./chromedriver',options=chromeOptions)
# driver = webdriver.Chrome('./chromedriver')
# driver.get('https://www.google.com')
# urlList=['https://play.google.com/store/apps/details?id=com.pekobbrowser.unblocksites','https://play.google.com/store/apps/details?id=arun.com.chromer','https://play.google.com/store/apps/details?id=fast.secure.light.browser']
driver=None
chromedriverPath=None
mailAddress=None
password=None
addressFilePath=None
start=None
end=None
deviceName='Google Pixel 3a'




def LoginGoogle(mailAddress,password):
    #open google top page
    # driver.get('https://www.google.com')
    # driver.get('https://accounts.google.com/ServiceLogin?hl=ja&passive=true&continue=https://www.google.com/')
    #click login button
    driver.find_element_by_id('gb_70').click()
    try:
        #enter mail address
        driver.find_element_by_id('identifierId').send_keys(mailAddress)
        #click next button
        driver.find_element_by_id('identifierNext').click()
        #wait for the password entry is appear
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME,'password')))
        time.sleep(1)
        #enter password
        driver.find_element_by_name('password').send_keys(password)
        #click next button
        driver.find_element_by_id('passwordNext').click()
    except NoSuchElementException:
        #enter mail address
        driver.find_element_by_id('Email').send_keys(mailAddress)
        #click next button
        driver.find_element_by_id('next').click()
        #wait for the password entry is appear
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME,'password')))
        time.sleep(1)
        #enter password
        driver.find_element_by_id('Passwd').send_keys(password)
        #click next button
        driver.find_element_by_id('signIn').click()
        time.sleep(1)
        # WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME,'q')))

def ReadAndExcute(mailAddress,password,start,end):
    # driver.execute_script('window.open()')
    # driver.switch_to.window(driver.window_handles[1])
    # WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME,'q')))
    # # time.sleep(1)
    # driver.find_element_by_name('q').send_keys('https://play.google.com/store?hl=ja')
    # driver.find_element_by_name('q').send_keys(Keys.ENTER)
    # driver.AddArgument('user-data-dir='+'/Users/ikedakouhei/Library/Application Support/Google/Chrome/Profile 2')
    driver.get('https://play.google.com/store/apps/details?id=com.duckduckgo.mobile.android')
    LoginGoogle(mailAddress,password)
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[2]/div/div[2]/div/c-wiz/c-wiz/button')))
    urlList=ReadExcel(start,end)
    for url in urlList:
        Execute(url)
    # driver.get('https://play.google.com/store/apps/details?id=com.pekobbrowser.unblocksites')

def Execute(url):
    driver.get(url)
    try:
        # WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[2]/div/div[2]/div/c-wiz/c-wiz/button')))
        # driver.find_element_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[2]/div/div[2]/div/c-wiz/c-wiz/button').click()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[2]/div/div[2]/div/c-wiz/c-wiz/div/span/button')))
        driver.find_element_by_xpath(
            '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[2]/div/div[2]/div/c-wiz/c-wiz/div/span/button').click()
        #/html/body/div/div/div[2]/div[3]/span/button
        # WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div[2]/div[3]/span/button')))
        # driver.find_element_by_xpath('/html/body/div/div/div[2]/div[3]/span/button').click()
        # for iframe in driver.find_elements_by_tag_name('iframe'):
        #     print(iframe.get_attribute('src'))
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/iframe')))
        driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[4]/iframe'))
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div > div > div.g3VIld.LhXUod.drrice.Up8vH.J9Nfi.iWO5td > div.XfpsVe.J9fJmf > span > button')))
        driver.find_element_by_css_selector('body > div > div > div.g3VIld.LhXUod.drrice.Up8vH.J9Nfi.iWO5td > div.XfpsVe.J9fJmf > span > button').click()
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME,'password')))
        driver.find_element_by_name('password').send_keys('bq5uf3zp0')
        driver.find_element_by_id('passwordNext').click()
        # sleep(10)/html/body/div[5]/iframe //*[@id="I0_1575297251288"]
        # driver.switch_to().parent_frame()
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/iframe')))
        driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[5]/iframe'))
        # WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div[2]/div[3]/button')))
        # driver.find_element_by_xpath('/html/body/div/div/div[2]/div[3]/button').click()
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div[3]/div/div/button')))
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div/button').click()

    except TimeoutException:
        print('Can\'t Install')

def ReadExcel(start,end):
    excelFile='./android_applist.xlsx'
    book = px.load_workbook(excelFile)
    sheet= book.active
    # columnNum=1
    rowAlp=65
    urlList=list()
    for i in range(end-start+1):
        print(str(start+i)+' : '+sheet[chr(rowAlp+1)+str(start+i)].value)
        urlList.append(sheet[chr(rowAlp+1)+str(start+i)].value)
    return urlList

def OpenPlayStore():
    driver.get('https://play.google.com/store/apps/details?id=com.duckduckgo.mobile.android')
    # WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME,'LkLjZd ScJHi HPiPcc IfEcue  ')))
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[2]/div/div[2]/div/c-wiz/c-wiz/div/span/button')))
    # driver.find_element_by_class_name('LkLjZd ScJHi HPiPcc IfEcue  ').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[2]/div/div[2]/div/c-wiz/c-wiz/div/span/button').click()

def ShowHelp():
    print('-m [str]\n\tメールアドレス指定(必須だが、-fを指定しているなら省略可)\n-p [str]\n\tパスワード指定(必須だが、-fを指定しているなら省略可)\n-f [str]\n\tメールアドレスとパスワードをファイルから指定(-mと-pを指定しているなら省略可)\n\tファイルの形式は1行目にメールアドレス、2行目にパスワード\n-s [int]\n\tandroid_appListにおけるスタートindex指定（必須）\n-e [int]\n\tandroid_appListにおけるエンドindex指定（必須）\n-c [str]\n\tchromedriverへのパスを指定（必須）')

if __name__=='__main__':
    if len(sys.argv)>=2:
        for i in range(1,len(sys.argv),2):
            if sys.argv[i]=='-m':
                if len(sys.argv)>=i+2:
                    temp=sys.argv[i+1]
                    mailAddress=temp
            elif sys.argv[i]=='-p':
                if len(sys.argv)>=i+2:
                    temp=sys.argv[i+1]
                    password=temp
            elif sys.argv[i]=='-f':
                if len(sys.argv)>=i+2:
                    temp=sys.argv[i+1]
                    addressFilePath=temp
                    with open(addressFilePath,'r') as f:
                        mailAddress=f.readline()
                        mailAddress=mailAddress.replace('\n','')
                        password=f.readline()
                        password=password.replace('\n','')
            elif sys.argv[i]=='-s':
                if len(sys.argv)>=i+2:
                    temp=sys.argv[i+1]
                    start=int(temp)
            elif sys.argv[i]=='-e':
                if len(sys.argv)>=i+2:
                    temp=sys.argv[i+1]
                    end=int(temp)
            elif sys.argv[i]=='-c':
                if len(sys.argv)>=i+2:
                    temp=sys.argv[i+1]
                    chromedriverPath=temp
        print('len '+str(len(sys.argv)))
    else:
        ShowHelp()
    if mailAddress != None and password != None and start != None and end != None and chromedriverPath != None:
        # print(mailAddress)
        # print(password)
        # print(str(start))
        # print(str(end))
        driver = webdriver.Chrome(chromedriverPath)
        ReadAndExcute(mailAddress,password,start,end)
    else:
        ShowHelp()
    # LoginGoogle()
    # ReadAndExcute()
    # list=ReadExcel(100,110)
    # print('')
    # for l in list:
    #     print(l)
    # OpenPlayStore()
    # None
