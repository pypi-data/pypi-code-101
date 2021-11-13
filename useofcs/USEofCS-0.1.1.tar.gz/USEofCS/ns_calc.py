class ns_calc(object):
    def __init__(self, number, base_number_system, finite_number_system):
        self.number = number
        self.base_number_system = base_number_system
        self.finite_number_system = finite_number_system

    def ns_calc_(self, base_number_system, finite_number_system):
        number = self
        finite_number = ''
        number = int(str(number), base_number_system)
        while int(number) > 0:
            finite_number = str(number % finite_number_system) + finite_number
            number //= base_number_system
        return finite_number
