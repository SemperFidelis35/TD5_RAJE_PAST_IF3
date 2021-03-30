class Order:
    # Constructor
    def __init__(self, quantity, price, type, nb):
        self.__qty = quantity
        self.__price = price
        self.__type = type
        self.__id = nb


    # Setters
    def set_qty(self, quantity):
        self.__qty = quantity
        

    # Getters
    def get_qty(self):
        return self.__qty
    

    def get_price(self):
        return self.__price
    

    def get_type(self):
        return self.__type
    

    def get_id(self):
        return self.__id


class Book:
    
    # Constructor
    def __init__(self, name="BOOK"):
        self.__name = name
        self.__buy_orders = []
        self.__sell_orders = []
        self.__cpt = 1

    # Methods (public)
    def insert_buy(self, quantity, price):
        self.__insert_order(quantity, price, type="BUY")
        

    def insert_sell(self, quantity, price):
        self.__insert_order(quantity, price, type="SELL")
        

    # Methods (private)
    def __insert_order(self, quantity, price, type):
        
        order = Order(quantity, price, type, self.__cpt)
        self.__cpt += 1
        
        # Add Order To Book
        if type == "BUY":
            self.__buy_orders.append(order)
        else:
            
            self.__sell_orders.append(order)
        print("\t Insert {} {}@{} id={} on {}".format(order.get_type(), order.get_qty(), order.get_price(), order.get_id(), self.__name))
        # Update Book
        self.__sort_orders(type)
        self.__check_order_execute()
        
        return self.__print_book()
    

    def __sort_orders(self, type):
        
        #Sort All Active Buy Orders
        if type == "BUY":
            s = sorted(self.__buy_orders, key=Order.get_id, reverse=False)
            self.__buy_orders = sorted(s, key=Order.get_price, reverse=True)
            
        #Sort All Active Sell Orders
        else:
            s = sorted(self.__sell_orders, key=Order.get_id, reverse=True)
            self.__sell_orders = sorted(s, key=Order.get_price, reverse=True)
            

    def __check_order_execute(self):
        
        # Check If The Two Order Book Aren't Empty        
        if len(self.__sell_orders) > 0 and len(self.__buy_orders) > 0:
            
            #While An Order Is Executed            
            while self.__buy_orders[0].get_price() >= self.__sell_orders[-1].get_price():
                
                #Set Transaction Quantity of a transaction
                if self.__buy_orders[0].get_qty() > self.__sell_orders[-1].get_qty():
                    trans_qty = self.__sell_orders[-1].get_qty()
                    
                else:
                    trans_qty = self.__buy_orders[0].get_qty()
                    
                #Updating Order Quantity
                self.__buy_orders[0].set_qty(self.__buy_orders[0].get_qty() - trans_qty)
                self.__sell_orders[-1].set_qty(self.__sell_orders[-1].get_qty() - trans_qty)
                print("Execute {} at {} on {}".format(trans_qty, self.__buy_orders[0].get_price(), self.__name))
                
                #Removing From Book
                if self.__buy_orders[0].get_qty() == 0:
                    self.__buy_orders = self.__buy_orders[1:]
                    
                if self.__sell_orders[-1].get_qty() == 0:
                    self.__sell_orders = self.__sell_orders[0:-1]
 
    
    def __print_book(self):
        print("Book on {}".format(self.__name))
        
        #Show All Actual SELL Orders
        for i in range(0, len(self.__sell_orders)):
            print("        {} {}@{} id={}".format(self.__sell_orders[i].get_type(), self.__sell_orders[i].get_qty(), self.__sell_orders[i].get_price(), self.__sell_orders[i].get_id()))   
        #Show All Actual BUY Orders
        for i in range(0, len(self.__buy_orders)):
            print("        {} {}@{} id={}".format(self.__buy_orders[i].get_type(), self.__buy_orders[i].get_qty(), self.__buy_orders[i].get_price(), self.__buy_orders[i].get_id()))
        print("\n")
