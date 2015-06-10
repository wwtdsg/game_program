#! -*- encoding:utf-8 -*-
import os
import sys
import commands

print '当前工作区情况：'
status, output = commands.getstatusoutput('git st')
print '----' + output
if status:
    print status
    sys.exit()
else:
    string = raw_input("输入提交备注: ")
    os.popen('git add .')
    os.popen('git ci -m "%s"' % string)
    os.popen('git push origin master')
