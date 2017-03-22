# _*_ coding:UTF-8 _*_
#! /usr/bin/env python
from test import *


print "是否更新控件坐标: Y or N "
updateflag = raw_input("Enter your choice: ")
if updateflag == 'Y' or 'y':
  print "鼠标放到用户名框保持1S"
  user_x, user_y = set_cursor_po()
  time.sleep(1)
  print "鼠标放到password框保持1S"
  pas_x, pas_y = set_cursor_po()
  time.sleep(1)
  print "鼠标放到验证码输入框保持1S"
  vcode_x, vcode_y = set_cursor_po()
  time.sleep(1)
  print  "鼠标放到login保持1S"
  log_x, log_y = set_cursor_po()
  time.sleep(1)
  inputtextbox(user_x,user_y,'13818169690')
  p = str(251578056/314)
  inputtextbox(pas_x,pas_y,p)
  vcode = raw_input("Enter Vcode: ")
  inputtextbox(vcode_x, vcode_y, vcode)
  mouse_click(log_x,log_y)