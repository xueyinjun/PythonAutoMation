#enconding=utf-8

# import pyautogui
# pyautogui.PAUSE = 1
# pyautogui.FAILSAFE =True
# import pyautogui
# print(pyautogui.size())
# width ,height = pyautogui.size()

#将鼠标立即移动到屏幕指定的位置
# import pyautogui
# for i in range(10):
#     pyautogui.moveTo(100,100,duration=0.25)
#     pyautogui.moveTo(200,100,duration=0.25)
#     pyautogui.moveTo(200.200,duration=0.25)
#     pyautogui.moveTo(100,200,duration=0.25)

#当前位置移动鼠标
# import pyautogui
# for  i in range(10):
#     pyautogui.moveRel(100,0,duration=0.25)
#     pyautogui.moveRel(0,100,duration=0.25)
#     pyautogui.moveRel(-100,0,duration=0.25)
#     pyautogui.moveRel(0,-100,duration=0.25)

#获取鼠标的位置
# import pyautogui

# print(pyautogui.position())

# mouseNow.py - Displays the mouse cursor's

# import pyautogui
# print('Press Ctrl-C to quit.')

# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
#         print(positionStr, end='')
#         # 利用字符串复制得到需要\b字符构成的字符串，长度与position中保存的字符串长度一样
#         print('\b' * len(positionStr), end='', flush=True)

# except KeyboardInterrupt:
#     print('\nDone')


#点击鼠标
# import  pyautogui
#点击将使用鼠标鼠标左键，butto关键字参数,分别是left, right,middle
# pyautogui.click(10,5,button='left')
#实现点击还可以调用的方法
# pyautogui.mouseDown()
# pyautogui.mouseUp()

#只执行双击鼠标左键
# pyautogui.doubleClick()
# pyautogui.rightClick()
# pyautogui.leftClick()

# x,y轴是水平和垂直移动的 自动绘画
# import pyautogui, time
# time.sleep(5)

# #click to put drawing program in focus
# pyautogui.click()

# distance = 200
# while distance > 0:
#     #move right
#     pyautogui.dragRel(distance, 0, duration=0.2)
#     distance = distance - 5
#     #move down
#     pyautogui.dragRel(0, distance, duration=0.2)
#     #move left
#     pyautogui.dragRel(-distance, 0, duration=0.2)
#     distance = distance - 5
#     #move up
#     pyautogui.dragRel(0, -distance, duration=0.2)

#滚动鼠标
# import  time,pyautogui
# time.sleep ;pyautogui.scroll(200)

#替代代码
# import pyperclip
# numbers = ''
# for i in range(200):
#     numbers = numbers + str(i) + '\n'
# pyperclip.copy(numbers)

#处理屏幕
# import pyautogui

# im = pyautogui.screenshot()
# print(im.getpixel((0, 0)))
# print(im.getpixel((50, 200)))
# pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
# pyautogui.pixelMatchesColor(50,200,(255,135,144))

#给出鼠标当前位置，也给出像素RGB颜色
# import pyautogui
# print('Press Ctrl-C to quit')

# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
#         pixelColor = pyautogui.screenshot().getpixel((x, y))
#         positionStr += ' RGB:( ' + str(pixelColor[0]).rjust(3)
#         positionStr += ', ' + str(pixelColor[1]).rjust(3)
#         positionStr += ' , ' + str(pixelColor[2]).rjust(3) + ')'
#         print(positionStr, end='')
# except KeyboardInterrupt:
#     print('\nDnoe')

#图像识别 locateOnScreen函数返回图像所处的坐标,返回4个整数的元组

# import pyautogui
# pyautogui.locateOnScreen('submit.png')
 
#如果找到多处图像用locateAllOnScreen 函数返回一个Generator可以将它传递给list返回一个4整数的元祖列表
# list(pyautogui.locateAllOnScreen('submit.png'))
#图像所在屏幕区域的4整数元组后，点击中心区域将元组传递给center函数
# pyautogui.center((643,745,70,29))

#键盘识别 typewrite()函数向计算机发送虚拟键，第二个参数是时间
# import  pyautogui
# pyautogui.click(100,100);pyautogui.typewrite('Hello world',0.25)

#键名
# pyautogui.typewrite(['a','b','left','left','X'])

#按下和释放键盘 press函数是更简单的方式
# pyautogui.keyDown('shift');pyautogui.press('4');pyautogui.keyUp('shift')

#热键组合
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('C')
# pyautogui.keyUp('C')
# pyautogui.keyUp('ctrl')
# pyautogui.hotkey('ctrl','c')

# import pyautogui, time
# def commentAfterDelay():
#     pyautogui.click(100,100)
#     pyautogui.typewrite('In IDLE Alt-3 comments out a line.')
#     time.sleep(2)
#     pyautogui.hotkey('alt','3')

# commentAfterDelay()