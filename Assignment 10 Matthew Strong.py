# CSCI 1300 Fall 2017
# Author: Matthew Strong
# Recitation: Recitation 201
# TA: Arcadia Zhang
# Assignment 10, Problem 1

# PART_1 functions here

# here is the first function
# This first function reads books based on a certain filename.
# It reads a specific file form the user and creates a list of books based on that information

def read_books(file_name):
    try:
        book_list = []
        fr = open(file_name)
        #  initializes the book list and sets it to be empty.
        for line in fr:
            # Goes through every line in the file, strips it (also
            # it the length is 0, we return an empty dictionary
            # Otherwise, we keep going and then split the line
            # Then, we set parts of the line to the author and book,
            # Then place all of that information into an array.

            line = line.strip()
            if len(line) == 0:
                return []
            booked = line.split(",")
            change = booked[0]
            changer = booked[1]
            narray = [changer, change]
            book_list.append(narray)
        # returns the whole list of books
        return book_list
    # In the events that the file does not open.
    except IOError:
        return None

# This function reads the users as well as their ratings and puts everything into a dictionary to use.
def read_users(file_name):
    try:
        # sets an empty dictionary to have nothing in it.
        dictionary = {}
        # opens the file
        fr = open(file_name)
        for line in fr:
            # Loops through each line in the file, strips it, and then splits it
            # Then we have where if the size of the line is 0, to return an empty dictionary
            # Next, the first item in the split array is the name
            line = line.strip()
            if len(line) == 0:
                return {}
            user = line.split()
            name = user[0]
            for i in range(1, len(user)):
                user[i] = int(user[i])
                # for every item in the split array, everything except the first item,
                # is set to the numbers associated with that user
            numbers = user[1:len(user)]
            # then a new key is created with all of the numbers being the corresponding values.
            dictionary[name] = numbers
        # the dictionary is now returned
        return dictionary
    except IOError:
        # in the event that the file does not open
        return None

# this function calculates the average rating of each book given the dictionary of users along with their ratings,
# here, this function, in terms of logic, was the most challenging to complete.
def calculate_average_rating(ratings_dict):
    try:
        # opening the file, to see if it works
        # then I hae an empty average list.
        # first I loop through the ratings dictionary and get the length of a key,
        # since the length of each key is the same, the length value will never change even as
        # I loop through each key in the ratings dictionary
        avglist = []
        for key in ratings_dict:
            length = len(ratings_dict[key])
        # looping through every value in the ratings
        for i in range(0, length):
            # l will be what I divide by to obtain the average.
            l =0
            # sets the sum of all of the ratings in each book to 0.
            sum = 0
            for key in ratings_dict:
                # loops through each key in the ratings dictionary ,
                # and if at a certain key, the rating is not 0, then l is increased by 1
                # and the rating is added to the sum, which grows as the loop progresses.
                if ratings_dict[key][i] != 0:
                    sum = sum + ratings_dict[key][i]
                    l = l + 1
            # ensures that the sum will be z float, so when the average is the sum divided by l,
            # the average will be a float.
            sum = sum * 1.0
            average = sum / l
            # appending the average to the average list.
            avglist.append(float(average))
        # returning the list
        return avglist
    # if anything might go wrong, None is returned.
    except:
        return None
# this function looks up the average of a book given an index, the book dictionary, and the average ratings dictionary
# and then returns a string in correct format that will display the average rating of a certain book along with the
# authror
def lookup_average_rating(index, book_dict, avg_ratings_dict):
    i = index
    array = book_dict[i]
    book = array[0]
    author = array[1]
    # sets the book to the first item of the array and the author to the second item of the array based
    # on the book dictionary
    # then sets the variable score equal to item at index i in the average ratings dictionary
    score = avg_ratings_dict[i]
    # formats the variable string so that the correct format is ultimately returned.
    string = "(" + str(round(score, 2)) + ") " + book + " by " + author
    return string

# Part 2

