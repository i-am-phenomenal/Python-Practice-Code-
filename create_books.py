import random 

book_location = "C:/Code/Files/Books/"
book_list_file = "C:/Code/Files/book_names.txt"

genres = ["Action", "Comedy", "Romance", "Sci-fi", "Adventure", "Drama", "Gray Shade"]

types = ["Novella", "StoryBook", "Informational", "Magazine"]

def make_files():
    global genres
    global types 
    global book_location

    for iter in range(2, 52): 
        book_name = "book_" + str(iter)
        author = "author_" +str(iter)
        genre = random.choice(genres)
        type = random.choice(types)
        file_location = book_location + book_name + '.txt'

        file = open(file_location, "a")
        file.write(book_name)
        file.write("\n")
        file.write(author)
        file.write("\n")
        file.write(genre)
        file.write("\n")
        file.write(type)
        file.close()

        book_file = open(book_list_file, "a")
        book_file.write(book_name)
        book_file.write("\n")
        book_file.close()

make_files()