#Global vs Local Variables
'''
a variable made inside a function is local -> it is born when function 
starts and dies when function returns
A variable made outside is global -> it is lives through out the
program
'''

# a = 15 #global
# def doSomething():
    
#     globals()['a'] = 10
   
#     a = 20 
#     print("inside : " , a)
# doSomething()
# print("outside : ",a)

#higher order function

def square(num1):
    return num1 * num1 

def cub(num1):
    return num1* num1 * num1 


def operation(a , oper):
    print(oper(a))

operation(5,square)
operation(4,cub)

#real world
#quickbite pricing 

def no_discount(total):
    return total 
def flat_50_off(total):
    return total - 50 
def ten_percent_off(total):
    return total * 0.9
def checkout(total, discount_rule):
    final = discount_rule(total)
    print("Bill to pay : " , final)

checkout(500,no_discount)
checkout(1000,flat_50_off)
checkout(10000,ten_percent_off)