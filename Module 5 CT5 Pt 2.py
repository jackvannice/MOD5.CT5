# The CSU Global Bookstore has a book club
# that awards points to its students based on the
# number of books purchased each month.
# The points are awarded as follows:
# If a customer purchases 0 books, they earn 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.
# Write a program that asks the user to enter the number of books
# that they have purchased this month
# and then display the number of points awarded

def bookstore():
    while True:
        try:
            num_books = int(input("How many books did you purchase this month? "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    if num_books < 0:
        print("Please input a valid number of books (non-negative integer)")
    elif 0 <= num_books < 2:
        print("Not enough books purchased, you have not earned any points")
    elif 2 <= num_books < 4:
        print("Congratulations, you have purchased enough books for 5 points")
    elif 4 <= num_books < 6:
        print("Congratulations, you have purchased enough books for 15 points")
    elif 6 <= num_books < 8:
        print("Congratulations, you have purchased enough books for 30 points")
    elif num_books >= 8:
        print("Congratulations, you have purchased enough books for 60 points")
    else:
        print("N/A")

bookstore()


