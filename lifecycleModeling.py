
def main():

    # Simple function to give the user an idea of what the program will
    # do and what input will be required.
    def display_program_function():
        print('This program will take the information\n'
              'from the file you specify and model cell states\n'
              'for a number of generations(iterations) that\n'
              'you will specify.\n')

    # This function captures user input for the fill name to be opened
    # while accounting for incorrect input.
    def capture_cell_file_name():

        # Loop gate
        verify = False
        while not verify:
            try:
                # cell_file_name = 'cell_file.txt'
                cell_file_name = input('Please enter the source file name: ')
                print('')
                open(cell_file_name)
            except IOError:
                print('Invalid source file name.\n')
            else:
                verify = True
                return cell_file_name

    # This function takes the name of the file specified and creates the
    # start conditions of the program based on the information contained within
    # specified file by reading the first three lines and assigning the read value to
    # a list. The value read on the fourth line is assigned to a separate
    # variable which then duplicates and append the list the number of times
    # specified by the fourth line
    def create_cell_start_conditions():
        cell_file = open(cell_file_name)
        cell_row = []
        cell_pattern_repeat = 0

        cell_row.append(cell_file.readline().rstrip())
        cell_row.append(cell_file.readline().rstrip())
        cell_row.append(cell_file.readline().rstrip())

        cell_pattern_repeat = int(cell_file.readline().rstrip()) - 1

        # This is the list extension loop
        while cell_pattern_repeat > 0:
            cell_row.append(cell_row[0])
            cell_row.append(cell_row[1])
            cell_row.append(cell_row[2])

            cell_pattern_repeat -= 1

        cell_file.close()

        return cell_row

    # This function captures the number of generations the user wishes to model.
    # It only accepts positive integer values and attempts to communicate this clearly to the user.
    def capture_number_of_cycles():

        # Loop gate
        verify = True
        while verify:
            try:
                number_of_cycles = int(input('please enter a positive integer for how many generations\n'
                                             'you would like to have modeled: '))
                print('')

            except ValueError:
                print('Invalid input. Non integer value.\n')
            else:
                if number_of_cycles < 0:
                    print('Invalid input. Integer must be positive.\n')
                    continue
                else:
                    verify = False
                    return number_of_cycles

    # The functions through out this program deal in strings as the preferred data structures
    # within the lists. However, the output of the program needs to be only a graphical
    # representation of the information. This function converts the states of 'alive' and 'dead'
    # to + and whitespace respectively by creating a new list for display purposes only.
    # It then immediately displays the converted information.
    def convert_and_display(cell_row):
        cell_display = []

        for position in range(len(cell_row[:])):
            if cell_row[position] == 'alive':
                cell_display.append('+')
            else:
                cell_display.append(' ')

        join = ''
        print(join.join(cell_display))

    # This is the core function of the program and as such contains the algorithm
    # which models the cell states for each generation. This algorithm does this by
    # comparing values of one cell's state with the state of it's neighbors. It then
    # created a new list with those recorded states, replaces the old list with the new
    # and repeats the number of times specified. In the case of the first, and last,
    # cell in the list, the algorithm uses predefined proxies for the missing neighbor.
    # This algorithm does only function linearly. Not that it matters, or that it could
    # do otherwise, but it seems important to note.
    def automate_cells(cell_row, number_of_cycles):

        # predefined cell states and variable initilization
        flc = 'dead'
        frc = 'dead'
        new_cell_row = []

        # Controlled loop
        while number_of_cycles > 0:

            # check for first cell in list
            if cell_row[0] == flc == cell_row[1]:
                new_cell_row.append('alive')
            else:
                new_cell_row.append('dead')

            # Loop for all cells except first and last
            for position in range(len(cell_row[0:-1])):
                if position == 0:
                    continue
                elif cell_row[position] == cell_row[position - 1] == cell_row[position + 1]:
                    new_cell_row.append('alive')
                else:
                    new_cell_row.append('dead')

            # Check for last cell in list
            if cell_row[len(cell_row) - 1] == frc == cell_row[len(cell_row) - 2]:
                new_cell_row.append('alive')
            else:
                new_cell_row.append('dead')

            # Conversion of new/old list and call for display of information
            cell_row = new_cell_row
            new_cell_row = []
            convert_and_display(cell_row)

            # Loop flag
            number_of_cycles -= 1

    display_program_function()

    cell_file_name = capture_cell_file_name()

    cell_row = create_cell_start_conditions()

    number_of_cycles = capture_number_of_cycles()

    convert_and_display(cell_row)

    automate_cells(cell_row, number_of_cycles)

main()


# I began this assigned by focusing on the logic of the automation of the cell list.
# This seemed like it would be the hardest part and I felt that I already had a bag of tricks
# to pull from in regard to the other functions that would be needed to compete the program
# I got hung up in getting the automation loop to read and function properly. I looked for
# a long time at how else I could set up the function I wanted and did not get very far
# at all. When I remembered how the range(len()) syntax needed to be set up. Once that was
# in place, it was just tweaking the allowed domain from the list to solve the rest of the
# problem. The next big challenge was actually sorting the methodology for creating the list
# of the start conditions. I had something that kind of worked, that developed into two
# separate functions that later collapsed back into a single function. When I tried nesting
# multiple methods and it worked I was supper excited. I think it's my favorite part of this
# programs code actually. The last big hurdle was the display function. I was caught up trying
# to get the .strip() method to accomplish what I was looking to do. Once I started looking
# outside of that particular function, it came together in minutes. I think the lesson there
# is when you're beating your head against a wall, that you should find another wall and hope
# it's softer. Good life lesson, that. In general, the constant testing, tweaking, moving,
# rewriting, and various other experiments, have proven how invaluable my Sandbox is. Having
# a separate place to work on functions and algorithms without having to involve
# the entirety of the program is probably the most procedurally useful thing I will be taking
# from this experience.







