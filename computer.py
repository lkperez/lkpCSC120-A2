class Computer:

    # What attributes will it need?
    #Computer information:
    # price 
    # year_made
    # processor_type
    # memory 
    # operating_system
    # hard_drive_capacity

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, price, year_made, processor_type, memory, operating_system, hard_drive_capacity):
        self.price = price 
        self.year_made = year_made
        self.processor_type = processor_type
        self.memory = memory
        self.operating_system = operating_system
        self.hard_drive_capacity = hard_drive_capacity

    # What methods will you need?
    # Updating a computer's OS
    def update_computer(computer):
        if computer["year_made"] < computer["year_made"] + 1: #Every year that passes
            ("update software")


# creating a computer 
computer = Computer(1200, 2021, "Apple M1 chip", "32GB", "macOS", "256GB") 
