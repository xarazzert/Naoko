from discord import Embed
from discord.ext import commands
from random import randint

class JoinMessage():
    def __init__(self, bot):
        self.bot = bot

    def info_box(self, g):
        return f"""
:wave: Hey! Nice to meet you and your server **{g.name}**, thanks for adding me!
My name is **Naoko** and i'm **multifunctional** bot for Discord. You can view all my commands by using n.help or {g.me.mention} help

:link: Here are **useful** links:

**[➙ Bot Website](https://naokobot.github.io)**
**[➙ Support The Bot](https://patreon.com/F4stZ4p)**
**[➙ Support Server](https://discord.gg/y3Ph9Nj)**
                """

    def generate_join_embed(self, g):
        return Embed(title="Hello!", color=randint(0x000000, 0xFFFFFF), description=self.info_box(g)).set_footer(icon_url=g.icon_url, text=g.name).set_thumbnail(url=g.me.avatar_url)

    async def on_guild_join(self, guild):
        try:
            await guild.system_channel.send(embed=self.generate_join_embed(guild))
        except:
            pass

def setup(bot):
    bot.add_cog(JoinMessage(bot))
