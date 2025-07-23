with open('FILE_1.txt','w') as file:
    file.write("First Line by write")
    file.close()

with open('FILE_1.txt','a') as f:
    f.write("\nSecond line by append")
    f.close()

with open('FILE_1.txt','r') as file:
    print(file.read())
    file.close()