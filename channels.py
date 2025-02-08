import nextcord
import logging

##############################################################################################################

async def create_category(guild, name):
    """Создаёт категорию, если её нет, и возвращает её объект."""
    category = nextcord.utils.get(guild.categories, name=name) or await guild.create_category(name)
    logging.info(f"✅ Категория '{name}' готова!")
    return category

####################################  Т Е К С Т О В Ы Й ##########################################################################

async def create_text_channel(category, name, topic, overwrites=None):
    """Создаёт текстовый канал с нужными правами."""
    guild = category.guild
    channel = nextcord.utils.get(category.text_channels, name=name)
    
    if not channel:
        channel = await category.create_text_channel(name, topic=topic, overwrites=overwrites or {})
        logging.info(f"✅ Создан канал: {name}")
    else:
        logging.info(f"🔹 Канал '{name}' уже существует.")
    
    return channel
#####################################  Ф О Р У М  #########################################################################

async def create_forum_channel(category, name, topic, overwrites=None):
    """Создаёт форумный канал с заданными параметрами."""
    guild = category.guild
    channel = nextcord.utils.get(category.channels, name=name, type=nextcord.ChannelType.forum)
    
    if not channel:
        channel = await category.create_forum_channel(name, topic=topic, overwrites=overwrites or {})
        logging.info(f"✅ Создан форумный канал: {name}")
    else:
        logging.info(f"🔹 Форумный канал '{name}' уже существует.")
    
    return channel

####################################  Г О Л О С О В О Й  ####################################################################

async def create_voice_channel(category, name, user_limit=0, overwrites=None):
    """Создаёт голосовой канал с нужными правами."""
    channel = nextcord.utils.get(category.voice_channels, name=name)
    
    if not channel:
        await category.create_voice_channel(name, user_limit=user_limit, overwrites=overwrites or {})
        logging.info(f"✅ Создан голосовой канал: {name}")
    else:
        logging.info(f"🔹 Голосовой канал '{name}' уже существует.")
        
##############################################################################################################

async def create_structure(guild):
    """Создаёт структуру ролей."""
    try:
        admin_role = nextcord.utils.get(guild.roles, name="🛡 ADM")
        mod_role = nextcord.utils.get(guild.roles, name="🔨 MOD")

        overwrites_info = {
            guild.default_role: nextcord.PermissionOverwrite(read_messages=True, send_messages=False),
            admin_role: nextcord.PermissionOverwrite(read_messages=True, send_messages=True),
            mod_role: nextcord.PermissionOverwrite(read_messages=True, send_messages=True),
        }

        overwrites_chat = {
            guild.default_role: nextcord.PermissionOverwrite(read_messages=True, send_messages=True),
            admin_role: nextcord.PermissionOverwrite(read_messages=True, send_messages=True, manage_channels=True),
            mod_role: nextcord.PermissionOverwrite(read_messages=True, send_messages=True),
        }

        overwrites_admin = {
            guild.default_role: nextcord.PermissionOverwrite(read_messages=False),
            admin_role: nextcord.PermissionOverwrite(read_messages=True, send_messages=True, manage_channels=True),
            mod_role: nextcord.PermissionOverwrite(read_messages=True, send_messages=True),
        }
        
##############################################################################################################

        category_ru_info = await create_category(guild, "📚 𝐑𝐔 | 𝐈𝐍𝐅𝐎 📚")
        await create_text_channel(category_ru_info, "❗┆информация", "🔴 Важная информация о ходе разработки 🔴", overwrites_info)
        await create_text_channel(category_ru_info, "💬┆чат", "Чат для общения", overwrites_chat)
        await create_voice_channel(category_ru_info, "🟢 ОСНОВНОЙ 🟢", 50)
        await create_voice_channel(category_ru_info, "🟡 ГОЛОС 🟡", 50)
    # Discord API не поддерживает создание форумных каналов (create_forum_channel) через библиотеку nextcord (или discord.py) в текущей версии
    # forum_ru = await category_ru.create_forum_channel("ideas-ru", topic="Оставляйте ваши идеи по игре")
    
        category_en_info = await create_category(guild, "📚 𝐄𝐍 | 𝐈𝐍𝐅𝐎 📚")
        await create_text_channel(category_en_info, "❗┆information", "🔴 Important information about development progress 🔴", overwrites_info)
        await create_text_channel(category_en_info, "💬┆chat", "General chat", overwrites_chat)
        await create_voice_channel(category_en_info, "🟢 BASIC 🟢", 50)
        await create_voice_channel(category_en_info, "🟡 VOICE 🟡", 50)

        category_admin = await create_category(guild, "🔴 Админы | Модеры 🔴")
        await create_text_channel(category_admin, "📀┆участники", "Список участников", overwrites_admin)
        system_channel = await create_text_channel(category_admin, "🔞┆системный", "Канал для системного вывода", overwrites_admin)
        await guild.edit(system_channel=system_channel)
        await create_text_channel(category_admin, "🔧┆админ-чат", "Чат для администраторов", overwrites_admin)
        await create_voice_channel(category_admin, "🔊┆админ-голос", 10, overwrites_admin)

        logging.info("✅ Вся структура сервера успешно создана!")
    except Exception as e:
        logging.error(f"❌ Ошибка при создании каналов: {e}")
