def calculate_running_total():
    total_sum = 0
    count_of_numbers = 0

    while total_sum < 100:
        user_input = input("Enter a number (or just press enter to finish): ")
        
        if user_input.strip() == "":
            break

        try:
            number = float(user_input)
            total_sum += number
            count_of_numbers += 1
        except ValueError:
            print("Please enter a valid number or just press enter to finish.")

    return total_sum, count_of_numbers

# Main program execution
if __name__ == "__main__":
    total_sum, count_of_numbers = calculate_running_total()
    print(f"The total sum is: {total_sum}")
    print(f"The count of numbers entered is: {count_of_numbers}")
