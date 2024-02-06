# Visualization - I decided to keep all calculations due to visualization in the same module
# except of create_pie_chart() function as calculations was a part of already existing function
# in process.py module
import matplotlib.pyplot as plt  # Importing matplotlib library for creating visualizations as a plt
# for easier coding purposes


def create_pie_chart(park_counts):
    # Defining a function named create_pie_chart() the function is created to visualise a pie chart
    # based on argument park_counts which is passed as an argument and its calculation is done as a part
    # of process.py module and its function count_reviews_by_park()
    labels = list(park_counts.keys())  # Creating list "labels" containing the keys (park names) of
    # dictionary "park_counts". In a pie chart, each slice has a label, which is the name of a park in this example.
    # The keys in the dictionary "park_counts" show the names of the parks.
    values = list(park_counts.values())  # Creating list "values" containing the values (review counts) of
    # dictionary "park_counts". In a pie chart, these "values" show how many reviews or what percentage of
    # reviews each park has. The "values" are the numbers in the dictionary "park_counts".

    explode = (0.05, 0.05, 0.05)  # Creating a tuple "explode" with 3 values of what pie chart should to be
    # expanded from the center what gives to my pie chart a unique visual separation of each slice
    colors = ['#FF0000', '#FFF000', '#00FFFF']  # Creating a list "colors" to store 3 hexadecimal values
    # these values ale equivalent to colors. This will change standard slices colors to defined by myself,
    # giving extraordinary visual effect.
    # Using a lambda function to format percentage values on the pie chart
    autopct_format = lambda p: f"{p:.1f}%\n({int(p * sum(values) / 100)})"  # I tried to add more details to each
    # slice, I found solution to use lambda function which basically format text that appears on each of the
    # pie chart slice. "autopct" parameter plt.pie() function below formatting the percentage labels on each
    # wedge of the pie. If I need to break it down - lambda function taking percentage value "p" and formatting
    # it by using f-string formatting method. So it is formatting "p" with one decimal place then adding a percentage
    # symbol and a new line character to separate percentage from the count and on the end calculates the count of
    # reviews by multiplying the percentage "p" with total sum of values (total number of reviews) and dividing by 100
    # In result is converted to integer and count is displayed in parentheses on the pie chart.

    plt.figure(figsize=(10, 5))  # In this line I defined size of figure where pie chart going to be displayed
    plt.pie(values, labels=labels, autopct=autopct_format, startangle=140, explode=explode, shadow=True, colors=colors)
    # line above creating the pie chart by its parameters, "values", "labels", "autopct", "explode" and "colors" have
    # been defined earlier; "shadow=True" it is a parameter responsible to adds shadow effect to the pie chart,
    # "startangle" parameter is specifying the angle at which first slice of the pie starts, in my case I set it on
    # 140 degrees.
    plt.title('Distribution of Reviews by Park')  # Adding title to the pie chart
    plt.show()  # And finally this function display final visualisation of the pie chart base on all data above.


