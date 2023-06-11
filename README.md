# vcPing
A small discord bot to subscribe to pings when someone joins a voice chat.

# setup

To run this bot, install docker, then run `docker compose build`, then `docker compose up -d`.  

# Commands

## proof of concept

follow ::= /follow \<user ping\>

A user may not follow themselves.  the bot will dm the user who sent the command when the target user enters a vc and stays in it for 30 seconds.  

## future

A subscribe command for the caller to get a ping or dm when the target user joins a vc (or in future, sends a number of messages in a small time frame).

follow ::= /vc \<user\> \<method\>

\<user\> ::= \<regular ping\> | \<user id\>

\<method\> ::= dm | ping

dm will send the caller a direct message, ping will ping in a set channel in the server.  

an unsubscribe command for a targeted user, e.g. to allow a user to unsubscribe someone from following them.  

### other features

- rate limiting
- ignore AFK channels

### back end

A logging framework would be nice.  
