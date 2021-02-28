from .imsp import imsp


def setup(bot):
    bot.add_cog(imsp(bot))