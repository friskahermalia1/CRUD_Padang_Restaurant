
# Purwadhika-Capstone1-Project
This repository contains the capstone project developed as part of the Digital Talent Incubator (DTI) program at Purwadhika. This is my first program that I wrote and actually uploaded to github for the world to access. This Python program serves as a digital seller system for managing orders and menu items at the RM Padang Restaurant. It offers two main interfaces: one for sellers to manage inventory and another for customers to browse the menu, place orders, and complete transactions. To access seller menu, choose option seller menu and  '101' as password.

## Data Initialization
In this program, it is not connected to an external database for dish information. Instead, all the necessary details are included directly in the code itself.

<img width="500" alt="Initial Data" src="Terminal_View/1 Initial Data.png">

## Main Menu 
This program offers two main interfaces: one for restaurant staff to manage dishes and orders, and another for customers to browse the menu, place orders, and make payments.

<img width="500" alt="Main Menu" src="Terminal_View/2 Main Menu.png">

## Seller Menu Features:
<img width="500" alt="Main Seller Menu" src="Terminal_View/3 Main Seller Menu.png">

1. **Display Dish Data:**
   - This feature allows sellers to view all the dishes available in the restaurant's inventory and view specific dishes based on dish code input.
   - Sellers can see essential details for each dish, including its unique code, name, calorie count, current stock quantity, and price.
<img width="500" alt="Display Dish Data" src="Terminal_View/3a Seller Menu - Display Dish Data.png">

2. **Add Dish Data:**
   - Sellers can use this feature to add new dishes to the restaurant's menu.
   - Upon selecting this option, sellers are prompted to input details for the new dish. The program validates the input to ensure data integrity, such as checking for unique dish codes and ensuring that numerical values are entered correctly.
   - After entering the information, the seller is given the option to confirm the addition of the new dish to the menu.
<img width="500" alt="Add Dish Data" src="Terminal_View/3b Seller Menu - Add Dish Data.png">

3. **Update Dish Data:**
   - With this feature, sellers can modify the details of existing dishes in the restaurant's menu.
   - Sellers are prompted to input the code of the dish they wish to update. Sellers can choose which attributes to update and enter the new values accordingly.
   - The program validates the input and provides feedback to ensure accurate data entry.
<img width="500" alt="Update Dish Data" src="Terminal_View/3c Seller Menu - Update Dish Data.png">

4. **Delete Dish Data:**
   - This feature allows sellers to remove dishes from the restaurant's menu by input dish code.
   - The program verifies the existence of the specified dish and displays its details for confirmation.
<img width="500" alt="Delete Dish Data" src="Terminal_View/3d Seller Menu - Delete Dish Data.png">

## Customer Menu Features:
<img width="500" alt="Main Customer Menu" src="Terminal_View/4 Main Customer Menu.png">

1. **View Dish Menu:**
   - Customers can access this feature to browse the restaurant menu and view available dishes and add them to their cart.
   - The program displays a comprehensive list of dishes along with their details, including code, name, calorie count, stock quantity, and price.
<img width="500" alt="View Dish Menu" src="Terminal_View/4a Customer Menu - View Dish Menu.png">

2. **View Order Cart:**
   - Customers can use this feature to review the items they have selected for their order and also if customers need to make adjustments to their order, they can utilize this feature to remove items from their order cart.
   - Additionally, the total price of the order is calculated and displayed for the customer's reference.
<img width="500" alt="View Order Cart" src="Terminal_View/4b Customer Menu - View Order Cart.png">

3. **Checkout:**
   - Once customers have finalized their order, they can proceed to checkout using this feature.
   - The program displays a summary of the customer's order, including all selected dishes and the total price.
   - Customers are prompted to confirm their decision to proceed with the checkout process.
   - After confirmation, the program processes the order and generates an invoice for the customer. An invoice includes order details and serves as a receipt for the transaction.
<img width="500" alt="Checkout" src="Terminal_View/4c Customer Menu - Checkout.png">

## How to Use
1. Make sure you have Python installed on your computer.
2. Install the tabulate module by running `pip install tabulate` in your terminal or command prompt.
3. Download or copy this project to your computer.
4. Open the project folder in your terminal or command prompt.
5. Run the program by typing `Capstone1_Restaurant_Management.py`.
6. Follow the instructions on the screen to navigate through the menus.

## Limitations
- This program uses hardcoded dish data directly in the code without integration with an external database. Please do share some feedback on the program If you have ideas for improvements or want to fix issues.
