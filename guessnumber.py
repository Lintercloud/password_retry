# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:43:48 2020

@author: Linter
"""

password = "a123456"
chance = 3

while chance > 0:
    guess = input("請輸入密碼: ")
    chance = chance - 1
    if guess == password :
        print("恭喜你猜對了")
        break
    else:
        print("猜錯了")
        if chance > 0:
           print( "你還有", chance, "次機會")