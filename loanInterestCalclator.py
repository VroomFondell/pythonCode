# program to determine loan payments and interest paid

def main():

    # intro to user and get user input
    print("Welcome to the loan calculator. This program will calculate your monthly payment,")
    print("total interest paid, and will also show you the results for a loan amount plus or minus ten percent.")
    print()
    print()
    amount = float(input("Please input the amount of the loan: $"))
    rate_input = float(input("Please input the interest rate of loan in whole number form: "))
    number_years = float(input("Please input the number of years of the loan term: "))

# conversions

    # calculate the number of months based on years
    number_months = number_years * 12

    # calculate the loan rate based on real estate site for converting interest based on months, not years
    rate_yearly = rate_input / 100
    rate = rate_yearly * .08333

    # adjust amount of loan to show user + 10%
    amount_plus10 = amount * 1.1

    # adjust amount of loan to show user - 10%
    amount_minus10 = amount * .9



# call section

    # call monthly pay function with user-entered amount
    # assign return value to monthly_payment
    monthly_payment = monthly_pay(amount, rate, number_months)

    # call monthly pay function with amount_plus10 to get +10% monthly payments
    # assign return value to monthly_payment_plus10
    monthly_payment_plus10 = monthly_pay(amount_plus10, rate, number_months)

    # call monthly pay function with amount_minus10 to get -10% monthly payments
    # assign return value to monthly_payment_minus10
    monthly_payment_minus10 = monthly_pay(amount_minus10, rate, number_months)

    # call total int paid function to find total interest paid
    # assign return value to total_paid
    total_paid = total_int_paid(amount, monthly_payment, number_months)

    # call total int paid function to find total interest paid based on + 10% amount
    # assign return value to total_paid_plus10
    total_paid_plus10 = total_int_paid(amount_plus10, monthly_payment, number_months)

    # call total int paid function to find total interest paid based on - 10% amount
    # assign return value to total_paid_minus10
    total_paid_minus10 = total_int_paid(amount_minus10, monthly_payment, number_months)

    display(monthly_payment, total_paid, amount, rate_input, number_years, monthly_payment_plus10,
            monthly_payment_minus10, total_paid_plus10, total_paid_minus10)

# calculate monthly payments based on user entered data, or adjusted amounts
def monthly_pay(amount, rate, number_months):
    payment = (amount * rate) / (1 - (1 + rate) ** - number_months)
    return payment

# calculate total interest paid based on user entered data, or adjusted amounts
def total_int_paid(amount, monthly_payment, number_months):
    inter_paid = number_months * monthly_payment - amount
    return inter_paid


def display(monthly_payment, total_paid, amount, rate_input, number_years, monthly_payment_plus10,
            monthly_payment_minus10, total_paid_plus10, total_paid_minus10):
    print()
    print()
    print('Amount of loan entered: $', format(amount, '.2f'))
    print('Interest rate entered: ', format(int(rate_input)), '%')
    print('Loan term entered:', format(int(number_years))),
    print()
    print("Monthly payment for original loan amount is: $", format(monthly_payment, '.2f'))
    print("Total interest for original loan amount paid is: $", format(total_paid, '.2f'))
    print()
    print("Monthly payment for original loan amount plus 10% is: $", format(monthly_payment_plus10, '.2f'))
    print("Total interest paid for original loan amount plus 10% is: $", format(total_paid_plus10, '.2f'))
    print()
    print("Monthly payment for original loan amount minus 10% is: $", format(monthly_payment_minus10, '.2f'))
    print("Total interest paid for original loan amount minus 10% is: $", format(total_paid_minus10, '.2f'))


main()

# I started by banging my head on the desk. A lot. Then I wrote out a general flow chart followed by a list of needed
# variables.

# I had a hard time sorting out the conversion of the interest rates from yearly to monthly.
# And problems understanding the moving of information from arguments to other arguments.
# I got stuck a lot with understanding that order matters more than variable name in passing information
# between functions.

# I'm still struggling with the formatting matting of the display output. Deleting the whitespace and creating
# new lines is eluding me.

# I certainly gained a deeper understanding of the movement of information through functions.
# next go around I will spend more time drawing pictures and flow charts with lots  of lines mapping out
# where information is coming from and going to.

# Getting unstuck this week required recovering from a few days of panic attacks and significant tutoring really.
