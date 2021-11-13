def ns_calc(number, base_number_system, finite_number_system):
    finite_number = ''
    number = int(str(number), base_number_system)
    while int(number) > 0:
        finite_number = str(number % finite_number_system) + finite_number
        number //= base_number_system
    return finite_number
