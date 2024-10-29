
def tax_calculator(value1):
    tax = round(value1 * 0.06, 2)
    total = round(value1 + tax, 2)
    return value1, tax, total
