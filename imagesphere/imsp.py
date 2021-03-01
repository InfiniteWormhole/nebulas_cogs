from redbot.core import commands
import os
import io
import requests
import discord

class imsp(commands.Cog):
    """Image Sphere Generator"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def imsp(self, ctx, urls=""):
        """Spherify an image!"""
        msg = await ctx.message.channel.send("processing...")
        async with ctx.typing():
            #response = requests.get(ctx.message.attachments[0].url)
            # file = open("/tmp/imsp/input.png", "wb")
            # file.write(response.content)
            # file.close()
            dl_command = ''
            if(urls or ctx.message.attachments):
                attach = ctx.message.attachments[0].url if not urls else urls
            else:
                attach = ""
            if(not attach):
                await ctx.send(content="Please provide an image")
            else:
                if "tenor.com" in attach:
                    dl_command = '(ulimit -f $(({bytes}/512)); curl --max-filesize {bytes} {url} -o tenor.gif)'
                else:
                    dl_command = '(ulimit -f $(({bytes}/512)); curl --max-filesize {bytes} -OJ {url})'
                #os.system("wget "+attach+' -P /tmp/imsp/input/')
                os.system("cd /tmp/imsp/input; " + dl_command.format(bytes=100000000, url=attach))
                os.system('bash /tmp/imsp/imsp.sh')
                image = io.open("/tmp/imsp/out/out.gif", "rb")
                dcfile = discord.File(image, filename="sphere.gif")
                await ctx.send(content = "", file = dcfile)
                os.system('bash /tmp/imsp/clean.sh')
            await msg.delete()  
def setup(bot):
    bot.add_cog(imsp(bot))
