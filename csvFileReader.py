# program writen, created, cried over, yelled at in frustration,
# called many derogatory names, cried over again, and once used
# as the butt of a very bad joke made in poor taste by:
# Derek 'why did I sign up for this' Sleeper


def program_description():
    print('This program will take a csv file denoted\n'
          'by your input and create two files.\n'
          'The first file will be a copy of the original\n'
          'though having had any readings outside\n'
          'of your inputted specifications removed.\n'
          'The second file will be a list of the highest\n'
          'reading per hour from the data stored in the\n'
          'first document created by this program.\n'
          'The files will be named dependent on the name\n'
          'of the original file name. Thus if the \n'
          'original file name is "data", the first\n'
          'file will be "dataV" and the second "dataV-MAX.\n')


# this function captures the name of the file to have data retrieved from
# and verifies the file is able to be opened. it accounts for invalid
# input using error exception and a sentinel
def capture_source_file_name():
    verify = False
    while not verify:
        try:
            source_file_name = input('enter source file name')
            open(source_file_name)
        except IOError:
            print('invalid file name')
        else:
            verify = True
            return source_file_name


# this function captures the limiting value for the variable
# that has called it. it accounts for invalid
# input using error exception and a sentinel
def capture_value_limit(limit):
    verify = False
    while not verify:
        try:
            limit = float(input('value'))

        except ValueError:
            print('invalid input')
        else:
            verify = True
            return limit


# this function verifies the data reading is within the user defined bounds
def verify_value_limit(reading, upper_limit, lower_limit):
    upper_limit = str(upper_limit)
    lower_limit = str(lower_limit)
    if reading <= upper_limit and reading >= lower_limit:
        return True
    else:
        return False


# this loop takes the data line from the original document and filters
# out any data values not with the user defined range and creates a
# new document with only valid readings entitled 'filename'V
def write_to_corrected_value(source_file, corrected_value, upper_limit, lower_limit):

    data_line = source_file.readline()
    data_line = source_file.readline()
    reading = data_line[23:]

    while data_line != '':
        reading = data_line[23:]
        if verify_value_limit(reading, upper_limit, lower_limit):
            corrected_value.write(data_line)
#            print(data_line)
            data_line = source_file.readline()
        else:
            print('outside range')
            data_line = source_file.readline()


# this loop combs the valid data document created by this program
# and sorts for highest value within a given hour by time stamp
# reading. It prints this hourly high to a 'filename'V-MAX document.
def write_to_sink_file(corrected_value, sink_file):

    data_line = corrected_value.readline()
    old_hour = data_line[12:14]
    old_reading = data_line[23:]

    while data_line != '':

        date = data_line[1:11]
        new_hour = data_line[12:14]
        new_reading = data_line[23:]

        if new_hour == old_hour:
            if new_reading >= old_reading:
                old_reading = new_reading
                data_line = corrected_value.readline()
            else:
                data_line = corrected_value.readline()
        else:
            sink_file.write(date+', '+old_hour+', ')
            sink_file.write(old_reading+'\n')
            old_hour = new_hour
            old_reading = ''
            data_line = corrected_value.readline()


# the main function stores most variable information to be passed back and forth
# through the program. In this case also making sure files are opened, created,
# amended, and closed in the appropriate order.
def main():
    program_description()
    source_file_name = capture_source_file_name()
    source_file = open(source_file_name, 'r')
    index = source_file_name.find('.')
    corrected_value = open(source_file_name[:index]+'V'+source_file_name[index:], 'a')
    sink_file = open(source_file_name[:index]+'V-MAX'+source_file_name[index:], 'a')

    limit = ''
    print('please enter maximum')
    upper_limit = capture_value_limit(limit)
    print('please enter minimum')
    lower_limit = capture_value_limit(limit)

    write_to_corrected_value(source_file, corrected_value, upper_limit, lower_limit)
    source_file.close()
    corrected_value.close()
    corrected_value = open(source_file_name[:index] + 'V' + source_file_name[index:], 'r')
    write_to_sink_file(corrected_value, sink_file)
    sink_file.close()

main()


# I started this assignment by making a copy of functional requirements.
# and continued by writing out flow charts. Lots and lots of flow charts.
# then writing the flow charts into psuedo code.

# I got stuck all over the place on this assignment. I had trouble with
# ordering the file open and close timing. I had trouble with getting the
# format of the output correct. As in spaces and commas and new lines
# all in the right places. I had trouble with getting the naming scheme
# to work no matter the name of the original text file. Though by a long
# long way the problem I struggled with the most was the core loops of the
# program. As it turns out, I struggled because I was trying to accomplish
# too much with a single loop. I couldn't sort out hoe to filter and loop
# simultaneously. I got unstuck with the hint that I should break the loop
# up into two separate loops. What had defeated me for days, suddenly fell
# into place as I stopped beating my head against a wall and managed to
# start unravelling the knot I had created. So, thank you for your help.

# tested this program in pieces once it was larger than a few definitions.
# I now keep a second instance open while I am working entitled sandbox.
# I can look at a problem or something I wish to alter in the primary window
# move a copy over to the sandbox and work with it there. Once I have the
# piece in sandbox working as it should, I copy the hole program to sandbox
# and work on integration there. Once integrated I move the whole concoction
# back into the main window and replace the old program with the new one.

# I learned the importance of file I/O timing and exactly why working
# on thing individually as functions is so beneficial. Though I think
# the biggest takeaway I have is not trying so hard. I focused on making
# the program do what I had writen down that I wasn't able to see that
# it was far from the best way to do it. I will definitely be more aware
# of this danger moving forward.

# next time, I will try more variations on flow before psuedo coding
# and keep variations on psuedo code before moving into coding proper.
# I will also implement the use of my sandbox much earlier as well.
