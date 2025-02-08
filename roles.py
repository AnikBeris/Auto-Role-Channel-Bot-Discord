import nextcord
import logging

async def create_roles(guild):
    """Создаёт роли на сервере (если их нет)."""
    roles = {
        "🎮 PLAYER": {
            "permissions": nextcord.Permissions(
                read_message_history=True,
                send_messages=True,
                create_public_threads=True,
                create_private_threads=True,
                connect=True,
                speak=True,
                stream=True
            ),
            "color": nextcord.Color.blue(),
            "hoist": True
        },
        "💻 DEVELOPER": {
            "permissions": nextcord.Permissions(
                manage_channels=True,
                manage_roles=True,
                manage_webhooks=True,
                manage_messages=True,
                ban_members=True,
                kick_members=True,
                view_audit_log=True,
                connect=True,
                speak=True,
                stream=True
            ),
            "color": nextcord.Color.dark_purple(),
            "hoist": True
        },
        "🛡 ADM": {
            "permissions": nextcord.Permissions(administrator=True),
            "color": nextcord.Color.red()
        },
        "🔨 MOD": {
            "permissions": nextcord.Permissions(
                manage_messages=True,
                mute_members=True,
                deafen_members=True,
                move_members=True,
                kick_members=True
            ),
            "color": nextcord.Color.orange()
        }
    }

    for role_name, role_data in roles.items():
        role = nextcord.utils.get(guild.roles, name=role_name)
        if not role:
            await guild.create_role(name=role_name, permissions=role_data["permissions"], color=role_data["color"])
            logging.info(f"✅ Создана роль: {role_name} (цвет: {role_data['color']})")
        else:
            logging.info(f"🔹 Роль '{role_name}' уже существует.")
