# vcPing
A small discord bot to subscribe to pings when someone joins a voice chat.

# setup

These instructions are intended for unix/linux systems, setup is similar but not the same for windows.  

Clone the git repo and change directory into it.  Create a virtual environment with `python3 -m venv venv` then activate with `source venv/bin/activate`.  Install the requirements with `python3 -m pip install -r requirements.txt`.  You may now run the server with `python3 followBot.py`

# Commands

## proof of concept

follow ::= /follow <user ping>
A user may not follow themselves.  the bot will dm the user who sent the command when the target user enters a vc and stays in it for 30 seconds.  

## future

subscribe command for the caller to get a ping or dm when the target user joins a vc (or in future, sends a number of messages in a small time frame).
follow ::= /vc <user> <method>
<user> ::= <regular ping> | <user id>
<method> ::= dm | ping
dm will send the caller a direct message, ping will ping in a set channel in the server.  

an unsubscribe command for a targeted user, e.g. to allow a user to unsubscribe someone from following them.  