def plot_average_review_scores(reviews):
    # Defining function to calculate and plot the average review scores for each Disneyland park
    park_ratings = {}  # Creating dictionary to store total ratings and counts for each park

    # Iterating each review
    for review in reviews:
        park = review['Branch'].lower()  # Extracting the park name and convert it to lowercase
        rating_str = review['Rating']  # Extracting the value with the key "Rating" from the "review"
        # dictionary and assigning it to "rating_str" variable.

        # This part makes sure that only real numbers are used for ratings, and it adds up
        # all the ratings and counts how many there are for each park in the "park_ratings" list.
        if rating_str.replace('.', '', 1).isdigit():  # Replacing the first occurrence of the dot ('.') with an
            # empty string. This is done to check for decimal point for floating-point values. "1" as a third argument
            # means that only the first occurrence of the dot should be replaced. Finally, isdigit method checking
            # if all characters in the string are digits nad returns "True" otherwise "False"
            rating = float(rating_str)

            # If statement below checking if the current park is not already present in the "park_ratings"
            # dictionary. If it is not present , it adds a new entry with initial values for "total_rating"
            # and "count" set to 0. This ensures that the code can later accumulate and calculate the
            # total_rating and count for each park during the processing of reviews.
            if park not in park_ratings:
                park_ratings[park] = {'total_rating': 0, 'count': 0}

            park_ratings[park]['total_rating'] += rating
            park_ratings[park]['count'] += 1

    # Extracting the park names and calculate average ratings
    parks = list(park_ratings.keys())
    average_ratings = [park_ratings[park]['total_rating'] / park_ratings[park]['count'] for park in parks]

    # Setting up bar chart parameters
    bar_colors = ['green', 'yellow', 'black']  # Defining other than default colors for bars in the chart
    bar_width = 0.4  # Setting up width of the bar
    bar_edge_color = 'pink'  # Setting up bar edge color to "pink"

    # Similar to pie chart I'm setting up figure size for plotting to keep my preferred size of the plot
    plt.figure(figsize=(10, 5))

    # Creating "bars" variable to assign returned container of individual bar elements
    # set up earlier from function plt.bar()
    _ = plt.bar(parks, average_ratings, color=bar_colors, width=bar_width, edgecolor=bar_edge_color)

    # Creating labels and title for the plot
    plt.xlabel('Disneyland Park')
    plt.ylabel('Average Rating')
    plt.title('Average Review Scores for Each Disneyland Park')

    # Setting y- and x-axis limits and adding grid limits for better readability
    plt.ylim(0, 6)
    plt.grid(axis='y', linestyle='--', alpha=0.2)

    # Adding text labels on top of each bar in the bar chart. It uses the "enumerate()" function to iterate
    # over the index (i) and the corresponding value (value) of each element in the "average_ratings" list.
    for i, value in enumerate(average_ratings):
        plt.text(i, value + 0.1, f'{value:.2f}', ha='center', va='bottom')  # "i" is a x-coordinate
        # "value +1" is a y-coordinate a little bit above the bar, specify horizontal alignment at the
        # center and vertical alignment at the bottom of the text.
    plt.show()   # And finally this function display final visualisation of the bar chart based on all data above.

# Because code of below 2 functions is roughly similar to function above I will comment just blocks of code


def display_top_locations_bar_chart(reviews):  # This function analyzing and visualizing top 10 locations with
    # the highest average rating for a given park.

    # Getting user input for the park name (California, HongKong, Paris)
    park = input("Enter the park name (California, HongKong, Paris): ").lower()

    park_locations = {}  # Initializing an empty dictionary named "park_locations"

    # Iterating through each review and collecting data for the specified park
    for review in reviews:
        # Checking if the specified park is mentioned in the review's "Branch" attribute
        # lower() is used to convert both park and branch names to lowercase
        if park in review['Branch'].lower():
            # If the park is mentioned in the review, the code extracts the lowercase reviewer location
            # and the rating string from the review.
            location = review['Reviewer_Location'].lower()
            rating_str = review['Rating']

            if rating_str.isdigit():  # Checking if the "rating_string" is a digit
                rating = float(rating_str)  # Converting the "rating_string" to a float

                # If the location is not in the "park_locations" dictionary, adding it with initial values
                if location not in park_locations:
                    park_locations[location] = {'total_rating': 0, 'count': 0}

                # Updating the "total_rating" and "count" for the location in the "park_locations" dictionary
                park_locations[location]['total_rating'] += rating
                park_locations[location]['count'] += 1
    # Sorting the locations stored in the "park_locations" dictionary based on the average rating in
    # descending order and selecting the top 10 locations.
    # Specifying my own custom sorting key for the sorted() function.
    # Sorting is based on the average rating for each location.
    # I used lambda function again which takes a tuple x (key-value), accesses the value at index 1
    # and calculating the average rating by dividing "total_rating" by "count".
    sorted_locations = sorted(
        park_locations.items(),
        key=lambda x: x[1]['total_rating'] / x[1]['count'],
        reverse=True
    )[:10]

    # Initializing two empty lists to store capitalized location names and their average ratings
    capitalized_locations = []
    average_ratings = []

    for loc in sorted_locations:
        # Capitalizing the first letter of the location name obtained from the sorted locations.
        # Purpose of this is to keep consistent and visually appealing presentation of
        # location names when they are used later, when labeling the x-axis of the bar chart.
        capitalized_location = loc[0].capitalize()
        capitalized_locations.append(capitalized_location)

        # Calculating average ratings
        total_rating = loc[1]['total_rating']
        count = loc[1]['count']

        # Calculating the "average_rating" for a specific location. The "average_rating" is calculated
        # by dividing the "total_rating" for that location by the "count" of reviews from that location.
        # Also, a conditional check is done to avoid division by zero.
        if count > 0:
            average_rating = total_rating / count
        else:
            average_rating = 0

        average_ratings.append(average_rating)  # Adding the calculated "average_rating" for a specific reviewer
        # location to a list named "average_ratings". This list is used to store the average ratings for
        # top 10 locations with the highest average ratings in the specified park.

    # Plotting a bar chart
    plt.bar(capitalized_locations, average_ratings, color='#330000')  # using specified data and own color

    # Creating labels and title for the plot
    plt.xlabel('Reviewer Location')
    plt.ylabel('Average Rating')
    plt.title(f'Top 10 Locations with Highest Average Rating in {park.capitalize()}')

    plt.xticks(rotation=45, ha='right')  # Rotating x-axis labels for better readability and aligning them to the right
    plt.ylim(0, 6)  # Setting the y-axis by limiting values between 0 and 6
    plt.tight_layout()  # Adjusting layout for a clean and tight visualization
    plt.grid(axis='y', linestyle='--', alpha=0.2)  # Adding grid lines with a dashed line
    # and reduced opacity "alpha=0.2" making grid lines subtle and not obstructing data in the plot.
    for i, value in enumerate(average_ratings):  # As in previous function this block of code plays
        # similar function in this situation by annotating each bar with its corresponding average rating
        plt.text(i, value + 0.1, f'{value:.2f}', ha='center', va='bottom')
    plt.show()  # And finally displaying final visualisation of the bar chart based on all data above.


