from data_scraper import *
def run_tradingview_search_scraper(link):
    Id="S7E43TQ6GEIMQGQ"
    response=scraper.run(link,id=Id)
    return response