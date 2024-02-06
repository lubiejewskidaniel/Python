# Text-based user interface
def display_greeting():  # Function which displaying the greeting message
    greeting = "Disneyland Review Analyser"  # Displaying the greeting message
    dashes = "-" * len(greeting)  # Creating dashes with the same length as the greeting string

    # Printing a formatted greeting message using dashes above and below
    print("\t\t\t\t\t\t\t\t", dashes)
    print(f"\t\t\t\t\t\t\t\t {greeting}")
    print("\t\t\t\t\t\t\t\t", dashes)


def display_main_menu():  # Function which displaying the main menu and get user input as a MENU selection
    # Below is a menu displayed in exact form as text is stated in triple quotes and awaiting user selection
    main_menu = input(""" 
            Please enter the letter which corresponds with your desired menu choice:
                                    [A] View Data
                                    [B] Visualise Data
                                    [C] Get aggregate information for each Park 
                                    [X] Exit
                                    """).upper()
    # The .upper() method is used to the user's input to convert it to uppercase.
    # This making that the function is case-insensitive and can be used both uppercase and lowercase input.
    return main_menu  # User's menu choice is here returned by the function

# All functions below going to be working in exactly the same way as function above.
# However, all of them will be displayed accordingly to user selection in the menu above as an inner sub-menu.


def display_main_menu_oop():
    print("\t\t\t\t\t\t\tYou have chosen option C - Get aggregate information in requested file")
    menu_oop = input("""
            Please enter the letter which corresponds with your desired menu choice:
                                    [A] Download data as TXT file
                                    [B] Download data as CSV file
                                    [C] Download data as JSON file
                                    [X] Go to main MENU
                                    """).upper()
    return menu_oop


def display_menu_a():
    print("\t\t\t\t\t\t\tYou have chosen option A - View Data")
    menu_a = input("""                            Please enter one of the following options:
                                    [A] View Reviews by Park
                                    [B] Number of Reviews by Park and reviewer Location
                                    [C] Average Score per Park and per Year
                                    [D] Average Score per Park and per Reviewer Location                
                                    """).upper()
    return menu_a


def display_menu_b():
    print("\t\t\t\t\t\t\tYou have chosen option B - Visualise Data")
    menu_b = input("""                            Please enter one of the following options:
                                    [A] Most Reviewed Parks
                                    [B] Average Scores
                                    [C] Park Ranking by Nationality
                                    [D] Most Popular Month by Park
                                    """).upper()
    return menu_b
