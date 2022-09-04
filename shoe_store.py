class shoe:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


shoes = []

shoes.append(shoe("Nike", 200))
shoes.append(shoe("Crocs", 20))
shoes.append(shoe("Puma", 20))
shoes.append(shoe("World", 222))

for shoe_ in shoes:
    print(shoe_.name, shoe_.amount)

def re_stock(shoe_list):
    shoe_names = []
    min_shoe_amount = shoe_list[0].amount
    name_of_min = shoe_list[0].name
    for shoe_amt in shoe_list:
        if shoe_amt.amount <= min_shoe_amount:
            min_shoe_amount = shoe_amt.amount
            name_of_min = shoe_amt.name
            shoe_names.append(shoe_amt.name)
    if shoe_list[0].amount != min_shoe_amount:
        shoe_names.pop(0)
    

    print(f"The min shoe/s are/is {', '.join(shoe_names)} amount is {min_shoe_amount}")


    while True:

        user_update = input("Update amount Y/N ").upper()

        if user_update == "N":
            print(f"The min shoe/s are/is {', '.join(shoe_names)} amount is {min_shoe_amount}")
            break

        elif user_update == "Y":
            i = 0
            for shoe in shoe_list:
                
                if shoe.amount == min_shoe_amount:
                    
                    shoe.amount = int(input(f"What is your {shoe_names[i]} new amount? "))
                    new_amt = shoe.amount
                    i += 1
                
            print(f"The min shoe was is {name_of_min} new amount is {new_amt}")
            break

        else:
            print("Must enter 'Y' or 'N'")
            pass
            
re_stock(shoes)

for shoe_ in shoes:
    print(shoe_.name, shoe_.amount)