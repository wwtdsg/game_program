#! -*- encoding:utf-8 -*-
import os
import re
import sys

print '当前工作区情况：'
st = os.popen('git st').read()
if re.search('fatal', st):
    print st
    sys.exit()
string = raw_input("输入提交备注: ")
print os.popen('git add .').read()
print os.popen('git ci -m "%s"' % string).read()
print os.popen('git push origin master').read()
