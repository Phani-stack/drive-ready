'''
    > In python function, there is no datatype for arguments
      and return type, it figure outs at runtime.

    > default arguments in python are used to choose the
      default value when the function doesn't have any
      arguments. Default is always at the end of function

    >
'''

# function
def add1(a, b):
    return a + b

# default arguments
def add2(a, b = 0):
    return a + b

# defined functions
def add3(a: int, b: int):
    return int(a + b)

# variable lenght arguments
def add4(a, *b):
    return a, b

# key:word length argument
def person1(name, age):
    print(name, age)

# person1(age = 10, name="John")

# key:word length arguments
def person2(name, **kwlargs):
    print("Name:", name)
    for k, v in kwlargs.items():
        print(k, ":" , v)

# person2("Phani", age=19, loc="amp", gpa=8.7)

def place_order(item, quantity = 1, *toppings, **details):
    # print(type(toppings))
    # print(type(details))

    print("Item:", item)
    print("Quantity:", quantity)
    print("Toppings:", list(toppings))

    # for topping in toppings:
    #     print(topping, end=", ")
    # print()

    for k, v in details.items():
        print(k, ":", v)

    return generate_order(item, quantity, toppings, details)


def generate_order(item, quantity, *toppings, **details):
    return {
        "item" : item,
        "quantiy": quantity,
        "topping": list(toppings),
        "details": details
    }

# print(place_order("Pizza", 2, "extra butter", "seasoning", address="x street", pincode=533277))


# global and local variables

a = 10
def display():
    # global a
    globals()['a'] = 30
    a = 20
    # print(a)
display()
# print(a)


# higher order functions
def square(num: int):
    return num * num

def cube(num: int):
    return num * num * num

def operate(num, operation):
    return operation(num)

def operate(nums, operation):
    result = []
    for num in nums:
        result.append(operation(num))
    return result

result = operate(["1", "2", "3", "4"], int)
# print(result)

def discount_10(amount):
    return amount * 0.9

def discount_30(amount):
    return amount * 0.7

def discount_60(amount):
    return amount * 0.4

def apply_discount(amount, discount):
    return discount(amount)

# print(apply_discount(1000, discount_60))


# lambda function
power = lambda num, n : pow(num, n)
# print(power(2, 4))


# map, filter, reduce
def even(num):
    return num % 2 == 0

def add_20(num):
    return num + 20

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(even, lst))
adds = list(map(add_20, lst))
# print(adds)

ages = {
    "Surya": 20,
    "Rahul": 19,
    "Phani": 19,
    "Getha": 20
}

def display_pep(value):
    print(value)

map(display_pep, ages)
