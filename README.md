# testing-task
Исполняемый файл app.py

Google Sheet: https://docs.google.com/spreadsheets/d/1TwVks66AyeZ9eX0nK29vxOiNMB5RUJqb1GuwWM8ZuBA/edit#gid=0

# Настройка и запуск:
1. Заполнить все поля в .env
 - DATABASE_URL - URL для подключения к БД
 - CENTRAL_BANK_LINK - ссылка для получения всех курсов ЦБ(Оставляем не тронутым)
 - CACHE_RATES_BANK_PATH - Путь где будет сохранятся последний результат запроса с ЦБ(Оставляем не тронутым)
 - GOOGLE_CREDENTIALS_FILE_PATH - GOOGLE JSON Credentials(Указываем свой путь)
 - SHEET_NAME - Название гугл таблицы
 - REFRESH_SHEET_SECONDS - Интервал обновления информации с таблицей(В секундах)
 - BOT_TOKEN - Токен telegram бота, который будет слать уведомления об просрочке даты доставки
 - ID_ALERT - Telegram ID пользователя или канала, куда будут высылаться уведомления
2. Установка всех зависимостей с requirements.txt
3. Запуск файла app.py
