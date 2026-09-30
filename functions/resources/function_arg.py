'''
python
Base Python (data types , oper , conditional , control , list)
dictionar, set , tuple , strings , functions

Functions 


python OOPS 


Quickbite --> App (swiggy)
class --> properties and behiv 
(data , function/methods)
'''
# def add(a ,b):
#     return a + b 

# res = add(4,5)
# print(res)

#Quiclbite deliveray fee
#20 
# import math
# math.sqrt(20)
# def deliveray_fee(distance_km):
#     if(distance_km <= 3):
#         return 20
#     return 20 + (distance_km - 3) * 8

# print(deliveray_fee(3))
# print(deliveray_fee(6))

#Arguments

#default Argument
# def add(num1 ,num3, num2 = 0  ): #default 
#     return num1+num2

# res = add(2,10) #actual argument



#variable length argument ->*

# def add(num1,*num2):
#     res = num1 
#     for i in num2:
#         res+=i 
#     return res

# add(1,2,3,4)

#keyword 

# def person(name,age):
#     print("Name : ", name)
#     print("Age : ", age)

# person(age = 30,name = "ram")


#keyword variable length --> **
#key value dictionary
#{'age': 30, 'loc': 'kakinada', 'tech': 'Python'}
   
def person(name, **kwlarg):
    print("Name : ",name)
    for k , v in kwlarg.items():
        print(k, " : " , v)

person("Ashok" ,age = 30 , loc = "kakinada" , tech = "Python" )


#real time
#place order -> iteam (address, coupon, toppings, )

def place_order(item, qty = 1 , *toppings, **details):
    pass

place_order("Pizza", 2 , "extra chees" , "seasoning", address = "Flat 4B", coupon = "code123")