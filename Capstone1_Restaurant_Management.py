from tabulate import tabulate   # Used to import tabulations

# Initial data
data_dish = [
    {'code': 'DISH01', 'name': 'Nasi Rendang Sapi', 'calories': 550, 'stock': 20, 'price': 30000},
    {'code': 'DISH02', 'name': 'Nasi Gulai Tunjang', 'calories': 500, 'stock': 10, 'price': 25000},
    {'code': 'DISH03', 'name': 'Nasi Dendeng Lambok', 'calories': 520, 'stock': 10, 'price': 30000},
    {'code': 'DISH04', 'name': 'Nasi Gulai Ayam', 'calories': 480, 'stock': 15, 'price': 20000},
    {'code': 'DISH05', 'name': 'Nasi Ayam Pop', 'calories': 520, 'stock': 15, 'price': 20000}
    ]

cart = []

# Function to display the main menu
def main_menu():
    while True:
        main_menu_choice = input('''
        -------------- WELCOME TO RM PADANG SEDERHANA --------------
        ------------------------------------------------------------
        1. Seller Menu
        2. Customer Menu
        3. Exit Program
        Please enter the corresponding number for your action (1-3): ''')

        if main_menu_choice == '1':
            while True:
                password = input('\tEnter the Seller Code to access the seller main menu: ')
                if password == '101':  # The current password is only 101
                    main_seller_menu()
                    break 
                else:
                    print('\tYour code is incorrect, please try again.')
        elif main_menu_choice == '2':
            main_customer_menu()
        elif main_menu_choice == '3':
            print('\tExiting the program. Have a great day!')
            break
        else:
            print('\tInvalid choice, please enter a valid option.')

# Function to display the main menu for seller
def main_seller_menu():
    while True:
        menu_seller_choice = input('''
                        Welcome to the Seller Menu!
        -----------------------------------------------------------
        1. Display Dish Data
        2. Add Dish Data
        3. Update Dish Data
        4. Delete Dish Data
        5. Back to Main Menu
        Please enter the corresponding number for your action (1-5): ''')
        
        if menu_seller_choice == '1':
            display_dish_data()
        elif menu_seller_choice == '2':
            add_dish_data()
        elif menu_seller_choice == '3':
            update_dish_data()
        elif menu_seller_choice == '4':
            delete_dish_data()
        elif menu_seller_choice == '5':
            print('\tExiting the Seller Menu.')
            return
        else:
            print('\tInvalid choice, please enter a valid option.')

# Function to display dish data in the seller menu
def display_dish_data():
    while True:
        menu_display_choice = input('''
                            Display Dish Data
        -----------------------------------------------------------
        1. Display All Dishes
        2. Search for Dish
        3. Back to Main Menu
        Please enter the corresponding number for your action (1-3): ''')

        if menu_display_choice == '1': 
            # Display all dishes
            if data_dish:
                print('\n\t\t\tRM Sederhana Menu')
                headers = ['Code', 'Name', 'Calories', 'Stock', 'Price']
                indented_table_all = '\n'.join(['\t'+ row for row in tabulate((dish.values() for dish in data_dish), headers=headers).split('\n')])
                print(indented_table_all)

        elif menu_display_choice == '2':  
            while True:  
                code = input('\tPlease input the dish code (e.g., \'dish01\', \'dish02\', etc.): ').upper()
                found_dish = None
                for dish in data_dish:
                    if dish['code'] == code:
                        found_dish = dish
                        break
                if found_dish:
                    print('\n\t\t\tSelected RM Sederhana Menu')
                    headers = ['Code', 'Name', 'Calories', 'Stock', 'Price']
                    indented_table = '\n'.join(['\t'+ row for row in tabulate([found_dish.values()], headers=headers).split('\n')])
                    print(indented_table)
                    break 
                else: 
                    print('\tDish not found! Please try again.')

        elif menu_display_choice == '3':  
            break 
        else:
            print('\tInvalid choice, please enter a valid option.')

