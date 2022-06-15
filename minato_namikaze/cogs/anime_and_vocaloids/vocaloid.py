from typing import TYPE_CHECKING

import discord
from discord.ext import commands
from lib.functions import meek_api

if TYPE_CHECKING:
    from lib import Context

    from ... import MinatoNamikazeBot


class Vocaloid(commands.Cog):
    def __init__(self, bot: "MinatoNamikazeBot"):
        self.bot: "MinatoNamikazeBot" = bot
        self.description = "Get some kawai pictures of the vocaloids."

    @property
    def display_emoji(self) -> discord.PartialEmoji:
        return discord.PartialEmoji(name="miku_wave", id=940993740967931914)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def rin(self, ctx: "Context"):
        """Rin kawai picture"""
        await ctx.send(embed=await meek_api("rin"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def una(self, ctx: "Context"):
        """Una kawai picture"""
        await ctx.send(embed=await meek_api("una"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def gumi(self, ctx: "Context"):
        """Gumi kawai picture"""
        await ctx.send(embed=await meek_api("gumi"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ia(self, ctx: "Context"):
        """Ia kawai picture"""
        await ctx.send(embed=await meek_api("ia"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def luka(self, ctx: "Context"):
        """Luka kawai picture"""
        await ctx.send(embed=await meek_api("luka"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def fukase(self, ctx: "Context"):
        """Fukase kawai picture"""
        await ctx.send(embed=await meek_api("fukase"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def miku(self, ctx: "Context"):
        """Hatsune Miku kawai picture"""
        await ctx.send(embed=await meek_api("miku"))

    @commands.command(name="len")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def _len(self, ctx: "Context"):
        """Len kawai picture"""
        await ctx.send(embed=await meek_api("len"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def kaito(self, ctx: "Context"):
        """Kaito kawai picture"""
        await ctx.send(embed=await meek_api("kaito"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def teto(self, ctx: "Context"):
        """Teto kawai picture"""
        await ctx.send(embed=await meek_api("teto"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def meiko(self, ctx: "Context"):
        """Meiko kawai picture"""
        await ctx.send(embed=await meek_api("meiko"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def yukari(self, ctx: "Context"):
        """Yukari kawai picture"""
        await ctx.send(embed=await meek_api("yukari"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def miki(self, ctx: "Context"):
        """Miki kawai picture"""
        await ctx.send(embed=await meek_api("miki"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def lily(self, ctx: "Context"):
        """Lily kawai picture"""
        await ctx.send(embed=await meek_api("lily"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def mayu(self, ctx: "Context"):
        """Mayu kawai picture"""
        await ctx.send(embed=await meek_api("mayu"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def aoki(self, ctx: "Context"):
        """Aoki kawai picture"""
        await ctx.send(embed=await meek_api("aoki"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def zola(self, ctx: "Context"):
        """Zola kawai picture"""
        await ctx.send(embed=await meek_api("zola"))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def diva(self, ctx: "Context"):
        """Random picturs from Project Diva"""
        await ctx.send(embed=await meek_api("diva"))


async def setup(bot: "MinatoNamikazeBot") -> None:
    await bot.add_cog(Vocaloid(bot))
