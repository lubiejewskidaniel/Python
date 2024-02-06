import csv  # Importing "csv" module which delivering functionality to read and write csv files


def read_all_data():  # Defining function which reads data from a CSV file named 'disneyland_reviews.csv'
    # and prints the number of rows in the dataset excluding the header.
    csv_list = []  # Initializing an empty list named "csv_list" that will be used to store the rows of the csv file
    file_path = 'data/disneyland_reviews.csv'  # Setting  file path to the CSV file
    # declaring it is located in the "data" directory and named "disneyland_reviews.csv"
    with open(file_path, 'r') as file:  # Opens "file_path" in mode "r" (file to reade) using with statement
        # to ensure file will be closed properly after reading.
        csv_reader = csv.reader(file)  # Creating "csv_reader" variable to iterate over lines in the csv file
        _ = next(csv_reader)  # Skipping the header but the header itself is not stored
        # accordingly to PEP8 it will come out as a PEP8 weak warning
        for row in csv_reader:  # This loop is responsible for iterating over each row in the csv file
            # and in each iteration "row" will represent a list of values from a single row in file. Inside
            # the loop each "row"  will be appended to the "csv_list". after the loop finish "csv_list" will contain
            # all the rows of the csv file excluding the header what gives exact amount of rows in csv file provided.
            csv_list.append(row)
    # Code below displaying message which is assigned to variable message by f-string which is calculating
    # length of the list "csv_list" by using "len()" function in this case it will give the number of rows
    # in dataset excluding header.
    message = f"Number of rows in the dataset: {len(csv_list)}, excluding the dataset header."
    print("\n\t\t\t\t\t\t\t\tDataset reading in - FINISHED.")
    print("\t\t\t", message)


def read_reviews_only(file):  # Function defining function to reads data from a csv file
    # containing reviews and returns a list of rows in the csv file.
    reviews = []  # Initializing an empty list "reviews" and will be used to store dictionaries
    # representing each row of the given csv file.

    #
    with open(file, 'r') as f:  # Opening file in read mode  and returns as "f"
        reader = csv.DictReader(f)  # Creating kind of instance od "DistReader"a and assigning to "reader" name
        # and it is linked with "f" open csv given file. Each row is taken as a dictionary data structure where
        # keys are taken from the header row of the csv file.
        for row in reader:
            reviews.append(row)  # Now csv file each line is iterating and append each dictionary row to the
            # "reviews" list what is below returned from function.
    return reviews


def view_reviews_by_park(reviews):  # This function displaying reviews for specified park from a given list of
    # reviews by taking them from parameter "reviews"
    # This function also allows user to input a park name (California, HongKong, or Paris) and
    # then after all calculations below displaying details of reviews related to expected park
    # from list of park provided in "disneyland_reviews.csv".
    park_reviews = []
    park_to_view = input("Enter the park you want to see reviews for (California, HongKong, Paris): ")

    # This loop checking reviews in given reviews list (which are case-insensitive by using
    # method "lower()") are present in the "Branch" column of the list.
    # If park name is found, adding review to the "park_reviews" list (using "append()" method).
    # Also checking if there are no reviews for specified park then message is displayed of
    # "No reviews found for {park_to_view}, please try again".
    # and finally if park is found iterating each review in "park_reviews" and
    # displaying all required information's.
    for review in reviews:
        if park_to_view.lower() in review['Branch'].lower():
            park_reviews.append(review)
    if not park_reviews:
        print(f"No reviews found for {park_to_view}, please try again.")
    else:
        for review in park_reviews:
            print(f"""                      Review ID: {review['Review_ID']}
                      Rating: {review['Rating']}
                      Year_Month: {review['Year_Month']}
                      Reviewer Location: {review['Reviewer_Location']}
                      Branch: {review['Branch']}
                      ----------------------------""")


def count_reviews_by_park_and_location(reviews):  # This function takes a list of "reviews" as
    # an input and performs calculations based on user selection and helps to find the number
    # of reviews for a specific park and reviewer's  location from a given list of reviews.

    matching_reviews = []

    # Getting user input for park name and reviewer's location
    # The lower method I used to convert user input to lowercase. This is done to make the
    # comparison case-insensitive when later on checking if the entered park and location match
    # the values in the "reviews".
    park = input("Enter the park name (California, HongKong, Paris): ").lower()
    location = input("Enter the reviewer's location: ").lower()

    for review in reviews:
        # Checking if the park name entered by the user is present in the current review
        if park in review['Branch'].lower():
            # Checking further if the reviewer's location entered by the user is present
            # in the current review
            if location in review['Reviewer_Location'].lower():
                # Identifying reviews where the user-specified location is part of the reviewer's
                # location in a case-insensitive manner. If both conditions are met, adding the "review"
                # to the list of "matching_reviews"
                matching_reviews.append(review)

    count = len(matching_reviews)  # Calculates the length of the "matching_reviews" list, which contains
    # the reviews that meet the conditions above.
    print(f"\nNumber of reviews for {park.capitalize()} from {location.capitalize()}: {count}\n")  # This line
    # prints a properly formatted message. Using an "f-string" to dynamically insert values into the string.
    # And changing first letter of park and location to capital letter using capitalize() method.


