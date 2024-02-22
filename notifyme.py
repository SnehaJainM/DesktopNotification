from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "*** Take a Break ***",
            message ="5 minute ka break lo, \n Lambi saas lo , \n aankho ko aaram do",
            timeout=8)
        time.sleep(3600)