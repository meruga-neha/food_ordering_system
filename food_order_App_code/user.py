import json
class user:
    def __init__(self):
        self.personal_details = {}
        self.ordered_item = {}
    def register(self):
        name = input("enter your name:  ")
        phone_no = int(input("enter phone number: "))
        self.email = input("enter your email: ")
        address = input("enter your address: ")
        self.password = input("enter your password: ")
        user_details = {"name": name,"phone_no": phone_no,"email": self.email,"address": address,"password": self.password}
        self.personal_details[self.email] = user_details
        with open("Personal_details.json","w") as f:
            json.dump(self.personal_details,f,indent=4)
        print("congratulations you had register successfully......")
        return self.personal_details
    def login(self):
        print("welcome to your login page...")
        with open("Personal_details.json","r") as f:
            data = json.load(f)
        while True:
            email = input("enter your email: ")
            key = input("enter your password: ")
            if email in data:
                if  key == data[email]["password"]:
                    return True

                else:
                    return False
            else:
                return False
    def place_new_order(self):
        order_id = 0
        order_id = order_id+1
        self.order_food_items = []
        list_of_food = [{"name" : "tandoori chicken","quantity" : "4pieces", "price" : 240},
                        {"name": "vegan burger", "quantity": "1 piece","price": 300},
                        {"name": "tandoori chicken","quantity":"4pieces","price":400},
                        ]
        print("here is the menu...")
        for i in list_of_food:
            print(i)
        
        user_input = int(input("select the food item which you want to order: "))
        if user_input == 0:
            self.order_food_items.append(list_of_food[0])
        elif user_input == 1:
            self.order_food_items.append(list_of_food[1])
        elif user_input == 2:
            self.order_food_items.append(list_of_food[2])
        else:
            print("choose the item from menu..")
        print("press 1 for order confirmation: ")
        print("press 2 for order confirmation: ")
        option = int(input("enter your choice: "))
        self.ordered_item[order_id] = self.order_food_items
        if option == 1:
            print("order placed successfully!")
            with open("Order_history.json","w") as f:
                json.dump(self.ordered_item,f,indent=4)
        else:
            print("order cancelled!")
        return self.ordered_item
    
    def order_history(self):
        for k,v in self.ordered_item.items():
            print(f"order_id : {k} || order_details : {v}")

      
    
    def edit_profile(self):
        with open("Personal_details.json","r") as f:
            data = json.load(f)
        
        for k,v in data.items():
            print(f"user mail id: {k} || user details: {v}")
        
        mail_id = input("enter the user mail id which u want to update: ")
        field = input("enter the field which you want to update: ")
        updated_value = input("enter the updated value: ")
        data[mail_id][field] =updated_value
        with open("Personal_details.json","w") as f:
            json.dump(data,f,indent=4)
        return data
x = user()
print(x.order_history())

         

   


