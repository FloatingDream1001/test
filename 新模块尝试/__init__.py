# -*- codeing=utf-8 -*-
# @Time : 2022/10/21 10:15
# @Author: 曹志阳
# @FALE __init__.py.py
# @software :PyCharm
import time
import random
import pyautogui
txt="I love Python"
time.sleep(3)#开始之前停三秒找到光标的位置
# for _ in range(10):#讲这句话循环10次输出
#     pyautogui.typewrite(txt,interval=0.15)#输入同样的话 ,interval每个字母保持0.15秒输出
#     pyautogui.press("Enter")#press单机某一个键   每输入完一句话，回车换行
#     time.sleep(2)#停隔两秒
#     #打开一个文件或者光标停留在某一上面即刻操作
#     #！！！一定要最后调回英文模式执行



with open('txt1','r',encoding = 'u8') as f:
    lines=f.readlines()

i=0

while True:
    pyautogui.typewrite(lines[i],interval=0.15)
    pyautogui.press ( "Enter" )  # press单机某一个键   每输入完一句话，回车换行
    time.sleep(1)
    i=i+1


