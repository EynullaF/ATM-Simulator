a = {
    "12345" : {
        "pin" : 3344,
        "name" : "Brian",
        "balance" : 800.0
    },
    "67890" : {
        "pin" : 1199,
        "name" : "Sally",
        "balance" : 500.0
    }
}
def check():
    print(f"\033[93mYour balance is {a[b]["balance"]}\033[0m")
    return False
def withdraw():
    print(f"\033[93mYour balance is {a[b]["balance"]}\033[0m")
    d=int(input("\033[95mEnter the amount you wish to withdraw: \033[0m"))
    if d<=0:
        print("\033[91mInvalid amount!\033[0m")
        g=input("Do you want to go back? (y/n): ").lower()
        if g == "n":
            withdraw()
    else:
        if d > a[b]["balance"]:
            print("\033[91mInsufficient balance!\033[0m")
            g=input("Do you want to go back? (y/n): ").lower()
            if g == "n":
                withdraw()
        else:
            a[b]["balance"] = a[b]["balance"] - d
            print(f"\033[93mYour balance is {a[b]["balance"]}\033[0m")
    return False
def deposit():
    print(f"\033[93mYour balance is {a[b]["balance"]}\033[0m")
    f=int(input("\033[95mEnter the amount you wish to deposit: \033[0m"))
    if f<=0:
        print("\033[91mInvalid amount!\033[0m")
    else:
        a[b]["balance"] = a[b]["balance"] + f
        print(f"\033[93mYour balance is {a[b]["balance"]}\033[0m")
        return False
def exit():
    print("\033[92mPlease take your card. Thank you for banking with us!\033[0m")
    return False
import sys
attempts = 3
while True:
    b=input("\033[94mEnter the card number: \033[0m")
    if b in a:
        while attempts > 0:
            c=int(input("\033[92mEnter the PIN code: \033[0m"))
            if c == a[b]["pin"]:
                print(f"Hello!, Dear {a[b]["name"]}")
                while True:
                    print("-----------------------")
                    print("---TRANSACTIONS---")
                    print("1. Check Balance")
                    print("2. Withdraw Cash")
                    print("3. Deposit Cash")
                    print("4. Exit")
                    print("-----------------------")
                    choice = input("\033[94mPlease select a transaction (1-4): \033[0m")
                    if choice == "1":
                        check()
                    elif choice == "2":
                        withdraw()
                    elif choice == "3":
                        deposit()
                    elif choice == "4":
                        exit()
                        sys.exit()
                    else:
                        print("\033[91mInvalid choice! Please select an option between 1 and 4.\033[0m")
            else:
                attempts -= 1
                print(f"\033[91mYou have {attempts} attempts left\033[0m")
                if attempts == 0:
                    print("-----------------------")
                    break
    else:
        print("\033[91mInvalid card number! Please check and try again.\033[0m")