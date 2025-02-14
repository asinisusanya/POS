def display_items(items):
    print("\n{:<10} {:<20} {:<10}".format("Item Code", "Item Name", "Price"))
    print("-" * 40)
    for item in items:
        print("{:<10} {:<20} {:<10.2f}".format(item['code'], item['name'], item['price']))


def get_valid_item_code(items):
    while True:
        code = input("Enter Item Code: ")
        for item in items:
            if item['code'] == code:
                return code
        print("Invalid Item Code! Please enter a valid code.")


def process_sale(items):
    num_types = int(input("Enter the number of different item types: "))
    bill = []
    total = 0

    for _ in range(num_types):
        code = get_valid_item_code(items)
        quantity = int(input("Enter Quantity: "))
        for item in items:
            if item['code'] == code:
                total_price = quantity * item['price']
                bill.append({'code': code, 'name': item['name'], 'quantity': quantity, 'unit_price': item['price'],
                             'total_price': total_price})
                total += total_price

    print("\n{:<10} {:<20} {:<10} {:<10} {:<10}".format("Item Code", "Item Name", "Quantity", "Unit Price", "Total"))
    print("-" * 60)
    for entry in bill:
        print("{:<10} {:<20} {:<10} {:<10.2f} {:<10.2f}".format(entry['code'], entry['name'], entry['quantity'],
                                                                entry['unit_price'], entry['total_price']))

    print(f"\nSUB TOTAL: Rs. {total:.2f}")
    discount_choice = int(
        input("\nChoose a discount type:\n1. No Discount\n2. 5% Discount\n3. Custom Discount\nEnter choice: "))

    if discount_choice == 2:
        discount = total * 0.05
    elif discount_choice == 3:
        discount = float(input("Enter discount amount: "))
    else:
        discount = 0

    net_total = total - discount
    print(f"\nDISCOUNTED VALUE: Rs. {discount:.2f}")
    print(f"NET TOTAL: Rs. {net_total:.2f}")


def main():
    items = [
        {'code': 'M100', 'name': 'Shirt', 'price': 1500.00},
        {'code': 'W200', 'name': 'Frock', 'price': 2000.00},
        {'code': 'T300', 'name': 'Trouser', 'price': 1800.00}
    ]

    while True:
        print("\n******** WELCOME TO ABC FASHION STORE ********")
        print("1. Make a new sale")
        print("2. Exit from POS system")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_items(items)
            process_sale(items)
        elif choice == 2:
            print("Thank you for using ABC Fashion Store POS System!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