# Function to add new dish data in the seller menu
def add_dish_data():
    while True:
        menu_add_choice = input(''' 
                                Add Dish Data
        -----------------------------------------------------------
        1. Add New Dish
        2. Back to Main Menu
        Please enter the corresponding number for your action (1-2): ''')

        if menu_add_choice == '1':
            while True:
                code = input('\tPlease input the dish code (e.g., \'dish01\', \'dish02\', etc.): ').upper()
                if not code:
                    print('\n\tDish code cannot be empty.')
                    continue
                existing_codes = [dish['code'] for dish in data_dish]  # Check if the dish code already exists
                if code in existing_codes:
                    print('\n\tDish with this code already exists. Please enter a different code.')
                    continue
                break
            
            while True:
                try:
                    name = input('\tEnter the dish name: ').title()
                    if name == '':
                        print('\tDish name cannot be empty.')
                        continue
                    break
                except ValueError:
                    print('\tInvalid input! Please enter a valid string for name')
            while True:
                try:
                    calories = int(input('\tEnter the calories (must be a positive integer): '))
                    if calories < 0:
                        print('\tCalories cannot be negative.')
                        continue
                    break
                except ValueError:
                    print('\tInvalid input! Please enter a valid integer for calories.')
            while True:
                try:
                    stock = int(input('\tEnter the stock (must be a positive integer): '))
                    if stock < 0:
                        print('\tStock cannot be negative.')
                        continue
                    break
                except ValueError:
                    print('\tInvalid input! Please enter a valid integer for stock.')
            while True:
                try:
                    price = float(input('\tEnter the price (must be a positive number): '))
                    if price < 0:
                        print('\tPrice cannot be negative.')
                        continue
                    break
                except ValueError:
                    print('\tInvalid input! Please enter a valid number for price.')

            # Displaying the new dish detail       
            new_dish = {'code': code, 'name': name, 'calories': calories, 'stock': stock, 'price': price}
            new_dish_data = [[code, name, calories, stock, price]]
            headers = ['Code', 'Name', 'Calories', 'Stock', 'Price']
            print('\n\t\t\tNew Dish Detail:')
            indented_table = '\n'.join(['\t'+ row for row in tabulate(new_dish_data, headers=headers).split('\n')])
            print(indented_table)

            # Ask for user confirmation to save the new data
            while True:
                save_choice = input("\n\tDo you want to save this data? (yes/no): ").lower()
                if save_choice == 'yes':
                    data_dish.append(new_dish)  # Add the new dish to the dataset
                    print('\tNew dish added successfully.')
                    break
                elif save_choice == 'no':
                    print('\tNew dish data not saved')
                    break
                else:
                    print('\tInvalid choice, please enter "yes" or "no"')
        elif menu_add_choice == '2':
            break
        else:
            print('\tInvalid choice, please enter a valid option.')


# Function to update dish data in the seller menu
def update_dish_data():
    # Create a dictionary to store dishes with their codes as keys.
    dish_dict = {dish['code']: dish for dish in data_dish}  
    while True:
        menu_update_choice = input('''
                                Update Dish Data
        -----------------------------------------------------------
        1. Update Existing Data
        2. Back to Main Menu
        Please enter the corresponding number for your action (1-2): ''')
        
        if menu_update_choice == '1':
            code = input('\tPlease input the dish code (e.g., \'dish01\', \'dish02\', etc.) or type \'back\': ').upper()  # Ask for the dish code to be updated
            dish = dish_dict.get(code)
            if code == 'BACK':
                break
            elif dish is None:
                print('\tDish with this code does not exist.')
                continue
            else:
                # Display existing dish data
                print('\n\t\t\tExisting Dish Data:')
                existing_dish = [[dish['code'], dish['name'], dish['calories'], dish['stock'], dish['price']]]
                headers = ['Code', 'Name', 'Calories', 'Stock', 'Price']
                indented_table = '\n'.join(['\t'+ row for row in tabulate(existing_dish, headers=headers).split('\n')])
                print(indented_table)

            # Ask for confirmation to update the dish data
            while True:
                confirm_update = input('\n\tDo you want to update this dish data? (yes/no): ').lower()
                if confirm_update == 'no':
                    print('\tUpdate operation cancelled.')
                    break
                elif confirm_update == 'yes':
                    # Ask for the new values for the dish attributes
                    new_code = input('\tEnter the new dish code (leave blank to keep current): ').upper() or dish['code']
                    name = input('\tEnter the new dish name (leave blank to keep current): ').title() or dish['name']
                    while True:
                        try:
                            calories = int(input('\tEnter the new dish calories (leave blank to keep current): ') or dish['calories'])
                            if calories < 0:
                                print('\tCalories cannot be negative.')
                                continue
                            break
                        except ValueError:
                            print('\tInvalid input! Please enter a valid integer for calories.')
                    while True:
                        try:
                            stock = int(input('\tEnter the new dish stock (leave blank to keep current): ') or dish['stock'])
                            if stock < 0:
                                print('\tStock cannot be negative.')
                                continue
                            break
                        except ValueError:
                            print('\tInvalid input! Please enter a valid integer for stock.')
                    while True:
                        try:
                            price = float(input('\tEnter the new dish price (leave blank to keep current): ') or dish['price'])
                            if price < 0:
                                print('\tPrice cannot be negative.')
                                continue
                            break
                        except ValueError:
                            print('\tInvalid input! Please enter a valid number for price.')

                    # Display updated dish data value 
                    updated_dish_data = [[new_code, name, calories, stock, price]]
                    headers = ['Code', 'Name', 'Calories', 'Stock', 'Price']
                    print('\n\t\t\tUpdated Dish Detail:')
                    indented_table_upd = '\n'.join(['\t'+ row for row in tabulate(updated_dish_data, headers=headers).split('\n')])
                    print(indented_table_upd)

                    # Ask for confirmation to save the updated data
                    while True:
                        save_choice = input('\tDo you want to save updated data? (yes/no): ').lower()
                        if save_choice == 'yes':
                            dish.update({'code': new_code, 'name': name, 'stock': stock, 'price': price, 'calories': calories})
                            print('\tDish updated successfully')
                            break
                        elif save_choice == 'no':
                            print('\tUpdated dish data not saved.')
                            break
                        else:
                            print('\tInvalid input! Please enter either "yes" or "no".')
                            continue
                    break
                else:
                    print('\tInvalid input! Please enter either "yes" or "no".')
                    continue
        elif menu_update_choice == '2':
            return
        else:
            print('\tInvalid choice, please enter a valid option.')

