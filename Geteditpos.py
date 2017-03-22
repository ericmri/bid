# _*_ coding:UTF-8 _*_
#! /usr/bin/env python
import time
from pymouse import PyMouse,PyMouseEvent
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()
poslist = []

def exliststr(plist,x,y):
    plist.extend([str(x),str(y)])

class mmouse(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)

    def click(self, x, y, button, press):
        if button == 2:
            if press:
                self.x, self.y = x,y
                self.stop()


print "是否更新控件坐标: Y or N "
updateflag = raw_input("Enter your choice: ")
if updateflag == 'Y'or 'y':
    mm = mmouse()
    print "鼠标放到+price输入框点击右键"
    mm.run()
    add_x, add_y = mm.x, mm.y
    exliststr(poslist,add_x,add_y)
    print add_x,add_y
    mm = mmouse()
    print "鼠标放到+price确认图标点击右键"
    mm.run()
    add_b_x, add_b_y = mm.x, mm.y
    exliststr(poslist,add_b_x,add_b_y)
    print add_b_x, add_b_y
    mm = mmouse()
    print "鼠标放到价格输入框点击右键"
    mm.run()
    input_price_x, input_price_y = mm.x, mm.y
    exliststr(poslist,input_price_x,input_price_y)
    print input_price_x, input_price_y
    mm = mmouse()
    print "鼠标放到自选价格确认图标点击右键"
    mm.run()
    submit_x, submit_y = mm.x, mm.y
    exliststr(poslist,submit_x,submit_y)
    print submit_x, submit_y
    mm = mmouse()
    print "鼠标放到+300图标点击右键"
    mm.run()
    add300_x, add300_y = mm.x, mm.y
    exliststr(poslist,add300_x,add300_y)
    print add300_x, add300_y
    mm = mmouse()
    print "鼠标放到验证码确认按键点击右键"
    mm.run()
    vcode_con_x, vcode_con_y = mm.x, mm.y
    exliststr(poslist,vcode_con_x,vcode_con_y)
    print vcode_con_x, vcode_con_y

    file_abs = "d:\\pos.txt"
    with open(file_abs,"w") as f:
        for i in poslist:
            f.write(i+'\n')
    with open(file_abs,"r") as f:
        for line in f.readlines():
            poslist.append(int(line.strip('\n')))
    for i in poslist:
        print type(i)
        print i

