def ready_event(channel, link):                # This event fires whenever the script fully launches
    print("Listening to "+channel+" at "+link) # Print the channel and link the script is listening to
    history = retrieve_past()                  # Retrieves the messages sent before this script was launched
    change_interval(0.1)                       # Changes the script run interval to every 0.1 seconds, set to 0 by default

def message_event(msg): # This event fires whenever there is a new message in chat
    author = msg[0]     # msg[0] is the message author
    content = msg[1]    # msg[1] is the message content
    message_id = msg[2] # msg[2] is the message id
    user_id = msg[3]    # msg[3] is the user id
    
    print(author+": "+content)      # Prints new chat messages
    # print(user_id+": "+message_id) # Prints new chat message ids

def tick(): # This event fires every chat check tick
    pass    # Do nothing

exec(open("main.py").read()) # Run the main.py code (DO NOT TOUCH)