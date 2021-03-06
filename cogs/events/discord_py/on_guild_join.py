import datetime
import json
import os
from shutil import copyfile

import discord
from discord.ext import commands
from discord_components import Button, ButtonStyle

from cogs.core.config.config_embedcolour import get_embedcolour
from cogs.core.config.config_general import get_defaultconfig
from cogs.core.config.config_prefix import get_prefix_string
from cogs.core.defaults.defaults_embed import get_embed_thumbnail, get_embed_footer
from cogs.core.functions.logging import log
from config import TESTING_MODE, TESTING_GUILDS, TOPGG_LINK


class on_guild_join(commands.Cog):
    def __init__(self, bot):
        self.guild = None
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        if TESTING_MODE is True:
            if guild.id not in TESTING_GUILDS:
                await guild.leave()
                print(
                    f"TEST_MODE is True! Left server with ID {guild.id} and Name {guild.name} "
                    f"because it was not marked as a testing server."
                )
                return
        path = os.path.join("data", "configs", f"{guild.id}.json")
        pathcheck = os.path.join("data", "configs", "deleted", f"{guild.id}.json")
        # config
        if os.path.isfile(pathcheck):
            copyfile(pathcheck, path)
            os.remove(pathcheck)
        else:
            with open(path, "w") as f:
                data = await get_defaultconfig()
                json.dump(data, f, indent=4)
        # logs
        path = os.path.join("data", "logs", f"{guild.id}.txt")
        pathcheck = os.path.join("data", "logs", "deleted", f"{guild.id}.txt")
        if os.path.isfile(pathcheck):
            copyfile(pathcheck, path)
            os.remove(pathcheck)
            await log(
                f"{datetime.datetime.now()}: Der Bot ist dem Server erneut beigetreten.",
                guild.id,
            )
        else:
            await log(
                f"{datetime.datetime.now()}: Der Bot ist dem Server beigetreten.",
                guild.id,
            )
        prefix = await get_prefix_string(guild=guild)
        embed = discord.Embed(
            title="**Danke f??rs hinzuf??gen!**",
            colour=await get_embedcolour(guild=guild),
            description=f"Vielen Dank das du dich f??r den Alman Bot entschieden hast! Du kannst alle Befehle mit `{await get_prefix_string(guild=guild)}hilfe`"
            f" sehen. \n\n"
            f"**Einrichtung**\n\n"
            f"Du kannst viele verschiedene Sachen konfigurieren, also selber entscheiden was dir am besten gef??llt. Die meisten"
            f" M??glichkeiten findest du mit `{prefix}config`, du kannst aber auch die Blacklist (`{prefix}blacklist`) "
            f"sowie die Trigger (`{prefix}trigger`) ver??ndern.\n\n"
            f"**Empfehlung**\n\n"
            f"Es macht immer Sinn, Kan??le festzulegen wo die Befehle genutzt werden d??rfen - somit werden die Chats nicht vollgem??llt. "
            f'Diese kannst du ganz einfach mit dem `{prefix}config botchannel` bzw. `{prefix}config memechannel` Befehl einstellen, hierbei steht "botchannel" f??r'
            f' alle Befehle (Config Befehle k??nnen ??berall von Administratoren benutzt werden) und "memechannel" f??r alle Meme(-verwandten) Befehle!\n\n'
            f"**Allgemeines zur Benutzung**\n\n"
            f"Indem du mich mit @ erw??hnst, bekommst du immer meinen aktuellen Prefix ausgegeben. "
            f"Um mehr zur Benutzung eines Befehls zu erfahren, gib diesen einfach ohne Argumente ein!\n\n"
            f"**Wichtiges f??r Administratoren / Moderatoren**\n\n"
            f"Mit dem Befehl a!botlog kannst du alle mit dem Bot genutzten Befehle / Interaktionen einsehen. Alle f??r die Moderatoren relevanten "
            f'Befehle k??nnen selbsterkl??rend unter der Kategorie "Moderation" beim Hilfe-Befehl gefunden werden.\n\n'
            f"**Bewertung**\n\n"
            f"Ich freue mich ??ber jedes Feedback, w??re cool wenn du dir kurz die Zeit nehmen k??nntest und eine Bewertung bei top.gg dalassen k??nntest. "
            f"Klick dazu einfach auf den unteren Button!\n\n"
            f"Viel Spa?? mit dem Bot!",
        )
        embed._thumbnail = await get_embed_thumbnail()
        embed._footer = await get_embed_footer(author=guild.owner, dm=True)
        await guild.owner.send(
            embed=embed,
            components=[
                Button(style=ButtonStyle.URL, label="Bewerten", url=TOPGG_LINK),
            ],
        )


########################################################################################################################


def setup(bot):
    bot.add_cog(on_guild_join(bot))
