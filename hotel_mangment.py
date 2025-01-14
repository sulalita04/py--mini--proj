#HOTEL MANAGEMENT SYSTEM
class Restaurant:
    def __init__(self):
        self.menu = {
            'burger': 100,
            'pizza': 200,
            'salad': 50,
            'drinks': 20,
            'chicken':70,
            'veg_thali' :50,
            'non_veg_thali' :120
        }
        self.orders = {}

    def display_menu(self):
        for item, price in self.menu.items():
            print("------------------------")
            print(f"{item}: {price}")

    def place_order(self, table_number):
        items = input("Enter items (comma separated): ").split(',')
        for item in items:
            item = item.strip()
            if item in self.menu:
                if table_number in self.orders:
                    self.orders[table_number].append(item)
                else:
                    self.orders[table_number] = [item]
            else:
                print(f"Item {item} not available")
        print(f"Order placed for table {table_number}")

    def display_orders(self):
        for table_number, items in self.orders.items():
            print(f"Table {table_number}: {items}")

    def generate_bill(self, table_number):
        if table_number in self.orders:
            total = 0
            for item in self.orders[table_number]:
                total += self.menu[item]
            print(f"Bill for table {table_number}: {total}")
        else:
            print(f"No orders for table {table_number}")


def main():
    restaurant = Restaurant()
    print("WELCOME TO HEAVEN RESTAURANT")
    print("1. Display menu")
    print("2. Place order")
    print("3. Display orders")
    print("4. Generate bill")
    print("5. Exit")
    while True:
     
        choice = input("\nEnter your choice: ")
        if choice == "1":
            restaurant.display_menu()
            print("----------------------")
        elif choice == "2":
            table_number = int(input("Enter table number: "))
            restaurant.place_order(table_number)
            print("----------------------")
        elif choice == "3":
            restaurant.display_orders()
            print("----------------------")
        elif choice == "4":
            table_number = int(input("Enter table number: "))
            restaurant.generate_bill(table_number)
            print("----------------------")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

    
