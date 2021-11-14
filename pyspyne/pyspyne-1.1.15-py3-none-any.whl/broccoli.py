import requests, lxml, html
from bs4 import BeautifulSoup

class Broccoli():
    def __init__(self):
        pass

    class Organism:
        def __init__(self, sci_name=""):
            if sci_name == "":
                raise ValueError("Please include a scientific name")
            else:
                try:
                    fmtsn = " ".join(sci_name.split(" ")[:2])
                except:

                    # Get TSN Code of Organism
                    try:
                        fmtsn = " ".join(sci_name.split(" ")[:1])
                    except:
                        fmtsn = sci_name
                snfmt_response = requests.get(
                    f"https://www.itis.gov/ITISWebService/services/ITISService/searchByScientificName?srchKey={fmtsn}").text
                tsn_soup = BeautifulSoup(snfmt_response, "lxml")
                self.tsn = int(tsn_soup.find("ax21:tsn").text)

                # Get Taxonomy of Organism
                tax_response = requests.get(
                    f"https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value={self.tsn}#null").text
                tax_soup = BeautifulSoup(tax_response, "html.parser")
                self.common = tax_soup.select("td.datafield")[3].text.split("[")[0]
                textify = []
                for i in tax_soup.select("td.whiteboxhead table tr td.body"):
                    textify.append(html.unescape(i.text).replace("\xa0", " "))

                spaces_inc = True
                while spaces_inc:
                    try:
                        textify.remove(" ")
                    except ValueError:
                        spaces_inc = False

                tax_hier = []
                can_cont_lp = True
                for j in textify[8:]:
                    if can_cont_lp:
                        if j == "Direct Children:":
                            can_cont_lp = False
                        else:
                            tax_hier.append(j.split(" ")[-1])

                x = 0
                possible_kingdoms = ["Bacteria", "Archaea", "Protozoa", "Chromista",
                                     "Plantae", "Fungi", "Animalia", "Protista",
                                     "Eubacteria", "Archaebacteria", "Archezoa",
                                     "Monera", "Protoctista"]

                can_start = False
                tax_values = []
                counter = 0
                for b in tax_soup.select("td.whiteboxhead tbody tr td.datafield")[1:]:
                    i = b.text.split("\\")[0].split(" ")[0].split("\xa0")[0]
                    if i in possible_kingdoms:
                        can_start = True
                    if can_start and counter < len(tax_hier):
                        if i[0] != "-" and i[0] != " " and i[0] != "\xa0":
                            counter += 1
                            tax_values.append(i)
                    else:
                        can_start = False

                self.taxonomy = {}
                for y in tax_hier:
                    key = y.lower()
                    value = tax_values[tax_hier.index(y)]
                    if key == "species":
                        value = value.lower()
                    self.taxonomy[key] = value











