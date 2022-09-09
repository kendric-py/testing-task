from aiogram import Bot
from .. import config


async def send_alert(orders_id: list[int]) -> None:
    bot = Bot(token=config.BOT_TOKEN, parse_mode='html')
    await bot.send_message(
        config.ID_ALERT,
        f'<b>🔔 Уведомление</b>\
        \nУ следующих заказов, истек срок поставки:\n<code>{orders_id}</code>'
    )
    return


