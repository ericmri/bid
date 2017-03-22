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
 u_name_x, u_name_y = [1151, 299]
 pass_x, pass_y =  [1140, 366]
 v_code_x, v_code_y =  [1143, 410]
 sub_b_x, sub_b_y =  [1173, 541]
 x = 2517056.5574904
 x1 = x/3.1415926
 p = str(x1)
 inputtextbox(u_name_x,u_name_y,'13818169690')
 inputtextbox(pass_x,pass_y,p)
 wndh = get_wnd_handler('PyCharm Community')


 #getchildwnd(wndh,0)
 win32gui.SetWindowPos(wndh,win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOOWNERZORDER|win32con.SWP_SHOWWINDOW|win32con.SWP_NOSIZE)
 win32gui.SetWindowPos(wndh, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,win32con.SWP_NOMOVE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
 win32gui.SetForegroundWindow(wndh)
 time.sleep(0.1)
 win32api.keybd_event(0x0D, 0, 0, 0)
 win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
 time.sleep(0.1)
 win32api.keybd_event(0x0D, 0, 0, 0)
 win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
 vcode = raw_input("Enter your VCODE: ")
 inputtextbox(v_code_x,v_code_y,vcode)
 mouse_move(sub_b_x, sub_b_y)
 mouse_click()


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

