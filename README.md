# Capstone IV: Shoe Inventory

A Python programme that utilises OOP to manage an inventory of Nike shoes, stored in an external .txt file.

Users are able to:
- View existing stock
- Add new stock
- Restock shoes that are in low supply
- Search for a specific shoe
- Calculate out the total value of the stock
- Discount shoes that are in high supply

## Table of Contents
1) [Installation](#installation)
2) [Usage](#usage)
3) [Credits](#credits)

## Installation
To install the programme, simply run inventory.py from a local directory. Please note that inventory.txt must also be in the same directory for the programme to run properly.

## Usage
### Inventory.txt
IMPORTANT: Please ensure you have inventory.txt installed in the same directory as inventory.py.

inventory.txt is the external file that stores all the shoe information. Each line of the file is a comma separated string in the following format:

Country,Code,Product,Cost,Quantity

![App Screenshot](https://i.ibb.co/wyk0Lqm/Screenshot-2023-01-22-at-19-28-23.png)

inventory.py can access these entries, edit them and create new entries in order to perform its functions.

### Menu
The main menu presents the following options:
![App Screenshot](https://i.ibb.co/rmRZnfM/Screenshot-2023-01-22-at-19-16-42.png)
Simply enter the relevant letter, followed by ENTER to access your desired function.

- (V) View All Stock
- (A) Add New Shoes
- (R) Restock Shoes
- (S) Search for Shoe
- (T)  Total Value Per Shoe
- (D) Discount Overstock
- (Q) Quit Program

### (V) View All Stock
Tabulates the inventory.txt data in an easy to read format:
![App Screenshot](https://i.ibb.co/QnVRRsN/Screenshot-2023-01-22-at-19-32-45.png)

### (A) Add New Shoes
Gives a series of requests for the user to enter the data for each field in a new shoe entry to be added to inventory.py

Please note that 'Cost' and 'Quantity' must be provided as numbers, otherwise an error message will appear.

### (R) Restock Shoes

Returns the Product and Quantity for the shoe with the least stock, and asks the user whether they'd like to restock.

If response is 'yes', the user is asked to provide a quantity to add, before confirming the new updated quantity.

![App Screenshot](https://i.ibb.co/LCRKmcG/Screenshot-2023-01-22-at-19-41-20.png)

### (S) Search for Shoe

Allows the user to enter a Product code (starting with 'SKU') to search for a particular entry in inventory.txt

![App Screenshot](https://i.ibb.co/8X8zF2Y/Screenshot-2023-01-22-at-19-43-42.png)

### (T) Total Value Per Shoe

Calculates the total value of each entry (cost multiplied by quantity), as well as calculating a total value for the entire inventory. Displays this information in an easy-to-read table.

![App Screenshot](https://i.ibb.co/rkdxKT3/Screenshot-2023-01-22-at-19-48-27.png)

### (D) Discount Overstock

Returns the Product and Quantity for the highest-quantity item, and asks the user whether they want to implement a 20% discount.

If response is 'yes', the new cost for the shoes is returned.

![App Screenshot](https://i.ibb.co/fMXm95d/Screenshot-2023-01-22-at-19-52-26.png)

### (Q) Quit

Closes the program

## Credits

Coded by Greg Hearle, using a Task Template from the [HyperionDev](hyperiondev.com) Software Engineering Bootcamp course.
