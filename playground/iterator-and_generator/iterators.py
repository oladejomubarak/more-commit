lst = [1, 2, 3, 4]
it = iter(lst)
print(next(it))
print(next(it))
print(next(it))
print(list(it))  # print the remaining list in list that has not been iterated upon


def custom_for(iterable, func):
    it = iter(iterable)
    while True:
        try:
            #print(next(it))
            func(next(it))
        except StopIteration:
            print("End of loop")
            return


custom_for(lst, print)
