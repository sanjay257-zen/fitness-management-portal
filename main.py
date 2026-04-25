def main_menu():
    print("Welcome to the Fitness Management Portal!")
    print("1. View Fitness Programs")
    print("2. Create New Membership")
    print("3. Schedule a Training Session")
    print("4. View Progress")
    print("5. Exit")

    choice = input("Please select an option (1-5): ")
    return choice

if __name__ == '__main__':
    while True:
        user_choice = main_menu()
        if user_choice == '1':
            print("Displaying Fitness Programs...")
        elif user_choice == '2':
            print("Creating a New Membership...")
        elif user_choice == '3':
            print("Scheduling a Training Session...")
        elif user_choice == '4':
            print("Viewing Progress...")
        elif user_choice == '5':
            print("Exiting the portal. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")