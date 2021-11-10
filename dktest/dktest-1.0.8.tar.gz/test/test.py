from data_scraper import *
import json
link1='https://www.eshop.in/search?q=elaichi&options%5Bprefix%5D=last'
link2='https://www.eshop.in/search?q=green&options%5Bprefix%5D=last'
response=scraper.train(link1,link2)
print(response)
response=scraper.run(link1,id=response["id"])
#response=scraper.run(link1,id="NT554AIKII0QU7P")
print("response keys",response.keys())
with open ("data.json","w",encoding="utf-8") as d:
    d.write(json.dumps(response,sort_keys=False,indent=4))