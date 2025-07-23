try:
    data = ["a","b","c"]
    it=iter(data)

    for i in range(0,10):
        print(next(it))
except StopIteration as i:
    print(i)
    print("Stop here")