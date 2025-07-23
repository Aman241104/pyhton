def number_gen(n):
    for i in range(n):
        yield i
        i +=2

gen = number_gen(5)

for number in gen:
    print(number)