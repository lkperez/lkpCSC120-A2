class ResaleShop:

    # What attributes will it need?
    # Inventory 
    # Info_computer(price, year_made, processor_type, memory, operating_system hard_drive_capacity)

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory, info_computer, price, year_made, processor_type, memory, operating_system, hard_drive_capacity):
        self.inventory = inventory
        self.price = price 
        self.year_made = year_made
        self.processor_type = processor_type
        self.memory = memory
        self.operating_system = operating_system
        self.hard_drive_capacity = hard_drive_capacity
    
    # What methods will you need?
    #Checking Inventory/printing inventory
    def check_inventory(inventory):
        for item in inventory:
            print(item) #print if any all the computers in inventory
    # Updating Price
    def updating_price(computer):
        if computer["year_made"] < 2021: #If the computer's model was made before 2021
            print("computer's price decreases")
        elif computer["memory"] < computer["memory"]: #If the computer has the ability to contain less storage
            print("Computer's price decreases")
        elif computer["year_made"] > 2021: #If the computer is a newer model
            print("Computer's price increases")
        else:
            print("Computer's price stays the same")
                
    # Buying Computer(add to inventory)/ #Selling Computer(remove from inventory)
    def sell(inventory):
        for item in inventory:
            del computer["inventory"]
            print("item sold!")
        else:
            print("item bought!")

    #creating a computer 
computer = ResaleShop(1200, 2021, "Apple M1 chip", "32GB", "macOS", "256GB") 
