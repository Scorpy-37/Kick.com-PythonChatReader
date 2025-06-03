Hello, thank you for using my script for reading Kick.com chat messages!
For you to understand how to use this script effectively I recommend you at least skim over this file.

After 2 years of the script existing, and an entire year of me not maintaining it anymore, it is still surprisingly working with minimal issues and many people still using to read their stream chats.
Thank you a lot to everyone using the script and to those who had helped me with the project before, I appreciate you all a lot.



CONTACT (READ FULLY BEFORE CONTACTING):

If you're having problems with the script or are having issues understand how to use it feel free to contact my on Discord at 37scorpions.
However if you're going to DM me, once I add you back please don't waste time to explain why you're adding me and to explain your situation. I often receive spam or scam DMs on Discord so if you take a while to explain that you added me because of this script I may not be the most willing to speak to you.
A few notes:
1. I may not be able to help with issues that occur with your scripts. I can help with my part of the code, however I can only try to help with your part.
2. Do not DM me at all if you don't know Python and are looking for someone to teach you the entire language.
3. Do not DM me asking me to work for you
4. Be weary: I am gay and a furry so if you're homophobic don't add me I guess.


ABOUT (READ FULLY BEFORE USING):

This script is an old-school python-based Kick.com chat reader that utilizes undetected browsers to open the chatroom of a channel and read the HTML to detect chat messages.
The script is made for people looking to READ chat messages without the ability to SEND chat messages.


RULES (READ FULLY BEFORE USING):

This script was made to support creative and interactive streamers on Kick looking to have fun with their chat.
I do not support or condone this scripts usage to promote or simulate gambling, including but not limited to viewer-activated slot machines, roulette, or other wagering systems.
I also do not condone the usage of this script to scrape chats of channels without consent. You must either have permission from the channel owner to use this script on their channel or use it on your own channels.


SETUP:

1: Open the channel.txt file and enter your channels username
2: Open script.py with a text editor or python IDE and edit the code within to do whatever you want it to do
3: Save it and run script.py
4: Done!



NOTES:

- The script automatically installs its dependencies.

- You need to have PIP, otherwise the script will fail to install them.

- If you run into an issue with my script (main.py), either check for a newer version on the GitHub page or contact me on Discord and notify me of the issue.

- You don't need to be streaming for this script to work.

- Make sure you have Chrome installed, undetected-chromedriver may not function without it. You may also need to update your Chrome browser if the script fails to run the browser.

- This script is old and uses some questionable methods of parsing HTML. I am aware of that however I can't be bothered to fix it.

- If you have package related issues (ones coming from packages instead of the scripts themselves) try installing these specific versions of the required packages: selenium 4.10.0, undetected_chromedriver 3.5.3

- If you're having issues with script.py that are related to difficulty understanding how it works feel free to contact me on Discord.

- The methods this script uses to read chat is likely outdated. I recommend looking for more API-based scripts.


Q&A:

- How does it work?
It launches a browser (Chrome) using undetected_chromedriver, goes to your channels chatroom page on Kick.com and reads the page source to fetch messages.

- Is it reliable?
Kick.com HTML structure changes tend to break the script, however that has not happened in a while (over a year now) and most issues are easily fixable.

- Can I send chat messages with this?
Yes, but the script has removed the ability to send messages to avoid confusion.
Sending messages using this script is very impractical, requiring you to log into Kick.com and have the browser focused to send messages.
So while you *can* send messages using the browser, this script is focused on READING chat messages, not sending.

- Do I need to credit you?
If you want to, yes.

- Is this a virus?
No, but make sure to read the code before executing any scripts.



IDEAS:

- Chat message TTS
Read chat messages using the pyttsx3 text to speech package. (https://pypi.org/project/pyttsx3/)
   Available in Extras folder!

- Chat sound effects
Play sounds when chat uses certain commands, for example !fart

- Chat plays
Allow chat to use your keyboard/mouse by making commands to use them, for example !mouse up, !move left

- Welcome messages
Welcome new people in chat by displaying a file on your stream that says the users name

- Polls
Make chat be able to vote by inputting numbers in chat

and much more! The limit is your imagination... and your python knowledge.



CHANGELOG:

v1.11
- made the reader wait until you finish the page captcha to prevent reading problems
- fixed update.py

v1.12
- made install.py only get selenium 4.10.0
- fixed script not picking up on bot usernames

v1.13
- made install.py install setuptools because undetected_chromedriver seems to require it
- fixed and improved update.py

v1.14
- significantly cut down on the amount of files
- slightly documented reader.py
- changed reader.py name to main.py
- improved README.txt
- made browser make itself smaller
- fixed tts extra script

v1.15
- added pop up telling user to update browser if the browser returns null
- updated README.txt



END OF FILE:

Thanks to DKnightX91 for telling me about undetected_chromedriver! This project would be nothing without them.
Want to support me? Just a thanks is enough!

My Discord: 37scorpions
Project GitHub link: https://github.com/Scorpy-37/Kick.com-PythonChatReader



Wow, you really read the entire file. Nice.
Have fun now I guess
