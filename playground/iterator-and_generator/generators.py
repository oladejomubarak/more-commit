def custom_range(num):
   pass

def infinite_number_generator():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_number_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:
    print(i)