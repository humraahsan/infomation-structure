# Assignment1
def print_student_data(name, course, score):
    print(f'{name}  {course} {score}')

if __name__ == '__main__':
    # define list
    student_info = []
    for i in range(2):
        data = input("enter data for student:")
        # add data to the list
        student_info.append(data)
    # iterate list
    for j in student_info:
        splitted_string = j.split(",")
        print_student_data(splitted_string[0], splitted_string[1], splitted_string[2])
