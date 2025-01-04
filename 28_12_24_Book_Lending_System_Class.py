from enum import Enum


class MenuOption(Enum):
    VIEW_AVAILABLE_BOOKS = 1
    BORROW_BOOK = 2
    RETURN_BOOK = 3
    VIEW_BORROWED_BOOK = 4
    EXIT = 5


class BookLendingSystem:
    def __init__(self):
        self.available_books = {
            1: "The Great Gatsby",
            2: "To Kill a Mockingbird",
            3: "1984",
            4: "Pride and Prejudice"
        }
        self.borrowed_books = {}

    @staticmethod
    def close_program():
        print('Closing program, thank you for using our services')
        exit()

    @staticmethod
    def confirm_integer_input(user_input):
        """Helper function to confirm user input was a digit by checking if convertible to integer
        Converts user input to integer datatype as well"""
        try:
            return int(user_input)
        except ValueError:
            raise ValueError("Invalid choice, please make sure to provide an integer input")

    @staticmethod
    def confirm_book_range_validity(user_input, primary_dict, secondary_dict, primary_error, secondary_error):
        """Validates the range of a book choice.
        Note that this approach avoids the use of nested ifs"""
        user_input = int(user_input)  # Ensure it's an integer before proceeding
        if user_input in secondary_dict.keys():
            raise ValueError(primary_error)
        elif user_input not in primary_dict.keys():
            raise ValueError(secondary_error)

    @staticmethod
    def display_start_menu():
        """Prints out menu options for user to select from"""
        print("\nAvailable actions")
        for option in MenuOption:
            print(option.value, option.name.replace('_', ' ').capitalize())

    @staticmethod
    def confirm_input_range_validity(user_input):
        """Helper function to confirm user input is within range of choice"""
        if user_input not in [option.value for option in MenuOption]:
            raise ValueError('Choice out of specified range. Please try again')

    def obtain_user_display_menu_choice(self):
        """Method to obtain user choice from the display menu options.
        Method prompts for input, checks if digit, converts to integer, confirms if within valid range
        then returns integer version of user choice"""
        while True:

            user_input = input("Enter digit to choose action to perform: ").strip()

            if not user_input:
                print('Choice not detected, please try again')

                continue

            try:
                user_choice = BookLendingSystem.confirm_integer_input(user_input)

                self.confirm_input_range_validity(user_choice)

                return MenuOption(user_choice)

            except ValueError as e:
                print(e)

    def view_borrowed_books(self):
        """Displays a list of borrowed books"""
        [print(i, self.borrowed_books[i]) for i in self.borrowed_books.keys()]

    def borrow_book(self):
        while True:
            book_choice = input("Enter digit to choose the book that you wish to borrow: ").strip()

            if not book_choice:
                print('Book choice not detected, please try again')

                continue

            try:
                book_choice = BookLendingSystem.confirm_integer_input(book_choice)

                BookLendingSystem.confirm_book_range_validity(book_choice, self.available_books, self.borrowed_books,
                                                              'Book already borrowed. Please try again',
                                                              'Book choice out of specified range. Please try again')

                borrowed_book = self.available_books.pop(book_choice)
                self.borrowed_books[book_choice] = borrowed_book

                print(f"You have successfully borrowed: {borrowed_book}")
                break
            except ValueError as e:
                print(e)

    def view_available_books(self):
        """Displays a list of available books"""
        print("\nAvailable books")
        [print(i, self.available_books[i]) for i in self.available_books.keys()]

    def return_book(self):
        while True:
            book_choice = input("Enter digit to choose the book that you wish to return: ").strip()

            if not book_choice:
                print('Book choice not detected, please try again')

                continue

            try:
                book_choice = BookLendingSystem.confirm_integer_input(book_choice)

                BookLendingSystem.confirm_book_range_validity(book_choice, self.borrowed_books, self.available_books,
                                                              'Book not borrowed yet. Please try again',
                                                              'Book choice out of specified range. Please try again')

                returned_book = self.borrowed_books.pop(book_choice)
                self.available_books[book_choice] = returned_book

                print(f"You have successfully returned: {returned_book}")
                break
            except ValueError as e:
                print(e)

    def execute_action(self, choice):
        """Executes user action depending on user choice
        Note how this approach promotes easy code extendability by following these three steps:
        1. Add new action item to the display menu
        2. Adding a method within the class to perform that new action item
        3. Adding the method for that action item in the actions dictionary"""
        actions = {
            MenuOption.VIEW_AVAILABLE_BOOKS: self.view_available_books,
            MenuOption.BORROW_BOOK: self.borrow_book,
            MenuOption.RETURN_BOOK: self.return_book,
            MenuOption.VIEW_BORROWED_BOOK: self.view_borrowed_books,
            MenuOption.EXIT: self.close_program
        }
        action = actions.get(choice)
        if action:
            action()
        else:
            print('Invalid action')


def main():
    """Drives the main operation of the book lending system class"""

    # an instance of the lending system
    obj = BookLendingSystem()

    print("Welcome to the book lending system!")
    while True:
        obj.display_start_menu()

        # get user action choice
        user_choice = obj.obtain_user_display_menu_choice()

        # execute action
        obj.execute_action(user_choice)


if __name__ == "__main__":
    main()
