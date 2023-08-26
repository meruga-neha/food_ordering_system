import json
class Admin:
    def __init__(self):
        self.food_id = 0
        self.food_item = {}

    def add_new_food(self):
        self.food_id += 1
        name = input('enter food name:  ')
        quantity = input('enter food quantity:  ')
        stock = input("enter food stock:  ")
        price = float(input('enter the food price:  '))
        discount = float(input('enter the food discount:  '))
        food_items ={"food_name": name,"food_quantity": quantity,"food_stock": stock,"food_price": price,"food_discount": discount}
        self.food_item[self.food_id] = food_items
        with open("Food_items.json","w") as f:
            json.dump(self.food_item,f,indent=4)
        print("food item added successfully!")
        return self.food_item
    
    def edit_food_items(self):
        self.food_id+= 1
        with open("food_items.json","r") as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"food id: {k} || food items: {v}")
        id = input("enter the food id which you want to edit: ")
        item = input("enter the field which you want to update: ")
        updated_value = input("enter the updated value: ")
        data[id][item] = updated_value
        with open("Food_item.json","w") as f:
            json.dump(data,f,indent=4)
        print("food item updated successfully ..")
        return data
    
    def show_food_items(self):
        with open("Food_items.json","r") as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"food_id: {k} || food_items: {v}")


    def remove_food_items(self):
        with open("Food_items.json","r") as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"food_id: {k} || food_items: {v} ")
        id = input("enter the food id which you want to remove:  ")
        del data[id]
        with open("Food_items.json","w") as f:
            json.dump(data,f,indent=4)
        print("food id removed successfully...")
        return data

