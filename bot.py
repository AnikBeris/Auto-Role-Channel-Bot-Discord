import nextcord
from nextcord.ext import commands
import logging
import json
from roles import create_roles
from channels import create_structure

# Настроим логирование
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

# Загружаем конфигурацию
with open("config.json", "r") as config_file:
    config = json.load(config_file)

TOKEN = config["TOKEN"]
GUILD_ID = config["GUILD_ID"]

intents = nextcord.Intents.default()
intents.message_content = True  # Поддержка команд
intents.members = True  # Доступ к участникам

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logging.info(f"\u2705 Бот {bot.user} успешно подключился к Discord!")
    guild = bot.get_guild(GUILD_ID)
    
    if guild is None:
        logging.error("\u274C Ошибка: сервер не найден!")
        return
    
    await create_roles(guild)  # Создаём роли
    await create_structure(guild)  # Создаём категории и каналы

# Запускаем бота
bot.run(TOKEN)
