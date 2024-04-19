from handlers.buy import buy_rt
from handlers.start import start_rt
from handlers.close import close_rt
from handlers.help import help_rt
from handlers.refer import refer_rt
from handlers.sell_manage import sellmng_rt
from handlers.alert import alert_rt
from handlers.wallet import wallet_rt
from handlers.settings import settings_rt
from handlers.pin import pin_rt
from handlers.refresh import refresh_rt
from utils.config import dp, bot
import logging
import asyncio
import sys


async def main() -> None:
    dp.include_router(start_rt)
    dp.include_router(buy_rt)
    dp.include_router(close_rt)
    dp.include_router(sellmng_rt)
    dp.include_router(help_rt)
    dp.include_router(refer_rt)
    dp.include_router(alert_rt)
    dp.include_router(wallet_rt)
    dp.include_router(settings_rt)
    dp.include_router(pin_rt)
    dp.include_router(refresh_rt)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())