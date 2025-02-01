[English](/README.md) | [Русский](/README.ru_RU.md)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./media/logo-light.png">
    <img alt="Project Logo" src="./media/logo-light.png">
  </picture>
</p>

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-blue?style=flat&logo=github)](https://github.com/AnikBeris)
[![License](https://img.shields.io/badge/License-purple?style=flat&logo=github)](https://github.com/AnikBeris/AutoRoleChannelBot/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/your-repo?style=flat&logo=github&label=Звёзды&color=orange)](https://github.com/AnikBeris)

</div>

# Discord БОТ для создания структуры канала, так же создание ролей.

> **Отказ от ответственности:** Этот проект предназначен только для личного обучения и общения. Пожалуйста, не используйте его в незаконных целях и не применяйте в производственной среде.

**Если этот проект оказался полезным для вас, вы можете оценить его, поставив звёздочку.**:star2:

<p align="left">
  <a href="https://buymeacoffee.com/mhsanaei" target="_blank">
    <img src="./media/buymeacoffe.png" alt="Image">
  </a>
</p>

Пожертвования горячо приветствуются, какими бы маленькими они ни были, и большое спасибо. 😌

- **Bitcoin (BTC)** - `1Dbwq9EP8YpF3SrLgag2EQwGASMSGLADbh`
- **Ethereum (ERC20)** - `0x22258ea591966e830199d27dea7c542f31ed5dc5`
- **Binance Smart Chain (BEP20)** - `0x22258ea591966e830199d27dea7c542f31ed5dc5`
- **Solana (SOL)** - `yYYXsiVTzsvfvsMnBxfxSZEWTGytjAViE2ojf3hbLeF`



## Возможности
- Автоматически создаёт роли с определёнными правами и цветами
- Назначает специальные привилегии ролям "Developer" и "Player"
- Создаёт структурированные категории и каналы
- Поддерживает отображение ролей отдельно в списке участников

## Установка

```bash
# Клонируем репозиторий
git clone https://github.com/your-repo.git
cd your-repo

# Устанавливаем зависимости
pip install -r requirements.txt

# Запускаем бота
python bot.py
```

## Права Ролей

| Название Роли | Разрешения |
|--------------|-------------|
| 🎮 PLAYER   | Чтение истории сообщений, отправка сообщений, создание тредов, подключение, разговор, трансляция |
| 💻 DEVELOPER | Управление каналами, управление ролями, просмотр журналов аудита, подключение, разговор, трансляция |
| 🛡 ADM      | Полные права администратора |
| 🔨 MOD      | Управление сообщениями, отключение звука/глушение/перемещение участников, кик участников |

## Настройка БОТА

### 1. Создание Discord БОТА
1. Перейдите в [Портал Разработчиков Discord](https://discord.com/developers/applications).
2. Нажмите "New Application", введите название и сохраните.
3. Перейдите в "Bot" -> "Add Bot" -> Подтвердите.
4. Скопируйте **Токен** бота (он понадобится позже).
5. Включите **Привилегированные Интенты** (Присутствие, Участники сервера и Контент сообщений).

### 2. Получение GUILD_ID
1. Включите режим разработчика в Discord (Настройки -> Расширенные -> Режим разработчика).
2. Кликните правой кнопкой по названию сервера и выберите "Копировать ID". Это ваш `GUILD_ID`.

### 3. Добавление бота на сервер
1. Перейдите в **OAuth2** -> "URL Generator".
2. Выберите **bot** и **applications.commands**.
3. В разделе **Права Бота** выберите:
   - Управление ролями, управление каналами, чтение сообщений, отправка сообщений, подключение, разговор.
4. Скопируйте сгенерированную ссылку и вставьте её в браузер.
5. Выберите сервер и авторизуйте бота.

### 4. Настройка и запуск
1. Откройте `config.json` и добавьте ваш **TOKEN** и **GUILD_ID**.
2. Запустите бота:
   ```bash
   python bot.py
   ```
3. УСПЕХ! Бот сам создаст роли и каналы!

## Лицензия
Этот проект распространяется по [MIT License](https://github.com/your-repo/blob/main/LICENSE).

---

Для детальной документации ознакомьтесь с [Английским README](/README.md) или [Русским README](/README.ru_RU.md).

