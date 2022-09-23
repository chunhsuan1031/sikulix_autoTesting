from sikuli import *

# adb common use
def reopenApp():
    click("1662973655334.png")
    if exists("1662603882286.png",3):
        click("1662603882286.png")
        sleep(1)
    type("1650506536780-1.png","adb shell am force-stop com.lein.pppoker.android" + Key.ENTER) 
    sleep(1)
    type("1650506536780-1.png","adb shell monkey -p com.lein.pppoker.android 1" + Key.ENTER)
    wait(Pattern("1661397070003.png").similar(0.94),180)
    sleep(1)

def closeApp():
    click("1662973655334.png")
    if exists("1662603882286.png",3):
        click("1662603882286.png")
        sleep(1)
    type("1650506536780-1.png","adb shell am force-stop com.lein.pppoker.android" + Key.ENTER)
    
def openApp():
    click("1662973655334.png")
    if exists("1662603882286.png",3):
        click("1662603882286.png")
        sleep(1)
    type("1650506536780-1.png","adb shell monkey -p com.lein.pppoker.android 1" + Key.ENTER)
    wait(Pattern("1661397070003.png").similar(0.91),180)
    sleep(1)

def declineInvitation():
    while 1:
        if exists(Pattern("1662606059037.png").similar(0.95)and"1662606066801.png",1):
            print("close invitation")
            click(Pattern("1662606059037.png").similar(0.95))
            wait(1)
        else:
            print("no invitation")
            break

def waitPush():
    if exists(Pattern("1663039496447.png").similar(0.95)or(Pattern("1663039506159.png").similar(0.93))):
        sleep(10)

def globalTournamentNotice():
    if exists(Pattern("1663921130323.png").similar(0.90),1):
        click(Pattern("1663921130323.png").similar(0.90))
        print("close globalTournamentNotice")