import re
import sys

pattern1   = "[0-9]+\s/store/"
repattern1 = re.compile(pattern1)
pattern2   = "[0-9]+\s"
repattern2 = re.compile(pattern2)

link=None
apps = list()

class App:
    link=None
    name=None
    def __init__(self,link,name):
        self.link=link
        self.name=name

    def getName(self):
        return self.name

    def getLink(self):
        return self.link

    # def process(self):
    #     print(self.name+':'+self.link)

def lineFunc(line):
    global link
    if str(line)=='\n':
        None
    elif repattern1.match(line):
        link=re.sub(repattern2,'',str(line).replace('\n',''))
    else:
        apps.append(App(link,str(line).replace('\n','')))

def compareName(line):
    global link
    if str(line)=='\n':
        None
    elif repattern1.match(line):
        link=re.sub(repattern2,'',str(line).replace('\n',''))
    else:
        for app in apps:
            if app.getName()==str(line).replace('\n',''):
                return None
        apps.append(App(link,str(line).replace('\n','')))

if __name__ == '__main__':
    if len(sys.argv)>=3:
        with open(sys.argv[1],'r')as f1:
            lines=f1.readlines()
            for line in lines:
                lineFunc(line)
        with open(sys.argv[2],'r')as f2:
            lines=f2.readlines()
            for line in lines:
                compareName(line)
        with open(sys.argv[1],'w')as f3:
            num =0
            for app in apps:
                f3.write(str(num)+' '+app.getLink()+'\n'+app.getName()+'\n\n')
                num+=1
        # num=0
        # for app in apps:
        #     print(num)
        #     num+=1
        #     app.process()
