from data.db import init_db


def main():
    init_db()
    print("WELCOME")
    while True:
        print("\nOptions: [1] Add [2] View [3] Delete [0] Exit")
        choice = input("Choice")
        if choice == '1':
            ...
        elif choice == '2':
            ...
        elif choice == '3':
            pass

        elif choice == '0':
            break
        else:
            print("invalid")

if __name__ == "__main__":
    main()