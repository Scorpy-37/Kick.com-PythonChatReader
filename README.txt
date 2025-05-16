Edit: Thanks to all the support and usage of the script! I'm surprised it still works after so long of not being maintained

Hello! Thank you for using my script for reading Kick.com chat messages :3
If you don't like reading, just quickly skim over this file and read anything that catches your eye. It is quite important to read this to understand how to use it.



CONTACT (READ FULLY BEFORE CONTACTING):

Need help with anything? Contact me on Discord at 37scorpions!
When DMing me do tell me that you're referring to this script, I can't read your mind.
Note that I am only here to help you with problems that arise while using the script or if you don't understand how something works. Don't DM me if you don't know how python works, don't DM me if you need help with python related problems and certainly don't DM me if you expect me to work for you (I'm a minor lol).
Also brief warning before you contact me, I am a furry and I like boys. Yes, I'm not lying. Many people have gotten mad at me about it after adding me to message me.



ABOUT (READ FULLY BEFORE USING):

This script is a simple python-based Kick.com chat reader that opens a browser and reads the HTML to fetch chat messages, it does NOT use the API to read the chat.
It is made for people who know Python and are looking to skip needing to decompile the structure of the Kick.com website to read chat messages.
Let your imagination run loose without needing to lay the floors it runs on.



SETUP:

1: Open the channel.txt file and enter your channels username
2: Open script.py with a text editor or python IDE and edit the code within to do whatever you want it to do
3: Save it and run script.py
4: Done!



NOTES:

- You NEED to have PIP for the packages, otherwise the script will fail to install them.
- If you run into any issues try checking the github page for whether there is a newer version, otherwise DM me and I'll try to fix it.
- You don't need to be streaming for this script to work.
- Make sure you have Chrome installed, undetected-chromedriver may not function without it.
- If you have package related issues (ones coming from packages instead of the scripts themselves) try installing these specific versions of the required packages: selenium 4.10.0, undetected_chromedriver 3.5.3
- If the script doesn't work, give it a kiss and try again.
- If the script still doesn't work, contact me on Discord.



Q&A:

- How does it work?
It launches a browser (Chrome) using undetected_chromedriver, goes to your channels chatroom page on Kick.com and reads the page source to fetch messages.

- Why should I use this?
No reason, as people look deeper and deeper into Kicks API a lot of more conviniant wrappers are getting out into the public. This script was made at the very start of Kick when no one knew anything about the API so it was pretty useful back then, now it can be replaced by scripts that use the API.

- Is it reliable?
Due to HTML structure changes the script does tend to break but it's been a while since that happened. If you ever have issues with the script that seem to come from it being out of date you can DM me and I'll try to get it fixed.

- Can I send chat messages with this?
Yes, but no... well, you kind of could but not anymore. If you're looking to use this as a simple chat reader, go ahead, though if you want to make something more complex like a bot I heavily advise you to go out and look for an API wrapper made by someone else, or even make your own. This script uses a browser to fetch messages from the browser source rather than the kick.com API so that introduces a few obsticles into the message sending process such as needing to log in each time you launch the script and that you have to focus the browser all of the time in order to send messages, so you technically could send messages but I removed the functions to not cause any confusion. TL;DR: if you want to send messages, find an API wrapper.

- Does this come with premade scripts?
Yes, one. It's a text to speech script that reads chat messages aloud. You can find it in the extras folder.

- Do I need to credit you?
No... Unless you want to.

- Can I install this script as a package using PIP?
No, I cannot be bothered to find a way to make this into a PIP package, you can only use this by downloading the project files and modifying the script.py file.

- Is this a virus?
No, but good that you're being cautious. For your own safety make sure to review this script (and any script you get in the future) to make sure it won't perform malicious actions on your device, especially if you accidentally got it from someone who isn't me (Scorp). Stay safe out there!



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



END OF FILE:

Thanks to DKnightX91 for showing me undetected_chromedriver!
Want to support me? Just a thanks is enough <3

If you're looking for an API wrapper capable of reading AND sending messages you can check out https://github.com/cibere/kick.py, haven't tried it myself but it looks like a good async API wrapper.



Wow, you really read the entire file. Nice.
Have fun now I guess
