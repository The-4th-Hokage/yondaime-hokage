import discord

def check_if_support_is_setup(ctx):
    if discord.utils.get(ctx.guild.text_channels, topic='This channel will be used as a support channel for thsi server.'):
        support_channel = True
    else:
        support_channel = False
    return support_channel


def perms_dict(ctx):
    admin_roles = [
        role for role in ctx.guild.roles if role.permissions.manage_guild and not role.managed
    ]
    overwrite_dict = {}
    for i in admin_roles:
        overwrite_dict[i] = discord.PermissionOverwrite(read_messages=True)
    overwrite_dict.update({ctx.guild.default_role: discord.PermissionOverwrite(
        read_messages=False), ctx.guild.me: discord.PermissionOverwrite(read_messages=True)})
    return admin_roles, overwrite_dict


async def channel_creation(ctx):
    admin_roles, overwrite_dict = perms_dict(ctx)

    category = discord.utils.get(ctx.guild.categories, name="Admin / Feedback") if discord.utils.get(
        ctx.guild.categories, name="Admin / Feedback") else False

    # Feedback Channel
    if discord.utils.get(ctx.guild.text_channels, topic='Feedback given by the members of the servers will be logged here.'):
        feed_channel = discord.utils.get(
            ctx.guild.text_channels,
            topic='Feedback given by the members of the servers will be logged here.'
        )
    else:
        feed_channel = False

    # Ban
    if discord.utils.get(ctx.guild.text_channels, topic='Bans of the server will be logged here.',):
        ban = discord.utils.get(
            ctx.guild.text_channels,
            topic='Bans of the server will be logged here.'
        )
    else:
        ban = False

    # Unban
    if discord.utils.get(ctx.guild.text_channels, name="unban"):
        unban = discord.utils.get(
            ctx.guild.text_channels,
            topic='Unbans of the server will be logged here.',
        )
    else:
        unban = False

    # Support
    if discord.utils.get(ctx.guild.text_channels, topic='This channel will be used as a support channel for thsi server.'):
        support_channel = discord.utils.get(
            ctx.guild.text_channels,
            topic='This channel will be used as a support channel for this server.'
        )
    else:
        support_channel = False

    support_channel_roles = discord.utils.get(ctx.guild.roles, name="SupportRequired") if discord.utils.get(
        ctx.guild.roles, name="SupportRequired") else False

    if not category and not support_channel and not unban and not ban and not feed_channel:
        category = await ctx.guild.create_category("Admin / Feedback", overwrites=overwrite_dict, reason="To log the admin and feedback events")

    # Bot Setup
    if discord.utils.get(category.channels, name="bot-setup"):
        botask = discord.utils.get(category.channels, name="bot-setup")
    else:
        botask = False

    return feed_channel, support_channel, support_channel_roles, ban, unban, botask
