from discord.ext import commands, tasks
import discord
from discord import FFmpegPCMAudio



TOKEN = "DISCORD_BOT_TOKEN"

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".")
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

is_playing = True

#on ready
@client.event
async def on_ready():
    print("Bot is ready/")
    await client.change_presence(activity = discord.Activity(type=discord.ActivityType.playing, name = "Waiting for commands"))


@client.command(aliases=['p', 'pla'])
async def play(ctx):
    sourceLink = "https://icecast.refnet.fm/utc/-0400"
    channel = ctx.message.author.voice.channel
    global player

    try:
        player = await channel.connect()
    except:
        pass
    player.play(FFmpegPCMAudio(sourceLink))



@client.command(aliases=['s', 'sto'])
async def stop(ctx):
    player.stop()

client.run(TOKEN)
print(client.user.name)