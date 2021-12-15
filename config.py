import discord

OWNER_IDS = [879416069440303196]

# BASIC THINGS

BOT_NAME = "Death-Alman"
DEFAULT_PREFIX = ["a!"]
DEFAULT_EMBEDCOLOUR = 0x41A13A
DEFAULT_BUTTONCOLOUR = "green"  # green, red, blue, grey
DEFAULT_MEMESOURCE = "memes"
ICON_URL = "https://cdn.discordapp.com/attachments/884553838839885827/918583545230950410/Download_2.jpg"
THUMBNAIL_URL = "https://cdn.discordapp.com/attachments/884553838839885827/918583545230950410/Download_2.jpg"
FOOTER = ["für ", " | Entwickelt von ", " | Prefix "]
STATUS = discord.Status.online
ACTIVITY_LIST = [
    "Death-Zone",
    "Einstellbaren Prefix",
    "Viele Einstellungen",
    "in {guild_count} Servern",
    "mit {user_count} Nutzern",
    "Entwickelt von SaTiVa#8442, SimsumMC#2248",
]
DEFAULT_LVLUP_MESSAGE = (
    "Herzlichen Glückwunsch, du bist auf Level {level} aufgestiegen! 🎉"
)
DEFAULT_LVLUP_MODE = "same"  # dm , channel, same
# guild_count, user_count, developer_names
DEFAULT_LEVELLING_COOLDOWN = 3
DEFAULT_LEVELLING_XP_PER_MESSAGE = 5

SUGGESTION_CHANNEL_ID = 919335907029577749

# Other Thumbnails

COIN_HEAD = "https://cdn.discordapp.com/attachments/851853486948745246/851853519497199671/kopf.png"
COIN_NUMBER = "https://cdn.discordapp.com/attachments/851853486948745246/851853652002996224/zahl.png"
SSP = "https://cdn.discordapp.com/attachments/645276319311200286/803373963316953158/stp.png"
CUBE = "https://cdn.discordapp.com/attachments/645276319311200286/803550939112931378/wurfelv2.png"
GIVEAWAY = "https://media.discordapp.net/attachments/851853486948745246/897609523911614534/1f389.png"

# TOKEN

DISCORD_TOKEN = (
      # to run the bot
)
STATCORD_TOKEN =   # Optional, for bot stats ->
REDDIT_APP = {  # for the memes command, just create an application on reddit
    
ABSTRACT_API_KEY = "your key" # required for Screenshot Command


class lavalink:  # for music module
    host = "lava.link"
    port = "80"
    rest_uri = "http://lava.link:80"
    passwort = BOT_NAME
    identifier = BOT_NAME
    region = "europe"


# DEFAULTS | ⚠️ DANGER ZONE ⚠️ -> anything wrong here can cause crashes *while* running (when receiving messages)

DEFAULT_TRIGGER_LIST = ["Death-Fun", "SaTiVa"]
DEFAULT_TRIGGER = {
    "Death-Fun": "Hey, Ich bins!",
    "SaTiVa": "Das ist der komische RGB Fan, der für meine Existenz verantwortlich ist...",
}

""" Example for more Triggers

DEFAULT_TRIGGER_LIST = ["Alman Bot", "Käse"]
DEFAULT_TRIGGER = {
    "Alman Bot": "Hey, Ich bins!",
    "Käse": "Käse ist echt lecker LOL"
}

"""
# Messages

WRONG_CHANNEL_ERROR = (
    "Dieser Befehl kann in diesem Chat nicht genutzt werden. "
    "Hier ist eine Liste in denen der Befehl funktioniert: "
)

MISSING_PERMISSIONS_BUTTON_ERROR = (
    "Diese Nachricht gehört dir nicht! Nutz den Befehl bitte selbst!"
)

CALCULATING_ERROR = "Fehler beim berechnen!"

DEFAULT_BROADCAST_MESSAGE = "Hinweis: _Du erhälst diese Nachricht da du diesen Bot auf einem deiner Server nutzt._"

# Colour Configuration | ⚠️ DANGER ZONE ⚠️ -> anything wrong here can cause crashes *while* running (at any action)

EMBEDCOLOUR_CODES = {
    "rot": 0xA80000,
    "hellrot": 0xF00000,
    "gelb": 0xF3D720,
    "hellblau": 0x2FA5EE,
    "blau": 0x573CE2,
    "hellgrün": 0x20DE12,
    "grün": 0x41A13A,
    "hellorange": 0xE29455,
    "orange": 0xE36D0D,
    "schwarz": 0x000000,
    "hellgrau": 0x999494,
    "grau": 0x444141,
    "weiß": 0xFFFFFF,
    "dunkellila": 0x852598,
    "lila": 0xB144E4,
    "pink": 0xE114BC,
    "random": "random",
    "rainbow": "rainbow",
}

EMBEDCOLOURS_SUPPORTED = [
    "rot",
    "hellrot",
    "hellblau",
    "blau",
    "hellgrün",
    "grün",
    "hellorange",
    "orange",
    "schwarz",
    "hellgrau",
    "grau",
    "weiß",
    "dunkellila",
    "lila",
    "pink",
    "rainbow",
    "random",
    "gelb",
]

# Developer Settings | ⚠️ DANGER ZONE ⚠️ -> anything wrong here can cause the bot to instant leave your server and misfunctions

TESTING_MODE = False  # only allowing Servers to join GUILDS with ID in TESTING_GUILDS, removes guild owner bypasses and more
TESTING_GUILDS = []

WRONG_CHANNEL_ERROR_DELETE_AFTER = 5
BLACKLIST_DELETE_AFTER = 5

BLACKLIST_IGNORE = ["blacklist", "qr", "broadcast"]

# © github.com/SimsumMC | You're not allowed to change the following parts without my (github.com/SimsumMC) permission ⚠️

BOT_MAIN_DEVELOPER = "SaTiVa#8442, SimsumMC#2248"
BOT_DEVELOPERLIST = ["SaTiVa#8442"]
INVITE_LINK = "https://discord.com/oauth2/authorize?client_id=906517819087265852&scope=bot&permissions=2620914775"
DISCORD_LINK = "https://discord.gg/a7WvZdxu7X"
WEBSITE_LINK = "https://discord.gg/a7WvZdxu7X"
GITHUB_LINK = "-x-"
TOPGG_LINK = "-x-"
ABOUT = f"""
Egal ob Moderation, einfach ein Lächeln aufs Gesicht zaubern, eine Matheaufgabe lösen oder den Avatar von einem Nutzer 
klauen - ich helfe dir wo ich nur kann! Penibel wie ein Deutscher bin ich natürlich auch...
        """

BANNER = """
     **      **                                    ******              **    
    ****    /**                                   /*////**            /**    
   **//**   /** **********   ******   *******     /*   /**   ******  ******  
  **  //**  /**//**//**//** //////** //**///**    /******   **////**///**/   
 ********** /** /** /** /**  *******  /**  /**    /*//// **/**   /**  /**    
/**//////** /** /** /** /** **////**  /**  /**    /*    /**/**   /**  /**    
/**     /** *** *** /** /**//******** ***  /**    /******* //******   //**   
//      // /// ///  //  //  //////// ///   //     ///////   //////     //    
        """
