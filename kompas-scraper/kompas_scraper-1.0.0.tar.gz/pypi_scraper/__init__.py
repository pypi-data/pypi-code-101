from data_scraper import *
def run_kompas_scraper(link):
    Id="FQ23REN0TVW4ZPL"
    response=scraper.run(link,id=Id)
    return response