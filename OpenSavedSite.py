import os,pyautogui,time
savedSite = open("savedSite.i",'r')
siteList = savedSite.read().split()
name = []
site = []
for check in range(0,len(siteList),2):
    name.append(siteList[check])
    site.append(siteList[check+1])
nameChecking = input("Name:")
s = ''
for n in range(0,len(name)):
    if name[n] == nameChecking:
        s = site[n]
if s != '':
    os.system('start firefox')
    time.sleep(5)
    pyautogui.write(s)
    pyautogui.press('enter')
else:
    print("This Site In Saved Sites Is Not Found")