# Запуск бота

## Python

```bash
# Создание и активация виртуального окружения (опционально)
python -m venv .venv
source .venv/bin/activate
```

```bash
# Устновка зависимостей
pip install -r requirements.txt
```

```bash
# Запуск (нужно заменить BOT_TOKEN на токен бота)
python app.py BOT_TOKEN 
```

## С .env

Создайте .env файл где напишите токент вашего бота

```env
BOT_TOKEN=1234567890:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

```bash
# И запустите
python app.py
```