# Function to delete dish data in the seller menu
def delete_dish_data():
    while True:
        menu_delete_choice = input('''
                                Delete Dish Data
        -----------------------------------------------------------
        1. Delete Dish
        2. Back to Main Menu
        Please enter the corresponding number for your action (1-2): ''')
        
        if menu_delete_choice == '1':
            while True:  
                dish_code = input('\tPlease input the dish code (e.g., \'dish01\', \'dish02\', etc.): ').upper()
                found_dish = None
                for dish in data_dish:
                    if dish['code'] == dish_code:
                        found_dish = dish
                        break
                if found_dish:
                    print('\n\t\t\tSelected Dish Data:')
                    headers = ['Code', 'Name', 'Calories', 'Stock', 'Price']
                    dish_data = [[found_dish[key] for key in ['code', 'name', 'calories', 'stock', 'price']]]
                    indented_table = '\n'.join(['\t'+ row for row in tabulate(dish_data, headers=headers).split('\n')])
                    print(indented_table)

                    # Ask for confirmation to delete dish data
                    while True:
                        confirm_delete = input('\n\tAre you sure you want to delete this dish data? (yes/no): ').lower()
                        if confirm_delete == 'yes':
                            data_dish.remove(found_dish)
                            print('\tDish data deleted successfully.')
                            break
                        elif confirm_delete == 'no':
                            print('\tDeletion cancelled.')
                            break
                        else:
                            print('\tInvalid input! Please enter either "yes" or "no".')
                    break
                else:
                    print('\tDish with code {} does not exist.'.format(dish_code))
        
        elif menu_delete_choice == '2':
            break
        else:
            print('\tInvalid choice, please enter a valid option.')


# Function to display the main menu for customers
def main_customer_menu():
    while True: 
        menu_cust_choice = input('''
                    Welcome to Rumah Makan Padang Sederhana
        -----------------------------------------------------------
        1. View Dish Menu
        2. View Order Cart
        3. Checkout
        4. Back to Main Menu
        Please enter the corresponding number for your action (1-4): ''')

        if menu_cust_choice == '1':
            view_dish_menu()
            add_to_cart()
        elif menu_cust_choice == '2':
            print_cart()
            remove_from_cart()
        elif menu_cust_choice == '3':
            checkout_menu()
        elif menu_cust_choice == '4':
            print('\tThank you for choosing Rumah Makan Padang Sederhana!')
            break
        else:
            print('\tInvalid choice, please enter a valid option.')

# Function to display dish menu for customers
def view_dish_menu():
    print('\n\t\t\tRM Padang Sederhana Menu')
    headers = ['Code', 'Name', 'Calories', 'Stock', 'Price']
    indented_table = '\n'.join(['\t'+ row for row in tabulate((dish.values() for dish in data_dish), headers=headers).split('\n')])
    print(indented_table)