class Recommender:
    # creating a constructor for the class with self, as well as two files, one
    # of which has the file of all of the books, and the other of which has the users and
    # their ratings.
    def __init__(self, books_filename, ratings_filename):
        # initializing every member of the class to empty list or dictionary
        # also calls three of the methods within the class to create a list of books and
        # dictionary of the ratings along with the users.
        self.book_list = []
        self.user_dictionary = {}
        self.average_rating_list = []
        self.read_books(books_filename)
        self.read_users(ratings_filename)
        self.calculate_average_rating()

    # this method is similar to the function declared outside of the class except that the book list
    # is a method of the class, so I will not explain this much as I only append to the book list
    # and this book list is a property, essentially, of one declaration of the class.
    def read_books(self, file_name):
        try:
            fr = open(file_name)
            for line in fr:
                line = line.strip()
                if len(line) == 0:
                    return []
                booked = line.split(",")
                change = booked[0]
                changer = booked[1]
                narray = [changer, change]
                self.book_list.append(narray)
                # note that nothing is retuned here.
        except IOError:
            return None

    # this method is also similar to the function declared outside of the class. Thus, the only minor differences
    # is that nothing is returned. The user dictionary is a member of this class, so it is similar to
    # one of the properties for the class. Additionally, nothing is returned from the method.
    def read_users(self, file_name):
        try:
            fr = open(file_name)
            for line in fr:
                line = line.strip()
                if len(line) == 0:
                    return {}
                user = line.split()
                name = user[0]
                for i in range(1, len(user)):
                    user[i] = int(user[i])
                numbers = user[1:len(user)]
                self.user_dictionary[name] = numbers
        except IOError:
            return None

    # this method is also similar to the function outside of the class. The only differences
    # is that nothing is returned. I also had to use some of the data members in this class
    # to add to my average rating list. There was some reformatting that had to be done with adding
    # to each value in average list to ensure that there was not too many decimal places.
    def calculate_average_rating(self):
        for key in self.user_dictionary:
            length = len(self.user_dictionary[key])
        for i in range(0, length):
            l = 0
            sum = 0
            for key in self.user_dictionary:
                if self.user_dictionary[key][i] != 0:
                    sum = sum + self.user_dictionary[key][i]
                    l = l + 1
            sum = sum * 1.0
            average = sum / l
            self.average_rating_list.append("%.2f" % average)
            # nothing is returned here

    # this method is similar to the last function outside of the class,
    # and the logic is the same, except for the members of the class
    def lookup_average_rating(self, book_index):
        i = book_index
        array = self.book_list[i]
        book = array[0]
        author = array[1]
        score = self.average_rating_list[i]
        string = "(" + str(score) + ") " + book + " by " + author
        return string

    # this method calculates the similarity between two users by using the dot product between every rating of the user
    # and the other users
    def calc_similarity(self, user1, user2):
        # based on the users dictionary, each user has their array of ratings
        # and two variables are created
        # I use the dot product to increase the dot product to where it eventually has been
        # fully calculated. From here, this dot product is returned after every rating has been gone through
        # for each user
        first = self.user_dictionary[user1]
        second = self.user_dictionary[user2]
        dot = 0
        for i in range(0, len(first)):
            dot = dot + (first[i] * second[i])
        return dot

    # this method calculates the most similar user based on the name of the current user
    def get_most_similar_user(self, current_user_id):
        # setting the highest score to 0 and the best user to an empty string
        highestscore = 0
        bestuser = ""
        for key in self.user_dictionary:
            # looping through each key in the user ratings dictionary and seeing if the similarity score between that
            # key and user is higher than the current highestscore (also the current user cannot be the key, as that
            # would be the same user). If the requirements for the preceding sentence are met,
            # the best user is now the key, and the new highest score is the similarity score
            if self.calc_similarity(current_user_id, key) > highestscore and current_user_id != key:
                highestscore = self.calc_similarity(current_user_id, key)
                bestuser = key
        # after going through every key in the user ratings dictionary, the best user will have been returned
        return bestuser

    # this method is the most fun and will return a list of the recommended books for that user
    def recommend_books(self, current_user_id):
        # finds the best user based on the current user
        bestuser = self.get_most_similar_user(current_user_id)
        # setting two variables to the ratings for the current user and the best user
        books = self.user_dictionary[bestuser]
        mybooks = self.user_dictionary[current_user_id]
        recommend = []
        for i in range(0, len(books)):
            # for every item in the array of ratings for the best user,
            # if the rating in the current user array is 0, and if the rating
            # for the best user is 3 or above,
            # then lookup_average_rating method is called and set to a string
            # and that string is added to the list of recommended
            # books
            # then the list is returned
            if mybooks[i] == 0:
                if books[i] >=3:
                    string = self.lookup_average_rating(i)
                    recommend.append(string)
        return recommend


def main():
    # here is all of the test cases for the main, which I was able to draw from the examples that were given us.
    book_list = read_books("books.txt")

    user_dict = read_users("rating1.txt")
    print(book_list)
    print(user_dict)

    ave_rating_list = calculate_average_rating(user_dict)
    print(ave_rating_list)
    print(lookup_average_rating(0, book_list, ave_rating_list))



    r = Recommender("book.txt", "ratings.txt")


    print(r.calc_similarity('Cust8', 'Shannon'))
    print(r.calc_similarity('Megan', 'Strongbad'))
    print(r.calc_similarity('Apollo', 'James'))
    print(r.lookup_average_rating(0))
    print(r.lookup_average_rating(54))
    print(r.lookup_average_rating(10))
    print(r.get_most_similar_user("Leah"))
    print(r.get_most_similar_user("KeeLed"))
    print(r.get_most_similar_user("Rudy.A"))
    print(r.recommend_books("Brian"))
    print(r.recommend_books("Megan"))

    print(r.recommend_books("Tiffany"))

    print(r.recommend_books("Moose"))




if __name__ == "__main__":
    main()
