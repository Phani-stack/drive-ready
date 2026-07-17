#Anonymous Functions Using Lambda
# def fun(n): 
#     return n * n 

# res = fun(10)

# fun = lambda n : n * n 

# res = fun(5)
# print(res)

# nums = [1,2,3,4,5,6,7,8]

# fun = lambda n : n % 2 == 0
# evens = list(filter(fun,nums))
# print(evens)



menu = [{"name" : "Paneer Tikka", "price" : 280 , "veg":True},
        {"name" : "chicken Biriyani" , "price" : 220 , "veg" : False}]
#sort by price

# menu.sort(key = lambda item : item['price'])
# print(menu)

#[{x,y},{a,b},{c,d}]
list = [[2,1,3],[4,3,1],[4,6,2]]
list.sort(key = lambda item : item[2])
print(list)