# Function to add items to the cart
def add_to_cart():
    while True:
        input_dish = input('\n\tDo you want to buy? If yes, enter the dish code (e.g., \'dish01\', \'dish02\', etc.). If not, type \'back\': ').upper()
        if input_dish == 'BACK':
            break
        found_dish = False
        for item in data_dish:
            if item['code'] == input_dish:
                found_dish = True
                while True:
                    quantity = input(f'\tEnter the quantity of {item["name"]} to add to the cart: ')
                    if quantity.isdigit() and int(quantity) > 0:
                        quantity = int(quantity)
                        if quantity > item['stock']:
                            print('\tQuantity exceeds available stock. Please adjust accordingly.')
                        else:
                            for cart_item in cart:
                                if cart_item['code'] == input_dish:
                                    if cart_item['quantity'] + quantity > item['stock']:
                                        print('\tQuantity exceeds available stock. Please adjust accordingly.')
                                    else:
                                        cart_item['quantity'] += quantity
                                        print(f"\t{quantity} {item['name']} has been added to the cart")
                                    break
                            else:
                                cart.append({'code': item['code'], 'name': item['name'], 'price': item['price'], 'quantity': quantity})
                                print(f"\t{quantity} {item['name']} has been added to the cart")
                                print_cart()
                            break
                    else:
                        print('\tInvalid quantity. Please enter a positive integer.')
                break
        if not found_dish:
            print('\n\tDish not found in the menu. Please enter a valid dish code.')

# Function to remove items from the cart
def remove_from_cart():
    while True:
        confirm_remove = input('\n\tDo you want to remove a dish from the cart (yes/no)? ').lower()
        if confirm_remove == 'no':
            break
        elif confirm_remove == 'yes':
            if len(cart) == 0:
                print('\tYour cart is empty. You cannot remove any products.')
                break
            else:
                remove_item_code = input("\tEnter the dish code to remove: ").upper()
                found_dish_item = None
                for item in cart:
                    if item['code'] == remove_item_code:
                        found_dish_item = item
                        break
                if found_dish_item:
                    quantity_to_remove = input("\tEnter the quantity to remove: ")
                    if quantity_to_remove.isdigit():
                        quantity_to_remove = int(quantity_to_remove)
                        if quantity_to_remove <= 0:
                            print("\tInvalid quantity. Please enter a positive number.")
                        elif quantity_to_remove <= found_dish_item['quantity']:
                            found_dish_item['quantity'] -= quantity_to_remove
                            if found_dish_item['quantity'] == 0:
                                cart.remove(found_dish_item)
                                print('\tDish has been completely removed from the cart.')
                            else:
                                print('\tQuantity successfully reduced.')
                            print_cart()
                        else:
                            print("\tInvalid quantity. You can't remove more than what's in the cart.")
                    else:
                        print("\tInvalid input. Please enter a valid quantity.")
                else:
                    print('\tDish not found_dish in the cart.')
        else:
            print('\tInvalid choice. Please enter "yes" or "no".')

# Function to process checkout
def checkout_menu():
    print_cart()
    while True:
        confirm_checkout = input('\tDo you want to checkout (yes/no)? ').capitalize()
        if confirm_checkout == 'No':
            break
        elif confirm_checkout == 'Yes':
            if len(cart) == 0:
                print('\tYour cart is empty. Please add items to your cart.')
                break
            else:
                for item in cart:
                    for dish in data_dish:
                        if dish['code'] == item['code']:
                            dish['stock'] -= item['quantity']
                            break
                total_price = sum(item['price'] * item['quantity'] for item in cart)
                print(f"\n\tTotal Price: {total_price}")
                
                while True:
                    payment = input("\tEnter payment amount: ")
                    if payment.isdigit() and int(payment) >= 0:
                        payment = int(payment)
                        if payment < total_price:
                            print("\tSorry, your payment isn't enough. Please add more funds.")
                        else:
                            break
                    else:
                        print("\tInvalid input! Please enter a valid payment amount.")
                
                change = payment - total_price
                print_invoice(total_price, change) 
                cart.clear()
                break
        else:
            print('\tInvalid choice. Please enter Yes or No.')

# Function to display the cart
def print_cart():
    headers = ['Code', 'Name', 'Price', 'Quantity', 'Total']
    cart_table = []
    total_price = 0
    
    for item in cart:
        total = item['price'] * item['quantity']
        row = [item['code'], item['name'], item['price'], item['quantity'], total]
        cart_table.append(row)
        total_price += total
    print('\n\t\t\tYour Selected Dishes')
    indented_table_all = '\n'.join(['\t'+ row for row in tabulate(cart_table, headers=headers).split('\n')])
    print(indented_table_all)
    return total_price

# Function to print the invoice
def print_invoice(total_price, change):
    print(f'''\n
        ------------------------INVOICE ------------------------
                    Rumah Makan Padang Sederhana''')
    print_cart()
    print(f'\n\tTotal Price: {total_price}')
    print(f'\tThank you for your purchase! Your change is {change} rupiah.')
    print('''
        Thank you for choosing RM Padang Sederhana!
        --------------------------------------------------------''')

# Main program execution
main_menu()
