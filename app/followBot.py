import disnake
from disnake.ext import commands
import sqlite3

def getCursor():
    db = sqlite3.connect('/data/followBot.db', isolation_level=None)
    cur = db.cursor()
    cur.execute('SELECT name FROM sqlite_master;')
    if cur.fetchall() == []:
        # caution this isn't fully normalised, if the application grows larger then change schema
        cur.execute('''CREATE TABLE followLink(
                    user INTEGER, 
                    following INTEGER
                    );''')
    return cur

def setup():
    global bot, cur

    intents = disnake.Intents(guilds=True,       # strongly recommended by disnake for general functionality
                              voice_states=True, #for on_voice_state_update
                              dm_messages=True,  # for members to use commands in dms
                              members=True)      # for bot.get_user()

    bot = commands.InteractionBot(intents=intents)

    cur = getCursor()

setup()

@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.slash_command()
async def follow(inter: disnake.ApplicationCommandInteraction, target: disnake.Member):
    cur.execute('INSERT INTO followLink(user, following) VALUES (?,?);', (inter.user.id, target.id))
    print(f'{target.name} is being followed by {inter.user.name}')
    await inter.response.send_message(
        f'following {target.name}')

@bot.event
async def on_voice_state_update(member: disnake.Member, before: disnake.VoiceState, after: disnake.VoiceState):
    if before.channel is not None or after.channel is None: # if the user was already in a channel, or left, do nothing
        return

    cur.execute('SELECT user FROM followLink WHERE following=?;', (member.id, ))
    followers = cur.fetchone()
    if followers is None:
        return

    for i in followers:
        follower = bot.get_user(i)
        if follower != None:
            await follower.send(f"{member} has joined {after.channel.name} in {after.channel.guild.name}!")

def main():
    with open('token.txt', 'r') as f:
        bot.run(f.read())

main()