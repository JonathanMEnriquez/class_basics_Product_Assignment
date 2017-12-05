# Assignment: Product

class Product(object):
    def __init__(self,Price,Item_Name,Weight,Brand):
        self.price = Price
        self.item_name = Item_Name
        self.weight = Weight
        self.brand = Brand
        self.status = 'for sale'
    def sell(self):
        self.status = 'sold'
        return self
    def add_tax(self):
        tax = self.price * .1
        self.price += tax
        return self
    def returned(self,reason,box_opened = False):
        if reason == 'defective' or 'Defective':
            self.status = 'defective'
            self.price = 0
        elif box_opened == False:
            self.status = 'for sale'
        elif box_opened == True:
            self.status = 'used'
            self.price = self.price - (self.price * .2)
        return self
    def dislay_info(self):
        print "Price: " + str(self.price)
        print "Item: " + self.item_name
        print "Item Weight " + self.weight
        print "Brand: " + self.brand
        print "Status: " + self.status
        return self

milk = Product(3.99,'Milk','3 lbs','Dairy Farms')

milk.add_tax().sell().dislay_info()

