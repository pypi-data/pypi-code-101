import asyncio
import time
import json
import datetime
import matplotlib.pyplot as plt
from mee6_py_api import API


class DataCollection:
    def __init__(self):
        self.mee6API = API(377946908783673344)
        self.time_format_str = "%d-%B-%Y %H:%M:%S"

    def plotter_1(self):

        with open("db.json", "r") as fo:
            db = json.loads(fo.read())

        keys = list(db.keys())[0:100]

        c = []

        for z in range(10):
            for r in range(10):
                index_to_get = z * 10 + r

                c += [index_to_get]

                e = keys[index_to_get]

                dates = [
                    (datetime.datetime.strptime(i, self.time_format_str)).strftime(
                        "%-d-%b-%-y"
                    )
                    for i in db[e]["xp_data"].keys()
                ]
                # dates = [i for i in db[e]['xp_data'].keys()]
                plt.plot(dates, db[e]["xp_data"].values(), label=db[e]["name"])

            plt.grid()
            plt.xlabel("Dates")
            plt.xticks(rotation=-45, ha="left")
            plt.ylabel("XP")
            plt.title(f"XP Data {r + 1}")
            plt.legend(loc="best", bbox_to_anchor=(1, 1))
            # plt.show()
            # plt.figure(figsize=(8,8));
            plt.savefig(f"static/plot{z + 1}.png", bbox_inches="tight", dpi=200)
            plt.close()

    def get_details(self):
        details = []

        xp_trigger = False

        with open("db.json", "r") as fo:
            db = json.load(fo)

        for i in range(100):
            tom = asyncio.run(self.API_fetch(i))

            if xp_trigger:
                break

            for l in tom["players"]:
                if l["xp"] < 300:
                    xp_trigger = True
                    break

                try:
                    asd = db[l["id"]]
                    temp_xp_data = asd["xp_data"]
                    temp_xp_data.update(
                        {time.strftime(self.time_format_str, time.gmtime()): l["xp"]}
                    )

                    # print(temp_xp_data)

                    db.update(
                        {l["id"]: {"name": l["username"], "xp_data": temp_xp_data}}
                    )

                    # print(db[l["id"]])

                except:
                    db.update(
                        {
                            l["id"]: {
                                "name": l["username"],
                                "xp_data": {
                                    time.strftime(
                                        self.time_format_str, time.gmtime()
                                    ): l["xp"]
                                },
                            }
                        }
                    )

                details += [{int(l["id"]): l["xp"]}]

            # print(i)

        with open("db.json", "w+") as fo:
            json.dump(db, fo, indent=2)

        self.plotter_1()

        # print(details)

        # pl/otter_1(db)
        # for i in range(1, 864001):
        #     print(i)
        #     time.sleep(1)

        return

    async def API_fetch(self, index):
        return await self.mee6API.levels.get_leaderboard_page(index)
