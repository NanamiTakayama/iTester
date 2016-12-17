from updater import Updater
import time

while True:
    test = Updater(2,1)
    test.newapp()
    print(test)
    test.addcommit()
    test.push()
    print("___finish___")
    break
