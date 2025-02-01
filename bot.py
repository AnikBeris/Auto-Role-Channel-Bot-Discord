import nextcord
from nextcord.ext import commands
import logging
import json

# Настроим логирование
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

# Загрузка конфигурации
with open("config.json", "r") as config_file:
    config = json.load(config_file)

TOKEN = config["TOKEN"]
GUILD_ID = config["GUILD_ID"]

intents = nextcord.Intents.default()
intents.message_content = True  
intents.members = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logging.info(f"✅ Бот {bot.user} успешно запущен!")
    guild = bot.get_guild(GUILD_ID)
    
    if guild is None:
        logging.error("❌ Ошибка: сервер не найден!")
        return

    await setup_roles(guild)
    await setup_channels(guild)

async def setup_roles(guild):
    """Создаёт роли на сервере, если они отсутствуют."""
    roles = {
        "🎮 PLAYER": {"permissions": nextcord.Permissions(send_messages=True, connect=True, speak=True, stream=True), "color": nextcord.Color.blue()},
        "💻 DEVELOPER": {"permissions": nextcord.Permissions(manage_channels=True, connect=True, speak=True, stream=True), "color": nextcord.Color.dark_purple()},
        "🛡 ADM": {"permissions": nextcord.Permissions(administrator=True), "color": nextcord.Color.red()},
        "🔨 MOD": {"permissions": nextcord.Permissions(kick_members=True, mute_members=True), "color": nextcord.Color.green()},
    }

    for name, details in roles.items():
        role = nextcord.utils.get(guild.roles, name=name)
        if not role:
            await guild.create_role(name=name, permissions=details["permissions"], color=details["color"])
            logging.info(f"✅ Создана роль: {name}")
        else:
            logging.info(f"🔹 Роль '{name}' уже существует.")

async def setup_channels(guild):
    """Создаёт категории и каналы."""
    categories = {
        "📚 INFO": ["❗-информация", "💬-чат"],
        "🔧 ADMIN": ["📀-участники", "🔞-системный", "🔧-админ-чат"],
    }

    for category_name, channels in categories.items():
        category = nextcord.utils.get(guild.categories, name=category_name) or await guild.create_category(category_name)
        for channel in channels:
            if not nextcord.utils.get(category.text_channels, name=channel):
                await category.create_text_channel(channel)
                logging.info(f"✅ Создан канал: {channel}")

bot.run(TOKEN)
