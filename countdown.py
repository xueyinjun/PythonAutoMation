# utf-8

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep()
    timeLeft = timeLeft - 1

subprocess.Popen(['start', 'alarm.wav'], shell=True)
