from data_scraper import *
def run_notion_scraper(link):
    Id="27I5J6QP4PSXIKW"
    response=scraper.run(link,id=Id)
    return response