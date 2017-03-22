# _*_ coding:UTF-8 _*_
#! /usr/bin/env python

from PIL import ImageGrab
import time
from test import *

print "是否更新坐标: Y or N "
updateflag = raw_input("Enter your choice: ")
if updateflag == 'Y' or 'y':
  print "鼠标放到所要拷贝区域左上角保持1S"
  plt_x, plt_y = set_cursor_po()
  temx, temy = plt_x, plt_y
  time.sleep(1)
  print "鼠标放到所要拷贝区域右下角保持1S"
  prd_x, prd_y = set_cursor_po()
  while (prd_x,prd_y == temx, temy):
      print "鼠标放到所要拷贝区域右下角保持1S"
      prd_x, prd_y = set_cursor_po()
      time.sleep(1)
  print "鼠标放到刷新按钮保持1S"
  pb_x, pb_y = set_cursor_po()
  temx, temy = prd_x,prd_y
  while (pb_x, pb_y == temx, temy):
      print "鼠标放到所要拷贝区域右下角保持1S"
      pb_x, pb_y = set_cursor_po()
      time.sleep(1)

for i in range(0,5):
    im = ImageGrab.grab([plt_x, plt_y, prd_x, prd_y])
    im.save('d:/' + str(i) + '.jpg', 'JPEG')
    mouse_click(pb_x,pb_y)
    time.sleep(3)
