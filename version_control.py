# Rafael Hinchey

def encode(password):
    new_password = ""
    data = password[:]
    for i in data:
        j = int(i)
        k = (j + 3) % 10
        x = str(k)
        new_password += x
    return new_password


def main():
    encrypt = True
    while encrypt is True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!")

        if option == 2:
            pass
            # code below is option 2 but, we're supposed to create a decode function?
            # print(f"Your encoded password is {encode(password)}, and the original password is {password}.")

        if option == 3:
            encrypt = False


if __name__ == '__main__':
    main()