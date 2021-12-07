#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

print("Number Sorter!")

#ask user input

def input_numbers():
    number_1 = int(input('Enter the 1st number: '))
    number_2 = int(input('Enter the 2nd number: '))
    number_3 = int(input('Enter the 3rd number: '))
    number_4 = int(input('Enter the 4th number: '))
    return number_1, number_2, number_3, number_4
  
first, second, third, fourth = input_numbers()
print(f'The numbers you enter, {first}, {second}, {third}, {fourth}')

#solve highest, midhigh, midlow, lowest number
def number_sorter_1() :
    if first > second and first > third and first > fourth:
        print(f"The highest number is", first)
        if second > third and second > fourth:
            print(f"The second to the highest number is", second)
            if third > fourth:
                print(f"The third to the highest number is", third)
                print(f"The lowest number is", fourth)
            else:
                print(f"The third to the highest number is", fourth)
                print(f"The lowest number is", third)
        elif third > second and third > fourth:
            print(f"The second to the highest number is", third)
            if second > fourth:
                print(f"The third to the highest number is", third)
                print(f"The lowest number is", fourth)
            else: 
                print(f"The third to the highest number is", fourth)
                print(f"The lowest number is", third)
        elif fourth > second and fourth > third:
            print(f"The second to the highest number is", fourth)
            if second > third:
                print(f"The third to the highest number is", second)
                print(f"The lowest number is", third)
            else:
                print(f"The third to the highest number is", third)
                print(f"The lowest number is", second)

def number_sorter_2() :
    if second > first and second > third and second > fourth:
        print(f"The highest number is", second)
        if first > third and first > fourth:
            print(f"The second to the highest number is", first)
            if third > fourth:
                print(f"The third to the highest number is", third)
                print(f"The lowest number is", fourth)
            else:
                print(f"The third to the highest number is", fourth)
                print(f"The lowest number is", third)
        elif third > first and third > fourth:
            print(f"The second to the highest number is", third)
            if first > fourth:
                print(f"The third to the highest number is", first)
                print(f"The lowest number is", fourth)
            else:
                print(f"The third to the highest number is", fourth)
                print(f"The lowest number is", first)
        elif fourth > first and fourth > third:
            print(f"The lowest_number", fourth)
            if first > third:
                print(f"The third to the highest number is", first)
                print(f"The lowest number is", third)
            else:
                print(f"The third to the highest number is", third)
                print(f"The lowest number is", first)

def number_sorter_3() :
    if third > first and third > second and third > fourth:
        print(f"The highest number is", third)
        if first > second and first > fourth:
            print(f"The second to the highest number is", first)
            if second > fourth:
                print(f"The third to the highest number is", second)
                print(f"The lowest number is", fourth)
            else:
                print(f"The third to the highest number is", fourth)
                print(f"The lowest number is", second)
        elif second > third and second > fourth:
            print(f"The second to the highest number is", second)
            if third > fourth:
                print(f"The third to the highest number is", third)
                print(f"The lowest number is", fourth)
            else:
                print(f"The third to the highest number is", fourth)
                print(f"The lowest number is", third)
        elif fourth > first and fourth > second:
            print(f"The lowest number is", fourth)
            if first > second:
                print(f"The third to the highest number is", first)
                print(f"The lowest number is", second)
            else:
                print(f"The third to the highest number is", second)
                print(f"The lowest number is", first)

def number_sorter_4() :
    if fourth > first and fourth > second and fourth > third:
        print(f"The highest number is", fourth)
        if first > second and first > third:
            print(f"The second to the highest number is", first)
            if second > third:
                print(f"The third to the highest number is", second)
                print(f"The lowest number is", third)
            else:
                print(f"The third to the highest number is", third)
                print(f"The lowest_number", second)
        if second > first and second > third:
            print(f"The second to the highest number is", second)
            if first > third:
                print(f"The third to the highest number is", first)
                print(f"The lowest number is", third)
            else:
                print(f"The third to the highest number is", third)
                print(f"The lowest number is", first)
        if third > first and third > second:
            print(f"The second to the highest number is", third)
            if first > second:
                print(f"The third to the highest number is", first)
                print(f"The lowest number is", second)
            else:
                print(f"The third to the highest number is", second)
                print(f"The lowest number is", first)

def display_output() :
    number_sorter_1()
    number_sorter_2()
    number_sorter_3()
    number_sorter_4()

display_output()