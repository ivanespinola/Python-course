# Generators

def generator_function(num):
    for i in range(num):
        yield i

for item in generator_function(10):
    print(item)

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            #print(iterator)
            print(next(iterator))
        except StopIteration:
            break

special_for([1,2,3])


# class MyGen:
#     current = 0
#     def __init__(self, first, last):
#         self.firts = first
#         self.last = last
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration

    
  
# gen = MyGen(0,100)

# for i in gen:
#     print(i)

def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a 
        temp = a 
        a = b 
        b = temp + b 

for x in fib(21):
    print(x)