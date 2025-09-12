# Write a program that uses nested loops to collect data and
# calculate the average rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months,
# the total inches of rainfall, and the average rainfall per month for the entire period.

def rainfall():
    year_input = int(input("Please enter the number of years: "))
    month_range = range(1,13)
    inches_list = []
    for i in range(year_input):
        for j in month_range:
           inches = int(input("Please enter the rainfall in inches for each month of the year: "))
           inches_list.append(inches)
    num_months = len(inches_list)
    total_rainfall = sum(inches_list)
    avg_rainfall = total_rainfall / num_months
    print("Number of months: ", num_months)
    print("Total rainfall: ", total_rainfall, "inches")
    print("Average rainfall per month for the entire period: ", round(avg_rainfall,2))
rainfall()

