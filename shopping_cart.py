class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = [ ]
      
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({'name' : name, 'price' : price})
            self.total += price
        
        return self.total
    
    def mean_item_price(self):
        return self.total / len (self.items)

    def median_item_price(self):
        prices = [item['price'] for item in self.items]
        prices.sort()
        length = len (prices)
        
        if length % 2 == 0:
            median = (prices[length/2] + prices [length/2+1])/2
            return median
        
        median2 = prices[int(length/2)]
        return median2

    def apply_discount(self):
        if self.employee_discount == None:
            return "Sorry, there is no discount to apply to your cart :("
        
        return self.total * ((100-int(self.employee_discount))/100)

    def void_last_item(self):
        if self.total != 0:
            self.total -= self.items[-1]['price']
            del self.items [-1]
            
            return self.total
        
        return "There are no items in your cart!"