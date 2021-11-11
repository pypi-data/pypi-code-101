from data_scraper import *
def run_spotify_scraper(link):
    Id="3213Z7RIH1EI1JP"
    response=scraper.run(link,id=Id)
    return response