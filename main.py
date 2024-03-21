import discord
from discord import app_commands 
from discord.ext import commands

# 創建 client 對象
class client(discord.Client):
    def __init__(self):
        # 設置 intents，包括成員列表
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(intents=intents)
        self.synced = False 

    async def on_ready(self):
        # 等待機器人登錄完成
        await self.wait_until_ready()
        if not self.synced: # 檢查斜線指令是否已經同步 
            # 同步指令到特定伺服器，如果是全域指令則留白
            await tree.sync(guild = discord.Object(id=guild_id))
            self.synced = True
        print(f"We have logged in as {self.user}.")

bot = client()

# 創建 CommandTree 對象，用於處理指令
tree = app_commands.CommandTree(bot)

# 定義斜線指令的處理函數
@tree.command(guild = discord.Object(id=guild_id), name = 'test1', description='測試') # guild specific slash command
async def slash2(interaction: discord.Interaction):
    # 回應一個消息，並設置為僅客戶端可見
    await interaction.response.send_message(f"初步測試成功{interaction.user.mention}", ephemeral = True)

@tree.command(guild = discord.Object(id=guild_id), name = 'test2', description='沒東西 別看!')
async def img(interaction: discord.Interaction):
    # 從機器人所在的頻道中獲取頻道對象，然後回應一個消息
    channel = bot.get_channel(channel_id)
    await interaction.response.send_message(f"{interaction.user.mention}抓到摸魚", ephemeral = False)

@tree.command(guild = discord.Object(id=guild_id), name = 'test3', description='試試')
async def kfg(interaction: discord.Interaction):
    # 回應一個消息，並設置為公開可見
    await interaction.response.send_message(f"試試就逝世",ephemeral=False)

# 登錄機器人，開始運行程式
bot.run("token")
