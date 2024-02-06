# Importing classes and functions required to run program
from classes.exporter import Exporter
from classes.ops import Ops
from process import read_all_data, read_reviews_only, view_reviews_by_park, count_reviews_by_park_and_location
from process import average_rating_by_park_and_year, average_rating_by_park_and_location
from process import count_reviews_by_park
from tui import display_greeting, display_main_menu, display_menu_a, display_menu_b
from tui import display_main_menu_oop
from visual import create_pie_chart, plot_average_review_scores, display_top_locations_bar_chart
from visual import plot_average_rating_by_month


# Creating instance of Exporter class
exporter = Exporter()
# Creating instance of Ops class for Disneyland
disneyland = Ops("Disneyland")
# Specifying the file name for reading reviews
filename = 'data/disneyland_reviews.csv'
# Reading only this reviews which are from specified file
reviews = read_reviews_only(filename)

# Displaying a greeting message from function display_greeting()
display_greeting()
# Reading data from function read_all_data() to show all records in dataset provided
# in file Disneyland_reviews.csv
read_all_data()
print()

# Adding each review to the "Disneyland" object
# I implemented this in "main.py" as I was not to sure how to create external function
# for this functionality
for review in reviews:
    disneyland.add_review(review)

while True:  # Added "while loop" - This loop will continue to execute indefinitely
    # until user press "X" to Exit program - this behaves like a proper Menu with selectable options
    # Displaying the main menu from function "display_main_menu()" and getting user input
    main_menu = display_main_menu()
    if main_menu.upper() == "A":
        # If user's input "A" in main Menu - displaying nested/inner Menu to select 4 further options
        # and for each selected options will be separate function executed
        while True:
            menu_a = display_menu_a()
            if menu_a.upper() == "A":  # if user choose A
                view_reviews_by_park(reviews)  # calling a function to display reviews by park
                break  # Breaking out of the inner loop and going back to main menu
            elif menu_a.upper() == "B":  # if user choose B
                count_reviews_by_park_and_location(reviews)  # calling function to count reviews by park and location
                break  # Breaking out of the inner loop and going back to main menu
            elif menu_a.upper() == "C":  # if user choose C
                average_rating_by_park_and_year(reviews)  # calling function to calculate
                # average rating by park and year
                break  # Breaking out of the inner loop and going back to main menu
            elif menu_a.upper() == "D":  # if user choose D
                average_rating_by_park_and_location(reviews)   # Calling function to calculate
                # average rating by park and location
                break  # Breaking out of the inner loop and going back to main menu
            else:
                print("Incorrect menu option selected. Please try again.")  # If user enters an incorrect option
                break  # breaking out of the inner loop and going back to main menu
    elif main_menu.upper() == "B":
        # If user's input "B" in main Menu - displaying nested/inner Menu to select 4 further options
        # and for each selected options will be separate function executed
        while True:
            menu_a = display_menu_b()
            if menu_a.upper() == "A":
                # If user chooses option A, calculate and display park counts and a pie chart for
                # Most Reviewed Parks
                park_counts = count_reviews_by_park(reviews)  # This line is calculating and storing the counts
                # of reviews for each park in variable "park_counts" by function called form module "processes.py"
                # "count_reviews_by_park()" passing an argument "reviews" to its function
                create_pie_chart(park_counts)  # Displaying pie chart by function "create_pie_chart()" by passing as
                # an argument calculations executed by function above and stored in variable "park_counts"
                break  # Breaking out of the inner loop and going back to main menu
            elif menu_a.upper() == "B":
                # If user chooses B, the average review score will be given in a form of a single bar chart
                plot_average_review_scores(reviews)  # Plotting average review scores by
                # function "plot_average_review_scores(reviews)"
                break  # Breaking out of the inner loop and going back to main menu
            elif menu_a.upper() == "C":
                # If user chooses C, will be given Park Ranking by nationality in a form of bar chart
                display_top_locations_bar_chart(reviews)  # Displaying top locations bar chart
                break  # Breaking out of the inner loop and going back to main menu
            elif menu_a.upper() == "D":
                # If user select D, will be asked to input a park name and then will be given bar chart of
                # the average rating that park received for each month of the year.
                plot_average_rating_by_month(reviews)  # Displaying bar chart
                break  # Breaking out of the inner loop and going back to main menu
            else:
                print("Incorrect menu option selected. Please try again.")  # If user input incorrect menu option
                break  # breaking out of the inner loop and going back to main menu
    elif main_menu == "C":  # Checking if user selected option "C" and if is selected
        # inner menu will be displayed to be able to choose appropriate file extension
        # For each selection is a proper calling method created named "export_to_..." on an instance of the "Exporter"
        # class.
        while True:
            menu_oop = display_main_menu_oop()
            if menu_oop.upper() == "A":  # If A option selected will be created txt file
                # with aggregated data:
                # -Number of reviews.
                # -Number of positive reviews.
                # -Average review score
                # -Number of countries that have reviewed each park.
                # and file will be named "disneyland_aggregate.txt"
                # Accordingly "disneyland_aggregate.csv", "disneyland_aggregate.json" files will be created
                # for selection B and C unless user select X to exit from this inner submenu.
                exporter.export_to_txt(disneyland, 'disneyland_aggregate.txt')
                break  # Breaking out of the inner loop and going back to main menu
            elif menu_oop.upper() == "B":
                exporter.export_to_csv(disneyland, 'disneyland_aggregate.csv')
                break  # Breaking out of the inner loop and going back to main menu
            elif menu_oop.upper() == "C":
                exporter.export_to_json(disneyland, 'disneyland_aggregate.json')
                break  # Breaking out of the inner loop and going back to main menu
            elif menu_oop.upper() == "X":
                break
            else:
                print("Incorrect menu option selected. Please try again.")  # If user input incorrect menu option
    elif main_menu.upper() == "X":
        print("\t\t\t\t\t\t\tYou decided to end the program. Good Bye!")
        break  # Breaking out of the loop and ending program
    else:
        print("You have entered incorrect menu option. Please try again.")  # If userinput incorrect menu
        # option, will be displayed appropriate information and possibility to chose correct option unless
        # user decide to chose X and END the program.
