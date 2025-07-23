# bname, author, ibpn, pages, book_type, price, copies

class book:
    def __init__(self,name,author,ibpn,pages,book_type,price,copies):
        self.name = name
        self.author = author
        self.ibpn = ibpn
        self.pages = pages
        self.book_type = book_type
        self.price = price
        self.copies = copies

        # def getdata(self):
        #     self.name = input("Enter Book Name:")  
        #     self.author = (input("Enter Auther Name:"))
        #     self.ibpn=int(input("Enter ibpn number:"))
        #     self.pages=int(input("Enter number of pages:"))
        #     self.book_type=(input("Enter book type:"))
        #     self.price=int(input("Enter price:"))
        #     self.copies=int(input("Enter number copies:"))

        def display(self):  
            print(f"Book Name: {self.name}")
            print(f"Auther: {self.author}")
            print(f"ibpn number: {self.ibpn}")
            print(f"Pages: {self.pages}")
            print(f"Type: {self.book_type}")
            print(f"Price: {self.price}")
            print(f"Copies: {self.copies}")

book1 = book("abc","idk",0000,1,"idk",513,1)
# book1.getdata()
book1.display()