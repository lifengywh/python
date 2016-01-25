import os
import sys

def get_w(word,path):
    files = os.listdir(path)
    for f in files:
        fff = path + "\\" + f
        if os.path.isdir(fff):
            print "this is dir:" + fff
            get_w(word,fff)
        else:
             ff = open(fff,'r').read()
             if word in ff:
                 print "words in: "+ fff

get_w(sys.argv[2],sys.argv[1])