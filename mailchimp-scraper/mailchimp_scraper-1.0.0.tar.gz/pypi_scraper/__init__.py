from data_scraper import *
def run_mailchimp_scraper(link):
    Id="57HYFHR6SIQVFYW"
    response=scraper.run(link,id=Id)
    return response