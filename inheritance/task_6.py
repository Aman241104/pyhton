# Create a system where a product is both a Discountable and a Taxable item. Calculate the final price after applying both tax and discount.


class tax:
    def tax(self):
        self.tax=(self.amt*28)/100
        print("Tax: ",self.tax)
        print("Product Price With Taxs: ",(self.amt+self.tax))

class discount:
    def discount(self):
        self.discount=int(input("Enter Discount Amount: "))
        self.discountamt=(self.amt*self.discount)/100
        print("Discount: ",self.discount)
        print("Price after Discount: ",self.amt - self.discount)
        print("-------------------------------------")
        print("Total Price: ",self.amt+self.tax-self.discount)


class product(tax,discount):
    def product(self):
        self.amt=int(input("Enter Product Price: "))
        print("Product original price: ",self.amt)


p1=product()
p1.product()
p1.tax()
p1.discount()
