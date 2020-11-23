#import library
import hashlib


def create_rainbow(file_parm):
    # try to open the file
    try:
        file_input = open(file_parm)
    # except error when the file cannot be opened
    except:
        print("File cannot be found or opened:", file_parm)
        # quit the program
        exit()
    # open the rainbow text file
    rainbow_file = open("english_rainbow.txt", "w")
    # enumerate lines in file_input to get index numbers and line values
    for idx, line in enumerate(file_input):
        # remove all trailing characters at the end of the string
        line = line.rstrip()
        # encode the string
        line = line.encode("ISO-8859-1")
        # hash the string
        line_hash = hashlib.md5(line)
        # return the hash value as a string
        hash_value = line_hash.hexdigest()
        # write that hash value to the rainbow text file
        rainbow_file.write(hash_value + "\n")
    # close opened files
    file_input.close()
    rainbow_file.close()


# prompt the user for a file name
my_file = input("Enter file name to open: ")

# execute function
create_rainbow(my_file)
