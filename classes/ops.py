# ops.py file for OOP - Class to accomplish last assessment point

class Ops:  # Defining a new class named "Ops"

    def __init__(self, name):  # Defining the constructor method "__init__", which is called when
        # a new instance of the class is created.
        # It takes self and name as parameters.
        self.name = name  # Initializing instance variable "name" with the value passed as a parameter to constructor.
        self.reviews_list = []  # Initializing an instance variable "reviews_list" as an empty list.
        # This list will be used to store reviews.

    def add_review(self, review):  # Defining a method named "add_review" which takes "self" and "review" as parameters.
        self.reviews_list.append(review)  # Appending the provided "review" to the "reviews_list" of the instance.

    def get_aggregate_info(self):  # Defining a method named "get_aggregate_info" which takes self as a parameter.
        num_reviews = len(self.reviews_list)  # Calculating the total number of reviews by getting the length
        # of the "reviews_list".
        num_positive_reviews = 0  # Initializing a counter for the number of positive reviews
        for review in self.reviews_list:  # Checking if the rating of the current review is greater than or equal to 4.
            # I assumed positive reviews are 5s and 4s only. If statement is "True" then "num_positive_reviews" is
            # increased by 1
            if int(review['Rating']) >= 4:
                num_positive_reviews += 1

        average_score = 0  # Initializing the variable average_score to 0.
        if num_reviews > 0:  # Checking if there are reviews - to avoid division by zero
            total_score = 0  # Initializing a variable "total_score" to calculate the sum of all review ratings.

            for review in self.reviews_list:  # This loop iterating through each "review" in the "reviews_list".
                # If the current "review" has a "Rating" key and if the condition is "True", adding the integer value
                # of the rating to the "total_score".
                if 'Rating' in review:
                    total_score += int(review['Rating'])

            average_score = total_score / num_reviews  # Simply calculating the "average_score" by dividing the
            # "total_score" by the number of reviews "num_reviews".

        reviewer_locations = set()  # Initializing an empty set to store unique "reviewer_locations".
        for review in self.reviews_list:  # Simply iterating through each "review" in the "reviews_list"
            if 'Reviewer_Location' in review:  # Checking if the current review has a "Reviewer_Location" key.
                reviewer_locations.add(review['Reviewer_Location'])  # If the condition is "True", adding the
                # reviewer's location to the set of unique locations.

        num_countries = len(reviewer_locations)  # Calculating the number of unique countries "num_countries" by
        # getting the length of the set of "reviewer_locations".

        # Returning a dictionary of aggregate information:
        # total number of reviews, number of positive reviews, average review score,
        # and number of unique countries reviewed.
        return {
            'Number of reviews': num_reviews,
            'Number of positive reviews': num_positive_reviews,
            'Average review score': average_score,
            'Number of countries reviewed': num_countries
        }
