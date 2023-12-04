class Module:
    def __init__(self, foodName, foodAmount):
        self.foodName = foodName
        self.foodAmount = foodAmount
        self.itemPrice = self.__itemPrice()
        self.totalPrice = self.totalPrice()

    def __itemPrice(self):
        if self.foodName == 'Dry Cured Iberian Ham':
            return 177.80
        elif self.foodName == 'Wagyu Steaks':
            return 450.00
        elif self.foodName == 'Matsukake Mushrooms':
            return 272.00
        elif self.foodName == 'Kopi Luwak Coffee':
            return 306.50
        elif self.foodName == 'Moose Cheese':
            return 487.20
        elif self.foodName == 'White Truffles':
            return 3600.00
        elif self.foodName == 'Blue Fin Tuna':
            return 3603.00
        elif self.foodName == 'Le Bonnote Potatoes':
            return 270.81
        else:
            print("Invalid")
            return
            


    def totalPrice(self):
        return itemPrice * foodAmount
    
    def __str__(self):
        return f'Food: {self.foodName} Amount: {self.foodAmount} Price: {self.totalPrice}'

        
        


    
    
