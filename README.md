# Disclaimer

This bot is currently in a proof of concept state.  It will work in a small server with people who trust one-another, but it has a large potential for abuse.  Please do not use on large servers where one member may not trust all other members.  The bot also has a number of missing features.  See the future section below.  Only use this bot in one server at a time.

# vcPing

A small discord bot to subscribe to pings when someone joins a voice chat.

# Setup

To run this bot, copy your bot token into `./app/token.txt`(without a trailing newline or any other text).  Then install docker, run `docker compose build`, then `docker compose up -d`.  

# Commands

## Proof of Concept

follow ::= /follow \<user ping\>

A user may not follow themselves.  The bot will dm the user who sent the command when the target user enters a vc and stays in it for 30 seconds.  

## Future

A subscribe command for the caller to get a ping or dm when the target user joins a vc (or in future, sends a number of messages in a small time frame).

follow ::= /vc \<user\> \<method\>

\<user\> ::= \<regular ping\> | \<user id\>

\<method\> ::= dm | ping

dm will send the caller a direct message, ping will ping in a set channel in the server.  

An unsubscribe command for a targeted user, e.g. to allow a user to unsubscribe someone from following them.  

### Other Features

- Rate limiting
- Ignore AFK channels
- Work out what happens with many servers per bot

### Back End

A logging framework would be nice.  
