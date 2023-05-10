from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from knitportal.db.database import get_db
from knitportal.scrapers.wollplatz import WollPlatzScraper

router = APIRouter()


@router.post("/scrape", tags=["scrape"])
async def scrape_products(
    background_tasks: BackgroundTasks, db_session: Session = Depends(get_db)
):
    scrapers = [WollPlatzScraper]

    for scraperClass in scrapers:
        scraper = scraperClass(db_session)
        background_tasks.add_task(scraper.start_scrape)
        # background_tasks.add_task(scraper.scrape_pages)

    return {"message": "Scraping started"}