def plot_average_rating_by_month(reviews):  # This function takes a list of "reviews" for a specific park as input
    # and plots the average rating for a specific theme park over different months.
    park = input("Enter the park name (California, HongKong, Paris): ").lower()  # Asking the user to input
    # the park name (California, HongKong, Paris) and convert it to lowercase.

    # Filtering reviews based on the specified park and valid year-month format.
    filtered_reviews = []

    for review in reviews:
        # Checking if the park in the review's 'Branch' attribute matches the user input park, ignoring case.
        is_matching_park = park in review['Branch'].lower()
        # Checking if the 'Year_Month' field of the review has exactly one '-' character and
        # indicating a valid year-month format.
        is_valid_year_month = review['Year_Month'].count('-') == 1

        if is_matching_park and is_valid_year_month:
            filtered_reviews.append(review)  # If both conditions are met for a particular review,
            # that review is considered relevant and is appended to the "filtered_reviews" list.
            # This filtered list is then used for further calculations and visualization

    # Initializing a dictionary to store month-wise data, including total rating and count of reviews.
    month_data = {f"{i:02d}": {'total_rating': 0, 'count': 0} for i in range(1, 13)}

    # Iterating through each review in the filtered_reviews list.
    for review in filtered_reviews:
        year_month = review['Year_Month'].split('-')  # Extracting the year and month from the 'Year_Month' field of
        # the current "review".
        month = year_month[1].zfill(2)  # Retrieving the month part and fill it with leading zeros,
        # ensuring a consistent format for example "01"instead of "1", etc.
        # zfill(2) is a Python method and in this case is used to ensure that month part of date string has at least
        # two characters, adding zero to the left if it is one character only.
        rating_str = review['Rating']

        if rating_str.replace('.', '', 1).isdigit():  # These operations were already explained in function
            # plot_average_review_scores() (please see above)
            rating = float(rating_str)

            # Update the "month_data" dictionary with the "total_rating" and "count" for the current month.
            month_data[month]['total_rating'] += rating
            month_data[month]['count'] += 1

    average_ratings = {}

    # Iterating through the "month_data" dictionary, where each entry represents data for a specific month.
    for month, data in month_data.items():
        if data['count'] > 0:  # Checking if there are reviews for the current month
            average_ratings[month] = data['total_rating'] / data['count']   # Calculating the average rating for
            # the month by dividing the "total_rating" by the review "count".
        else:
            average_ratings[month] = 0  # If there are no reviews for the month, setting the average rating to 0.

    # Extracting the "months" and corresponding "average_rating_values" for plotting.
    months = list(average_ratings.keys())
    average_ratings_values = list(average_ratings.values())

    # Plotting the bar chart based on above calculations all arguments, methods and functions
    # I explained already on previous bar charts.
    plt.bar(months, average_ratings_values)
    plt.xlabel('Month')
    plt.ylabel('Average Rating')
    plt.title(f'Average Rating for {park.capitalize()} by Month')
    plt.ylim(0, 6)
    for i, value in enumerate(average_ratings_values):
        plt.text(i, value + 0.1, f'{value:.2f}', ha='center', va='bottom')
    plt.grid(axis='y', linestyle='--', alpha=0.2)
    plt.show()
