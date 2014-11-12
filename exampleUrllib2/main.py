'''
Created on 2014-11-12

@author: raphael
'''
import sys
import urllib2
from sgmllib import SGMLParser

class FXList(SGMLParser):
    is_td=""
    is_Title=""
    data=[]
    def start_td(self, attrs):
        for k,v in attrs:
            if k == 'class' and v == 'titleLeft':
                self.is_Title = 1
            elif k == 'class' and v == 'link':
                self.is_Title = 0
        self.is_td=1
    def end_td(self):
        self.is_td=""
    def handle_data(self, text):  
        if self.is_Title:
                self.data.append(text)

if __name__ == '__main__':
    content = urllib2.urlopen('http://rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm').read()
    allFXList = FXList()
    allFXList.feed(content)
    index = 0
    for item in allFXList.data:    
        sys.stdout.write(item.decode('utf-8') + " ")
        if index%5 == 4:
            print ""
        index = index + 1
