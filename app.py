from core.database import database, queries
from core.scraper.scraper import MainScraper

def main() -> None:
    engine = database.create_database()
    Session = database.create_session(engine)
    MainScraper(Session()).checker()
main()