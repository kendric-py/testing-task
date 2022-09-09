import asyncio

from core.database import database, queries
from core.scraper.scraper import MainScraper





async def main() -> None:
    engine = database.create_database()
    Session = database.create_session(engine)
    MainScraper(Session()).checker()


asyncio.run(main())