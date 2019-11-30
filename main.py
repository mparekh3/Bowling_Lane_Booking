from bowlinglane import Bowlinglane, Customer

def main():
    book = Bowlinglane(5)

    while True:
        print("""
        =======Bowling Lane Booking=====
        1. Display available lanes
        2. Select lane
        3. Game Over
        4. Exit
        """)

        choice = input("How can I help you?: ")

        try:
            choice = int(choice)
        except ValueError:
            print("That's not an option!")
            continue
        if choice == 1:
            book.displaylane()
        elif choice == 2:
            book.Booklane(book.requestlane())

        elif choice == 3:
            bill = book.gameover()
        elif choice == 4:
            break
        else:
            print("Invalid input. Please select value form menu")
    print("Thank you for using Bowling Lane Book system.")
    print("\U0001f600")

if __name__ == "__main__":
    main()

