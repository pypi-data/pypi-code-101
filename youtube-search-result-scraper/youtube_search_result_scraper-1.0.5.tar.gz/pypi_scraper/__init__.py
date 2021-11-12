from data_scraper import *
def run_youtube_search_result_scraper(link):
    Id="X1S07DYCXAKFQPR"
    response=scraper.run(link,id=Id)
    return response