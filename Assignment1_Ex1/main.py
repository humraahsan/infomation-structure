# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_student_data(name, course, score):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name},  {course}, {score}' )  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # define list
    for i in range(3):
        data = input("enter data for students:")
        # add data to the list
    # iterate list
        splitted_string = data.split(",")

        print_student_data(splitted_string[0], splitted_string[1], splitted_string[2])



# See PyCharm help at https://www.jetbrains.com/help/pycharm/


