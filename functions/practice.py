def discount(amount, discount = 0):
    final_price = amount - amount * (discount / 100)
    return final_price


def order(item, *extra):
    print(item)
    print(extra)


def square(num):
    return num * num

def cube(num):
    return num * num * num

def operate(num, operation):
    result = operation(num)
    return result


def discount_10(amount):
    return amount * 0.9

def discount_30(amount):
    return amount * 0.7

def discount_60(amount):
    return amount * 0.4

def apply_discount(amount, discount):
    return discount(amount)

print(apply_discount(1000, discount_10))

print(__name__)
