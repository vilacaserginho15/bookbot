def main(): #function to read files in  a text file
    with open("books/frankenstein.txt") as f: #open text file as variable f
        file_contents = f.read #references variable f to be read, and its result to be stored.
        return file_contents
main()
