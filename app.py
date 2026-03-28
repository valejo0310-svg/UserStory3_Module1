from services import add_products , show_inventary , search_product , update_product , delete_product , calculate_statistics, inventary
from files import save_csv, load_csv, path
# Variable that keeps the main loop running (0 = exit)
Menu = 1
# Welcome banner displayed once at startup
print("""
╔════════════════════════════════════════════════════════════╗
        WELCOME TO THE SALES RECORD RIWI STORE!!             
╚════════════════════════════════════════════════════════════╝
""")

while Menu:
    """
        Main application loop.

        Displays the menu on each iteration and routes the user's input
        to the corresponding function. Keeps running until the user
        selects option 9 (Exit).
    """
    try:
        # Display menu and capture user input as an integer
        option = int(input(f"""{"-"*24} MAIN MENU {"-"*25}
1)  Enter Product
2)  Show inventory
3)  Search product
4)  Update product
5)  Delete product
6)  Calculate statistics 
7)  Save CSV
8). Load CVS
9) Exit
{"="*60}
➤ """))
#Capture user input and route to the corresponding function based on the selected option
        if option == 1:
            add_products()
        elif option == 2:
            show_inventary()
        elif option == 3:
            search_product()      
        elif option == 4:
            update_product()
        elif option == 5:
            delete_product()    
        elif option == 6:
            calculate_statistics()      
        elif option == 7:
            save_csv(inventary) 
        elif option ==8:
            load_csv(inventary)
        elif option == 9:
            print("Exiting...")
            Menu = 0

        else:
            # Handle any number outside the valid range
            print("Option not available.\n")

    except ValueError:
        # Triggered when the user types something that isn't a number
        print(" Invalid number.\n")
