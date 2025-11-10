class Coffee:
    def __init__(self ,name ,price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self ,coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your Order")

    def remove_item(self ,coffee):
        for item in self.items:
            if item.name.lower() == coffee.lower():
                self.items.remove(item)
                print(f"Removed {item.name} from your Order")
                return
        print(f"{coffee} is not in your Order")


    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
         if not self.items:
             print("Your Cart is Empty")
             return
         print("Your order")
         for i,item in enumerate(self.items,1):
             print(f"{i} . {item.name} - €{item.price}")

         print(f"Your Grand Total is : €{self.total():.2f}\n")

    def checkout(self):
        if not self.items:
            print("Your Cart is Empty")
            return
        self.show_order()
        confirm = input("Proceed to checkout? (yes/no):").strip().lower()
        if confirm == "yes":
            print("Order confirmed! Thank You.")
            self.items.clear()
        else:
            print("Checkout Failed.")


def main():

    menu = [
        Coffee("Caffè Nero", 3.85),
        Coffee("Greggs", 2.22),
        Coffee("Costa", 4.05),
        Coffee("Pert A Manger", 3.88)
    ]

    order = Order()

    while True:

        print("\n--- Coffee Menu ---\n")

        for i,coffee in enumerate(menu,1):
            print(f"{i}. {coffee.name} - €{coffee.price}")

        print("5. View Order")

        print("6. Remove Item")

        print("7. Checkout")

        print("8. Exit")


        choice = input("Choose an option: ")

        if choice in ['1','2','3','4']:
            order.add_item(menu[int(choice)-1])

        elif choice == '5':
            order.show_order()

        elif choice == '6':
            remove = input("Which Coffee is to be removed?\n")
            order.remove_item(remove)

        elif choice == '7':
            order.checkout()

        elif choice == '8':
            print("Thanks for visiting, Have a Great Day")
            break

        else:
            print("Invalid Choice. Try again.")

if __name__ == "__main__":
    main()