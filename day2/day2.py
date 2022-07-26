""""number"""
def main():
    result = 0
    value_input = int(input())
    if value_input == 0:
        return print("No Tape Measure")
    input_list=[str(number + 1) for number in range (value_input)]
    for _ in range (value_input):
        value=input()
        if value == "No more":
            break
        if value in input_list:
            result += int(value)

    if result == 0:
        print("Not Found Number")
    else:
        print("Sum of Found Number = %d" %result )

main()