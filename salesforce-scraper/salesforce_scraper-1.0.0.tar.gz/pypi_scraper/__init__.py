from data_scraper import *
def run_salesforce_scraper(link):
    Id="AVP3W8HKEF67DN6"
    response=scraper.run(link,id=Id)
    return response