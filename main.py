from os import system as sys
from time import sleep as wait
from concurrent.futures import ThreadPoolExecutor as tpe

import atexit
from tkinter import messagebox

try:
    from undetected_chromedriver import Chrome, By
    import undetected_chromedriver as uc
except:
    sys("pip install setuptools") # Prevents wheel building issues when downloading the packages below
    sys("pip install selenium==4.10.0") # Selenium is required for UC to function
    sys("pip install undetected_chromedriver")
    from undetected_chromedriver import Chrome, By
    import undetected_chromedriver as uc

thread = tpe(max_workers=100)

channel = open("channel.txt",'r').read()
url = "https://www.kick.com/"+channel+"/chatroom"
# Get the users chatroom url

options = uc.ChromeOptions()
browser = Chrome(use_subprocess=True, options=options)
browser.set_window_size(1, 1, browser.window_handles[0])
# Open a new browser

browser.get(url)
# Launch users chatroom in the browser

sys('cls')

readMessages = []
history = []
firstRun = True
interval = 0

def retrieve_past():
    return history
def change_interval(target):
    interval = target

wait(2.5)
# Let the browser load

if browser.page_source.find("Checking if the site connection is secure"): # Captcha page has triggered
    print("Waiting for captcha to be finished...")
while browser.page_source.find("Checking if the site connection is secure") != -1: # Wait until the captcha page is passed
    wait(0.1)

sys("cls")

thread.submit(ready_event, channel, url) # Trigger the ready_event function
while True:
    wait(interval)
    # Limit the speed of the message reading for performance reasons

    page = browser.page_source
    # Get the page source

    if page.find("Oops, Something went wrong") != -1:
        messagebox.showwarning("Warning", "The browser seems to have gotten a 404 error, make sure you entered your channel name into channel.txt correctly. It is case sensitive, make sure you enter just the username, not the full channel url.")
    # Got 404 page; user probably entered the wrong channel name

    # Below lies a bunch of magic to cut the page html and turn it into a list of messages
    messagesFormatted = []
    
    msgSplit = page.split('data-chat-entry="')
    del msgSplit[0]

    msgs = []
    usrs = []
    usrs_ids = []
    ids = []

    for v in msgSplit:
        if (v.find("chatroom-history-breaker") != -1):
            continue

        ids.append(v.split('"')[0])

        currentMsgList = v.split('class="chat-entry-content">')
        del currentMsgList[0]
        currentMsg = ""

        for i in currentMsgList:
            currentMsg += i.split("</span>")[0] + " "
        currentMsg = currentMsg[0:len(currentMsg)-1]
        msgs.append(currentMsg)

        usrs_ids.append(v.split('data-chat-entry-user-id="')[1].split('"')[0])
        colorCode = v.split('id="'+usrs_ids[len(usrs_ids)-1]+'" style="')[1].split(');">')[0]
        usrs.append(v.split(colorCode + ');">')[1].split("</span>")[0])
    
    for i,v in enumerate(msgs):
        messagesFormatted.append([usrs[i],msgs[i],ids[i],usrs_ids[i]])

    for i,v in enumerate(messagesFormatted):
        if v[2] not in readMessages:
            newMsg = v
            if not firstRun:
                thread.submit(message_event,newMsg)
            else:
                history.append(newMsg)
            readMessages.append(v[2])
    firstRun = False

    # Magic is done
    thread.submit(tick) # Trigger the tick function