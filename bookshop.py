bookshop = {
    "Harry Potter and the Philosopher's Stone":10,
    "Department 19":8,
    "Chain of Gold":12,
    "Chain of Iron":6,
    "Maths":3,
    "English":4,
    "Geography":3,
    "Music":4,
    "Physics":5,
    "Chemistry":6,
    "Biology":7,
    "DT":11,

}
print(bookshop)

book = input("Which book do you need? ")

if book in bookshop:
    print("Here is the book and we have the details")
    book_details = bookshop[book]
    print("The cost of the book is", book_details)

else:
    print("The book does not exist")