import disnake
from disnake.ext import commands
import sqlite3
# FIXME we don't need all these intents, only enough to see voice state updates
intents = disnake.Intents.all()

bot = commands.Bot(
    intents=intents, 
    command_prefix='/')

def dbSetup():
    db = sqlite3.connect('followBot.db', isolation_level=None)
    cur = db.cursor()
    cur.execute('SELECT name FROM sqlite_master;')
    if cur.fetchall() == []:
        # FIXME this isn't fully normalised, should probably have a link table
        cur.execute('''CREATE TABLE followed(
                    user INTEGER PRIMARY KEY
                    );''')
        cur.execute('''CREATE TABLE follower(
                    user INTEGER, 
                    following INTEGER,
                    FOREIGN KEY(following) REFERENCES followed(user)
                    );''')
    return cur

cur = dbSetup()

@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.slash_command()
async def follow(inter: disnake.ApplicationCommandInteraction, target: disnake.Member):
    cur.execute('INSERT INTO followed(user) VALUES (?);', (target.id, ))
    cur.execute('INSERT INTO follower(user, following) VALUES (?,?);', (inter.user.id, target.id))
    print(f'{target.name} is being followed by {inter.user.name}')
    await inter.response.send_message(
        f"following {target}")

@bot.event
async def on_voice_state_update(member: disnake.Member, before: disnake.VoiceState, after: disnake.VoiceState):
    if before.channel is not None or after.channel is None: # if the user was already in a channel, or left, do nothing
        return

    cur.execute('select follower.user from follower inner join followed where followed.user=?;', (member.id, ))
    followers = cur.fetchone()
    print(followers)
    for i in followers:
        await bot.get_user(i).send(f"{member} has joined {after.channel.name} in {after.channel.guild.name}")

with open("token.txt", "r") as f:
    bot.run(f.read())