def average_rating_by_park_and_year(reviews):  # This function calculating and displaying the average rating for
    # a specific park and year based on user input.

    # Getting user input for park name and year
    park = input("Enter the park name (California, HongKong, Paris): ").lower()
    year = input("Enter the year: (from 2010 up to 2019) ")

    # Initializing variables to keep track of total rating and count of reviews
    total_rating = 0
    count = 0

    for review in reviews:
        # Checking if the park and year match the current data in review
        if park in review['Branch'].lower() and year in review['Year_Month']:
            rating_str = review['Rating']  # Extracting value of the dictionary key "Rating" and
            # assigning to variable rating_str

            # Checking if the rating is a valid float it will be helpful if someone type in rating other than digits
            if rating_str.replace('.', '', 1).isdigit():  # Checking if replaced first dot "." onto empty string, it
                # is done to handle cases where the rating might be a decimal number and ensure that the decimal point
                # is valid. And checks after replacement if the final string consist digits only. In this way I
                # verified if modified "rating_str" is a valid numeric value. Finally, if conditions is "True",
                # "rating_str" is converted to float (as per below) and added to "total_rating"
                total_rating += float(rating_str)  # also if the condition is "True", it increments the "count"
                # variable. This variable keeps track of the number of valid ratings encountered.
                count += 1
            else:  # If condition is "False" than below code will be executed which using again "f-string"
                # indicating that the rating is invalid for the specific review ID what will be helpful to easily
                # debug code later on in case of any problems.
                print(f"Skipping invalid rating for Review ID {review['Review_ID']}.")
    # Checking if any valid reviews were found for the specified park and year.
    # If the condition is true (no valid reviews were found), it prints a message saying that no reviews
    # were found for the specified park and year. The message will include the values of the park and year
    # entered by the user earlier. If the condition is false (meaning there are valid reviews), the program will go to
    # calculate the average rating and print the result.
    if count == 0:
        print(f"No reviews found for {park} in {year}.")
        return None

    average_rating = total_rating / count  # Simple calculations executed to get average rating
    print(f"\nAverage rating for {park.capitalize()} in {year}: {average_rating:.2f}\n")  # Using "f-string" to
    # dynamically add message and insert wanted values.


def average_rating_by_park_and_location(reviews):  # This function, calculating average ratings for different parks
    # based on the reviewer's location
    park_locations = {}  # Initializing an empty dictionary

    for review in reviews:
        # Extracting required information from the review
        park = review['Branch'].lower()
        location = review['Reviewer_Location'].lower()
        rating_str = review['Rating']

        if rating_str.isdigit():  # Check if the string is a valid float similar like in function above
            rating = float(rating_str)

            if park not in park_locations:  # Checking if the park is already in the dictionary
                park_locations[park] = {}

            # Checking if the location for the park is already in the dictionary
            # There is a nested dictionary for each location, initialized with "total_rating" and "count" set to 0.
            # This allows the consequent code to correctly gather and calculate the average ratings for each park and
            # location combination.
            if location not in park_locations[park]:
                park_locations[park][location] = {'total_rating': 0, 'count': 0}

            # Updating "total_rating" and "count" for the specific park and location
            park_locations[park][location]['total_rating'] += rating
            park_locations[park][location]['count'] += 1

    for park, locations in park_locations.items():  # Iterating over each key-value pair in the "park_locations"
        # dictionary. "park" represents the park name (key), and "locations" represents the nested dictionary for
        # that park. items() is used to return a view of the dictionary's key-value pairs as tuples.
        print(f"\nAverage ratings for {park.capitalize()} by reviewer location:")  # Printing a message with title
        # for average ratings for the current park starting with capital letter because of method capitalize() used
        # within.
        for location, data in locations.items():  # This loop iterates over each key-value pair in the nested
            # dictionary related with the current park "locations".
            # "location" represents the reviewer's location for the current park, and "data" represents the nested
            # dictionary containing "total_rating" and "count" for that location.
            average_rating = data["total_rating"] / data["count"]  # simple calculations
            # d"ata["total_rating"]" retrieves the total rating for the current location.
            # data["count"] retrieves the count of reviews for the current location.
            print(f"{location.capitalize()}: {average_rating:.2f}")  # Printing final information, formatting the
            # "average_rating" as a floating-point number with two decimal places.


def count_reviews_by_park(reviews):  # Defining function that taking a list of reviews as an input,
    # doing some calculations and returning dictionary with the count of reviews for
    # each Disneyland park.

    # Initializing dictionary to keep within count of reviews for each park and setting up
    # starting value to 0
    park_counts = {'Disneyland_California': 0, 'Disneyland_HongKong': 0, 'Disneyland_Paris': 0}

    for review in reviews:  # Iterating for each review in the "review" list
        park = review['Branch']  # Extracting park name what is stored under "Branch in the
        # given file from current "review"

        # Checking if the extracted park name is one of the file in "park_counts" and if yes,
        # incrementing "park_counts" in dictionary by 1 and this is done for each review in the provided list.
        # and finally returns result what is dictionary as the output of the function
        if park in park_counts:
            park_counts[park] += 1
    return park_counts
