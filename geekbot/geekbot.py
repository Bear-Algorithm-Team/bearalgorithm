import discord
import sys
from datetime import datetime
from discord.ext import commands

if len(sys.argv) == 5:  # The first arg is the name of this file.
    GUILD_ID = int(sys.argv[1])
    CHANNEL_NAME = sys.argv[2]
    USER_ID = int(sys.argv[3])
    USER_NAME = sys.argv[4]
    GEEKBOT_ID = sys.argv[5]
else:
    print("Error: The number of arguments is not appropriate. You should use five arguments for this command.")
    print("Example: python3 ./geekbot.py 1138900602823393320 \"일반\" 882859405283041280 \"이강욱\" MTEzODg5MDAzNDM5MzY2NTY5OA.GfP9Zf.Lort5HAlrKrXuyyVjwGFYoxJ-ineIG3qoVoFuE")
    exit()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

questions = [
    "How do you feel today?",
    "What have you done since yesterday?",
    "What will you do today?",
    "Anything blocking your progress?"
]

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    target_guild = bot.get_guild(GUILD_ID)
    await start(target_guild.get_member(USER_ID), target_guild)

@bot.command()
async def start(member: discord.Member, target_guild: discord.Guild):
    dm_channel = await member.create_dm()
    await dm_channel.send(f"Salute {USER_NAME}! It's time for Daily in #{CHANNEL_NAME}. Please share what you've been working on.")

    answers = []
    for question in questions:
        # Question to the user via DM
        dm_channel = await member.create_dm()
        await dm_channel.send(question)

        # Wait for the user's response in DM
        def check(m):
            return m.author == member and isinstance(m.channel, discord.DMChannel)

        msg = await bot.wait_for('message', check=check)

        # Save user's response
        answers.append(msg.content)

    dm_channel = await member.create_dm()
    await dm_channel.send("Thank you! Have a nice day!")

    # Compile all responses
    today = datetime.today()
    formatted_date = today.strftime("%a, %d %B")
    response_form = f"**{USER_NAME}** posted a status update for **{formatted_date}**\n>>> " \
                      + "\n".join([f"**{questions[i]}**\n{answers[i]}" for i in range(4)])

    # Send the form to the target channel
    target_channel = discord.utils.get(target_guild.text_channels, name=CHANNEL_NAME)
    await target_channel.send(response_form)

    # Close the bot
    await bot.close()
    print("Completed today's daily report successfully!")

bot.run(GEEKBOT_ID)
