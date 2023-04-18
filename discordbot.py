import discord
import os
from discord.ext import commands


bot_prefix = "!"  # 봇의 접두사를 지정합니다.
intents = discord.Intents.default()  # 기본 의도를 사용합니다.
intents.message_content = True #v2
bot = commands.Bot(command_prefix=bot_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def 버튼(ctx):
    button = discord.ui.Button(
        label='비공개 채널 입장',
        style=discord.ButtonStyle.primary,
        custom_id='private_channel'
    )
    row = discord.ui.Row(button)
    await ctx.send(
        content='비공개 채널에 입장하시려면 아래 버튼을 클릭해주세요.',
        components=[row]
    )

@bot.event
async def on_button_click(interaction):
    if interaction.custom_id == 'private_channel':
        channel = await bot.fetch_channel(1097734174170959872) # 비공개 채널 ID를 입력하세요.
        if channel:
            await interaction.author.add_roles(1034824593678012489) # 비공개 채널에 접근 가능한 역할 ID를 입력하세요.
            await interaction.response.send_message('비공개 채널에 입장하셨습니다!', ephemeral=True)

access_token = os.environ["TOKEN"]
bot.run(access_token)
