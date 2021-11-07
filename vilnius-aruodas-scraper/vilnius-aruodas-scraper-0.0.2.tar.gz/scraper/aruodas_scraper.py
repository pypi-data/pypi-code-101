from requests_html import HTMLSession
import pandas as pd
import math


class AruodasScraper:
    '''
    AruodasScraper - scrapes house data from aruodas and returns a dataframe or csv file.

    Methods
    --------
    _num_results(num_houses:int):
        gets the maximum number of pages for the scraper to scrape
    scrape(num_houses, room_min, room_max):
        Loops through webpages and scrapes data off the aruodas website
    to_csv(df):
        used to save the dataframe to csv
    '''

    def __init__(self):
        self.s = HTMLSession()
        self.url = "https://en.aruodas.lt/butu-nuoma/vilniuje/"
        self.num_houses = None
        self.room_min = None
        self.room_max = None
        self.results = None

    def _num_result(self, num_houses):
        '''
        gets the maximum number of pages for the scraper to scrape
        :return: max_page or pages_to_scrape
        '''
        self.num_houses = num_houses
        url = self.url + f"?FRoomNumMin={self.room_min}&FRoomNumMax={self.room_max}"
        r = self.s.get(url)
        r.html.render(sleep=1, timeout=20)
        pages = r.html.find('a.page-bt')
        page_numbers = []
        for page in pages:
            if page.text != '»':
                page_numbers.append(page.text)
        max_page = int(page_numbers[-1])
        if self.num_houses > 25:
            pages_to_scrape = math.ceil(self.num_houses / 25)
        else:
            pages_to_scrape = 1
        if max_page < pages_to_scrape:
            return max_page
        return pages_to_scrape

    def scrape(self, num_houses=1, room_min=1, room_max=None):
        '''
        Loops through webpages and scrapes data off the aruodas website
        :param num_houses: number of houses to scrape
        :param room_min: minimum number of rooms
        :param room_max: maximum number of rooms
        :return: df
        '''
        self.room_min = room_min
        if room_max is None:
            self.room_max = room_min
        else:
            self.room_max = room_max
        max_num = self._num_result(num_houses)
        all_data = []
        for page_num in range(1, max_num + 1):
            links = []
            url = self.url + f"puslapis/{page_num}/?FRoomNumMin={self.room_min}&FRoomNumMax={self.room_max}"
            s = HTMLSession()
            r = s.get(url)
            r.html.render(sleep=1, timeout=90)
            link_container = r.html.find('td.list-adress')
            for item in link_container:
                links.extend(item.absolute_links)

            for link in links:
                page_data = {}
                page = s.get(link)
                page.html.render(sleep=1, scrolldown=6, timeout=20)

                name_tag = page.html.find("h1.obj-header-text", first=True)
                if name_tag is not None and name_tag.html:
                    name = name_tag.text.strip().replace('\n', '').replace(':', '')
                    addr = name.split(', ')
                    page_data['city'] = addr[0]
                    page_data['division'] = addr[1]
                    page_data['description'] = name
                    page_data['link'] = link

                    table = page.html.find('dl.obj-details', first=True)
                    raw = table.text.replace(':', '')
                    other_attrs = raw.split('\n')
                    i = 0
                    while i in range(len(other_attrs)):
                        page_data[other_attrs[i]] = other_attrs[i + 1]
                        i += 2

                    energy = page.html.find('span.energy-class-tooltip', first=True)
                    if energy is not None:
                        page_data['energy_class'] = energy.text

                    divs = page.html.find('div.statistic-info-cell-main')
                    if len(divs) != 0:
                        for div in divs:
                            feature = div.text
                            attr = feature.split("\n~ ")
                            page_data[attr[0]] = attr[1]
                all_data.append(page_data)
            print(f'Page {page_num} of {max_num} completed.')
        self.results = pd.DataFrame(all_data,
                                    columns=['city', 'division', 'description', 'link', 'House No.', 'Flat No.',
                                             'Area', 'Price per month', 'Number of rooms ', 'Floor', 'No. of floors',
                                             'Build year', 'Building type', 'Heating system', 'energy_class',
                                             'Nearest kindergarten', 'Nearest educational institution',
                                             'Nearest shop', 'Public transport stop'])
        print(f'{len(all_data)} results scarped!')
        return self.results

    def to_csv(self, df: pd.DataFrame) -> None:
        '''
        used to save the dataframe to csv
        :param df: dataframe to be converted to csv
        :return: none
        '''
        df.to_csv(f'aruodas_{self.room_min}_{self.room_max}.csv', index=False)
        print(f'aruodas_{self.room_min}_{self.room_max}.csv file saved to folder')
        return

    def scrape_to_csv(self, num_houses=1, room_min=1, room_max=None):
        '''
        used to scrape and save the data to csv
        :param num_houses:
        :param room_min:
        :param room_max:
        :return: none
        '''
        try:
            df = self.scrape(num_houses, room_min, room_max)
            return self.to_csv(df)
        except Exception as ex:
            print('Unable to scrape due to error')
            raise ex
