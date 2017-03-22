# _*_ coding:UTF-8 _*_
#! /usr/bin/env python

from test import *
import time
import win32api
import win32con
import win32gui
import win32com
from ctypes import *

if __name__ == "__main__":
 e_x, e_y = 1003, 122
 file_abs = "d:\\pos.txt"
 poslist = []
 with open(file_abs, "r") as f:
  for line in f.readlines():
   poslist.append(int(line.strip('\n')))
 # print "是否更新控件坐标: Y or N "
 # updateflag = raw_input("Enter your choice: ")
 # isfirstrun = True
 # if updateflag == 'Y'or 'y' and isfirstrun:
 #  print "鼠标放到+price图标保持1S"
 #  add_x, add_y = print_cursor_po()
 #  print "鼠标放到+price确认图标保持1S"
 #  add_b_x, add_b_y = print_cursor_po()
 #  print "鼠标放到价格输入框保持1S"
 #  input_price_x, input_price_y = 869, 446
 #  print "鼠标放到自选价格确认图标保持1S"
 #  submit_x, submit_y = 975, 454
 #  print "鼠标放到+300图标保持1S"
 #  add300_x, add300_y = 844, 421
 #  print "鼠标放到验证码确认按键保持1S"
 #  vcode_con_x, vcode_con_y = 763, 519
 #
 # add_x, add_y = 865, 360
 # add_b_x, add_b_y = 964, 361
 # input_price_x, input_price_y = 869, 446
 # submit_x, submit_y = 975, 454
 # add300_x, add300_y = 844, 421
 # vcode_tx, vcode_ty = 903, 449
 # vcode_con_x, vcode_con_y = 763, 519
 # py_x, py_y = 226, 586
 print len(poslist)
 print poslist[0:2]
 add_x, add_y = poslist[0:2]
 add_b_x, add_b_y = poslist[3:5]
 input_price_x, input_price_y = poslist[6:8]
 submit_x, submit_y = poslist[0:2]
 add300_x, add300_y = poslist[9:11]
 vcode_tx, vcode_ty = poslist[9:11]
 vcode_con_x, vcode_con_y = 763, 519
 py_x, py_y = 226, 586

#-------------------------------------------
 # mouse_move(e_x, e_y)
 # mouse_click()
 # mouse_move(add300_x, add300_y)
 # mouse_click()
 # time.sleep(0.2)
 mouse_move(submit_x, submit_y)
 mouse_click()
 wndh = get_wnd_handler('PyCharm Community')

 win32gui.SetForegroundWindow(wndh)
 win32gui.SetWindowPos(wndh,win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE |win32con.SWP_SHOWWINDOW|win32con.SWP_NOSIZE)
 win32gui.SetActiveWindow(wndh)
 vcode = raw_input("Enter your input: ")
 # inputtextbox(vcode_tx,vcode_ty,vcode)
 # mouse_move(vcode_con_x, vcode_con_y)
 # mouse_click()
 # --------------------------------------------------

 # inputtextbox(login_x, login_y, '53925237')
 # time.sleep(0.1)
 # inputtextbox(pass_x, pass_y, '4743')
 # time.sleep(0.1)
 # vcode = raw_input("Enter your input: ")
 # inputtextbox(log_code_x, log_code_y, vcode)
 # time.sleep(0.1)
 # mouse_move(log_b_x,log_b_y)
 # mouse_click()

# inputtextbox(100,100,'password')
# ispageload()
# inputtextbox(100,100,'price')
# keyboard_input(100,100) #验证码
#  mouse_move(1022, 35)
#  mouse_click()

