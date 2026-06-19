import discord
from discord.ext import commands
import random

keep_alive()

TOKEN = "MASUKKAN_TOKEN_BOT"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    print(f"{bot.user} berhasil login!")

    activity = discord.Streaming(
        name="Testing Bot",
        url="https://www.twitch.tv/discord"
    )

    await bot.change_presence(
        status=discord.Status.online,
        activity=activity
    )

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel

    if channel:
        await channel.send(
            f"Selamat datang {member.mention} di server!"
        )

@bot.command()
async def ping(ctx):
    await ctx.send(
        f"Pong! {round(bot.latency * 1000)} ms"
    )

@bot.command()
async def halo(ctx):
    await ctx.send(
        f"Halo {ctx.author.mention}!"
    )

@bot.command()
async def dice(ctx):
    angka = random.randint(1, 6)
    await ctx.send(f"🎲 Hasil dadu: **{angka}**")

@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author

    embed = discord.Embed(
        title="Informasi Pengguna",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="Nama",
        value=member.name,
        inline=False
    )

    embed.add_field(
        name="ID",
        value=member.id,
        inline=False
    )

    embed.add_field(
        name="Bergabung",
        value=member.joined_at.strftime("%d/%m/%Y"),
        inline=False
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild

    embed = discord.Embed(
        title=guild.name,
        color=discord.Color.green()
    )

    embed.add_field(
        name="Anggota",
        value=guild.member_count
    )

    embed.add_field(
        name="Owner",
        value=guild.owner
    )

    embed.add_field(
        name="ID Server",
        value=guild.id
    )

    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)

    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Daftar Command",
        color=discord.Color.orange()
    )

    embed.add_field(
        name="!ping",
        value="Cek latency bot",
        inline=False
    )

    embed.add_field(
        name="!halo",
        value="Menyapa pengguna",
        inline=False
    )

    embed.add_field(
        name="!dice",
        value="Lempar dadu",
        inline=False
    )

    embed.add_field(
        name="!userinfo",
        value="Info pengguna",
        inline=False
    )

    embed.add_field(
        name="!serverinfo",
        value="Info server",
        inline=False
    )

    await ctx.send(embed=embed)

bot.run(TOKEN)
