#import library
import hashlib


def create_rainbow(word_list, output_file):
    # try to open the file
    try:
        wordlist_input = open(word_list)
    # except error when the file cannot be opened
    except:
        print("File cannot be found or opened:", word_list)
        # quit the program
        exit()
    # open the rainbow text file
    rainbow_file = open(output_file, "w")
    for line in wordlist_input:
        # remove all trailing characters at the end of the string
        line = line.strip('\n')
        # encode the string
        line = line.encode("ISO-8859-1")
        # hash the string
        line_hash = hashlib.md5(line)
        # return the hash value as a string
        hash_value = line_hash.hexdigest()
        # write that hash value to the rainbow text file
        rainbow_file.write(hash_value + "\n")
    # close opened files
    wordlist_input.close()
    rainbow_file.close()


# prompt the user for a file name
my_file = input("Enter file name to open: ")

# execute function
create_rainbow(my_file)
