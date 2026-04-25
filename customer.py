'class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.packages = []
        self.booked_classes = []

    def register(self):
        # Registration logic (e.g., save user data to the database)
        print(f"{self.username} registered successfully!")

    def login(self, password):
        if password == self.password:
            print(f"{self.username} logged in successfully!")
            return True
        else:
            print("Invalid password!")
            return False

    def add_package(self, package_name):
        self.packages.append(package_name)
        print(f"Package '{package_name}' added.")

    def remove_package(self, package_name):
        if package_name in self.packages:
            self.packages.remove(package_name)
            print(f"Package '{package_name}' removed.")
        else:
            print(f"Package '{package_name}' not found.")

    def book_class(self, class_name):
        self.booked_classes.append(class_name)
        print(f"Class '{class_name}' booked.")

    def view_packages(self):
        print("Available Packages:")
        for package in self.packages:
            print(f"- {package}.")

    def view_bookings(self):
        print("Booked Classes:")
        for class_name in self.booked_classes:
            print(f"- {class_name}.")

# Example Usage
if __name__ == "__main__":
    customer = Customer("john_doe", "secure_password")
    customer.register()
    if customer.login("secure_password"):
        customer.add_package("Premium Membership")
        customer.book_class("Yoga Class")
        customer.view_packages()
        customer.view_bookings()'