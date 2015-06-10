#! -*- encoding:utf-8 -*-
import os

string = raw_input("输入提交备注: ")
print os.popen('git add .').read()
print os.popen('git ci -m "%s"' % string).read()
print os.popen('git push origin master').read()
