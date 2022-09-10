from aiogram import Bot
from .. import config
bot = Bot(token=config.BOT_TOKEN, parse_mode='html')

async def send_alert(orders_id: str) -> None:
    """Создаем бота, токен берется из конфига, отправляем полученное сообщение"""
    await bot.send_message(
        config.ID_ALERT,
        f'<b>🔔 Уведомление</b>\
        \nУ следующих заказов, истек срок поставки:\n<code>{orders_id}</code>'
    )
    return


