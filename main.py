def count_characters(text):
    string_dict = {}  # opens an empty dictionary 
    for char in text:  # loops through each character in text
        lowered_char = char.lower() 
        if lowered_char in string_dict: #looks at text through the lens of key values
            string_dict[lowered_char] += 1 #adds the number of characters as a value 
        else:
            string_dict[lowered_char] = 1
    return string_dict
    
def count_words(text): 
    splitting = text.split()  # split so it creates a list
    counting = len(splitting)  # when you have a list, len counts each word in that list
    return(counting)  # return the total 

def main():  # function to read files in a text file
    with open("books/frankenstein.txt") as f:  # open text file as variable f
        file_contents = f.read()  # references variable f to be read, and its result to be stored.
        print("--- Begin report of books/frankenstein.txt ---")
        word_count = count_words(file_contents)
        print(f"{word_count} words found in the document")
        print() 
        new_characters = count_characters(file_contents)
        string_list = []
        for key,value in new_characters.items():
            if key.isalpha(): 
                string_list.append({"char": key, "count": value}) 
        def sort_by_temp(dict):
            return dict["count"]
        string_list.sort(key=sort_by_temp, reverse=True)
        for char_data in string_list:
            print(f"The '{char_data['char']}' character was found {char_data['count']} times")
        print("--- End report ---") 

if __name__ == "__main__":
    main()

