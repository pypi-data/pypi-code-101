from .boredom import Boredom


class Alliances(Boredom):
    def __init__(self, **kwargs):
        super().__init__("alliances", **kwargs)

        self.length = "aa_count"
        self.total = [("total_aa_score", 7, float)]


class Cities(Boredom):
    def __init__(self, **kwargs):
        super().__init__("cities", **kwargs)

        self.length = "city_count"
        self.total = [
            ("total_infrastructure", 5, float),
            ("total_land", 7, float),
            ("oil_pp", 8, int),
            ("coal_pp", 10, int),
            ("nuclear_pp", 11, int),
            ("coal_mines", 12, int),
            ("oil_wells", 13, int),
            ("uranium_mines", 14, int),
            ("iron_mines", 15, int),
            ("lead_mines", 16, int),
            ("bauxite_mines", 17, int),
            ("farms", 18, int),
            ("supermarkets", 23, int),
            ("banks", 24, int),
            ("shopping_malls", 25, int),
            ("stadiums", 26, int),
            ("oil_refineries", 27, int),
            ("aluminum_refineries", 28, int),
            ("steel_mills", 29, int),
            ("munitions_factories", 30, int)
        ]


class Nations(Boredom):
    def __init__(self, **kwargs):
        super().__init__("nations", **kwargs)

        self.length = "nation_count"
        self.total = [
            ("total_score", "score", float),
            ("total_population", "population", int),
            ("beige", "beige_turns_remaining", int),
            ("soldiers", "soldiers", int),
            ("tanks", "tanks", int),
            ("aircraft", "aircraft", int),
            ("ships", "ships", int),
            ("missiles", "missiles", int),
            ("nukes", "nukes", int),
        ]
        self.match = [
            ("gray", 12, "gray"),
            ("blitzkrieg", 30, "Blitzkrieg"),
        ]

    def run(self, force_new=False, ignore=True):
        super().run(force_new, ignore)


class Trades(Boredom):
    def __init__(self, **kwargs):
        super().__init__("trades", **kwargs)

    def spec_collection(self, data: list[dict], ignore=False):
        self.collected = {}

        rss = [
            "credits",
            "food",
            "coal",
            "oil",
            "uranium",
            "lead",
            "iron",
            "bauxite",
            "gasoline",
            "munitions",
            "steel",
            "aluminum",
        ]

        sell = "%s_sell_total"
        buy = "%s_buy_total"
        max_buyer = {}
        max_seller = {}
        
        for resource in rss:
            self.collected[sell %resource] = 0
            self.collected[buy %resource] = 0

        for line in data:
            resource = rss.find(line["resource"])
            if accepted == "1":
                continue
            if resource == -1:
                raise KeyError
            self.collected[sell %rss[resource]] += quantity*price*(line["buy_or_sell"]=="sell")
            self.collected[buy %rss[resource]] += quantity*price*(line["buy_or_sell"]=="buy")


class Wars(Boredom):
    def __init__(self, **kwargs):
        super().__init__("wars", **kwargs)
        self.total = [
            ("infra_destroyed", 32, float),
            ("infra_destroyed", 33, float),
            ("money_looted", 34, float),
            ("money_looted", 35, float),
            ("soldiers_killed", 36, int),
            ("soldiers_killed", 37, int),
            ("tanks_destroyed", 38, int),
            ("tanks_destroyed", 39, int),
            ("aircraft_destroyed", 40, int),
            ("aircraft_destroyed", 41, int),
            ("ships_destroyed", 42, int),
            ("ships_destroyed", 43, int),
            ("missiles_used", 44, int),
            ("missiles_used", 45, int),
            ("nukes_used", 46, int),
            ("nukes_used", 47, int)
        ]
        self.match = [
            ("raid_count", "war_type", "raid"),
            ("attrition_count", "war_type", "attrition"),
            ("ordinary_count", "war_type", "ordinary")
        ]
