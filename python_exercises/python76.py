import csv
file = open("Books.csv", "w")
BookRecord = "To Kill a Mockingbird, Harper Lee, 1960\n"
file.write(str(BookRecord))
BookRecord = "A Brief History of Time, Stephen King, 1988\n"
file.write(str(BookRecord))
BookRecord = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(BookRecord))
BookRecord = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(BookRecord))
BookRecord = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(BookRecord))
file.close()

