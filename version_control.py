# Rafael Hinchey

def encode(password):
    new_password = "" 		# return result will be a str variable
    data = password[:] 		# creates an array variable
    for i in data:		    # for loop for each character from the str
        j = int(i)		    # turns str into int
        k = (j + 3) % 10    # encode formula
        x = str(k)		    # turns new int back into str variable
        new_password += x   # combining characters into one string

    return new_password

# Alexander Rufrano

def decode(password):
    temp_password = ""                      # Create empty string to return
    for i in password:                      # Create for loop to iterate through the encoded password string
        temp_password += str(int(i) - 3)    # Reduce each string number by 3
    return temp_password                    # Return the decoded password string

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
            # Alexander Rufrano
            encoded_password = encode(password) # create a variable that comprises the encoded password string
            decoded_password = decode(encoded_password) # create a varaible that decodes the encoded password
            print(f"Your encoded password is {encoded_password}, and the original password is {decoded_password}.")  # Create print function to display result.

        if option == 3:
            encrypt = False


if __name__ == '__main__':
    main()
