## 無理やりgoogle play store上のアプリのリストを取得する方法

おそらく期待しているのとはちょっと違うのですが調べても出てこない上にこれしかいい案が浮かばなかったのでご了承ください。  

- [全体像](https://github.com/ikeda0927/AppListMaker#全体像)  
- [方法](https://github.com/ikeda0927/AppListMaker#方法)  
- [250件までしか検索結果に表示されない件](https://github.com/ikeda0927/AppListMaker#250件までしか検索結果に表示されない件)  
- [appListIntegrator.pyの使い方](https://github.com/ikeda0927/AppListMaker#appListIntegrator.pyの使い方)  
- [Excelに反映](https://github.com/ikeda0927/AppListMaker#Excelに反映)  
- [自動でアプリをインストールする](https://github.com/ikeda0927/AppListMaker#自動でアプリをインストールする)  


### 全体像
---  
手動でgoogle play storeを開き、取得したいアプリのジャンルなどを検索欄に入力し、開発者モードに入り、検索して出てきたアプリの一覧をコンソールでjavascriptを実行し、取得する...感じです。  
※追記(2019/10/11)取得したリストをExelに反映させる

※追記 この方法では検索結果の250件しか得られませんでした...  
※簡単な対応策を追記  
※追記(2019/10/15)exelEditor.pyは __Windows非対応__ なのでOSXかLinuxで実行してください。また、別途pip3(pip)で必要なパッケージがあるので、以下のコマンドでインストールしてください。
~~~
pip3 install openpyxl beautifulsoup4 requests
~~~

### 方法  
---
まず、  
https://play.google.com/store?hl=ja  
を開く  

探したいアプリのジャンルで検索にかけ、一旦そのページを __一番下までスクロール__ する。

次に、表示されているアプリのうちのどれか一つのタイトルを右クリックし、開発者画面（Chromeなら検証ってところ）に移る。  

するとタイトルやリンクなどが含まれているタグがわかるのでそのタグのクラス名を控えておく。

控えたクラス名（以下の例ではb8cIId ReQCgd Q9MA7b）を使ってオブジェクトを取得する。

~~~
var apps= document.getElementsByClassName("b8cIId ReQCgd Q9MA7b")
~~~

上の文を実行するとappsにタイトルやリンクなどが含まれるオブジェクトが格納される。  

この時、
~~~
apps.length
~~~
を入力してappsの要素数が250より多くないか確認する。  

250より多い場合は更新してやり直す。  
※250より多い場合は余計な情報が含まれている可能性があるため

次はappsに格納されたオブジェクトからタイトルやリンクを取得する。

最初にstrを初期化

~~~
str=""
~~~

そしてそのstrにfor文でリンクとタイトル（アプリ名）を入れていく。

~~~
for(var i=0;i<apps.length;i++){
    str=str+i+' '+apps[i].firstElementChild.getAttribute("href")+"\n"+apps[i].firstElementChild.firstElementChild.getAttribute("title")+"\n\n";
}
~~~

これで検索結果に表示された全てのアプリのタイトルとリンクは取得できました。

あとは、

~~~
copy(str)
~~~

でクリップボードにコピーし、適当なテキストエディタに貼り付けて保存すれば完成です。

大事なのは検索結果が出た時に一旦ページを下までスクロールすることです。
こうしないと全てのデータを取得することができません。

### 250件までしか検索結果に表示されない件
---
以上の方法では250件しかアプリのデータが得られないので対応策を考えました。

#### 気になったこと
+ google play storeの検索結果のページには一度に250件までしか表示されない。
+ ページを更新するとページの上位のアプリはそのままだが下の方のアプリは順番が後退したり、新しいアプリが出てくる。

#### 上から考えられる解決策
ページを更新してアプリのリストを取得し、新しく表示された分をリストに追加するのを何回か行う。  

ということで、増加分を新たに追加するpython（3系）のスクリプト appListIntegrator.pyを作成しました。  

### appListIntegrator.pyの使い方
---
まずは上記の方法でアプリのリストを作成します。  

ここでは、最初に作成したリストをappList1.txtとし、２回目に作成したリストをappList2.txtとします。  

ここでappList1.txtにappList2.txtでの増加分をappList1.txtに加えたいので、以下のようにスクリプトを実行します。  

~~~
python3 appListIntegrator.py appList1.txt appList2.txt
~~~

するとappList1.txtの方にappList2.txtで増加した分が追加され、標準出力には追加した数が表示されます。  

これを何回か繰り返して、何回やっても増加分が0になるようであればアプリのリストの精度が高くなったと言えるでしょう。  

### Excelに反映
上記の方法で取得したリストをExcelに反映させます。  

まず、前提として、  

| A | B | C | D | E | F | G | H | I | J | K | L |  
| --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |  
| アプリ名 | URL | 製作者 | バージョン | インストール数 | 評価数 | 最終更新日 | --- | 検閲者 | --- | --- | --- |  

こんな感じの表になっているとします。  

上の形式のExcelファイルと上で作成したappList1.txt(名前は変更可)のあるディレクトリ上で  

~~~
python3 exelEditor.py appList1.txt 氏名(省略可)
~~~  

を実行するとapplist1.txt上にまとめられたアプリのアプリ名、URL、製作者、バージョン、インストール数、最終更新日、検閲者(氏名を省略した場合は空欄)  

みたいな感じで書き込めます。  

なお、重複などは無視されます。  

競合はおこるかもしれません

### 自動でアプリをインストールする

appInstallHelper.pyを使えば、上で作成したエクセル（Bの列にURLさえあれば問題ない）を元に自動でアプリをインストールできます。  

※動作を確認したのはmacOS CatalinaとWindos10です。  
※エラーが発生した場合は教えてください。  
※Windowsで実行してutf-8何たらかんたらのエラーが出た場合はShowHelp()内のprintfの行をNoneに置き換えてください。

##### 準備

まずは必要なものを用意します。
~~~
pip3 install selenium
~~~
でブラウザをPythonで操作するためにseleniumをインストールします。

次に、ChromeのWebDriverをダウンロードします。  

Chromeの　設定 > Chromeについて　から現在使用しているChromeのバージョンを確認します。  

https://chromedriver.chromium.org/downloads  

から、上で確認したバージョンにあったwebdriverをダウンロードしてください。  

ダウンロードしたものを展開して、出てきたchromedriverをappInstallHelper.pyと同じディレクトリにおきます。  

##### 実行

appInstallHelper.pyを動かすためには5つの値を指定する必要があります。  

一つ目はメールアドレス  
二つ目はパスワード  
三つ目はandroid_applist.xlsxでのstart Index（始まりの値）  
四つ目はandroid_applist.xlsxでのend Index（終わりの値）  
五つ目はchromedrivverへのパス

メールアドレスの指定は -m \<mailaddress\>  
パスワードの指定は    -p \<password\>  
start Indexの指定は　-s \<start Index\>  
end Indexの指定は　　-e \<end Index\>  
chromedriverへのパス指定は -c \<chromedriverへのパス\>

のように指定します。  
または、メールアドレスとパスワードをファイルに記述(1行目にメールアドレス、2行目にパスワード)してそのファイルへのパスを  
 -f \<ファイルへのパス\>  
 として渡すことも可能です。  

 例1  
~~~
python3 appInstallHelper.py -m testmail@gmail.com -p password -s 100 -e 110 -c ./chromedriver
~~~

~~~
python3 appInstallHelper.py -f address.txt -s 100 -e 110 -c ./chromedriver
~~~  


問題がなければ、ブラウザが開いて、自動的にインストールが進みます。
