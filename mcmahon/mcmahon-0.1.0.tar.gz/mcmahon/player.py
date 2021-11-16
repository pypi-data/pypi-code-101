class Player:
    def __init__(
        self,
        last_name: str,
        first_name: str,
        country: str,
        rating: int,
        start_mms: int = 0,
        absent_rounds: set[int] = None,
        bye_rounds: set[int] = None,
        is_final: bool = False,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.country = country
        self.rating = rating
        self.start_mms = start_mms
        self.absent_rounds = absent_rounds or set()
        self.bye_rounds = bye_rounds or set()
        self.is_final = is_final

    def __eq__(self, other: "Player"):
        return self.key == other.key

    @property
    def key(self):
        return f"{self.country}_{self.last_name}_{self.first_name}".upper()

    @property
    def rank(self) -> int:
        return self.rating // 100 - 21

    def bye_x2(self, rn: int) -> int:
        points = len([r for r in self.bye_rounds if r <= rn])
        return points * 2

    def absent_x2(self, rn: int) -> int:
        points = len([r for r in self.absent_rounds if r <= rn])
        return points - points % 2
