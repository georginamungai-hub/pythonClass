import json


# book = {
#         'Title': {Title},
#         'Author': {Author},
#         'Genre': {Genre},
#         'SubGenre': {SubGenre},
#         'Height': {Height},
#         'Publisher': {Publisher}
# }

def bookSearch(file_name):
    with open(file_name, "r") as file:
        for books in file:
            print(books)
bookSearch("books.csv")            

# def bookLib(file_name):
#     with open(file_name,'w') as library:
#         library.write(json.dumps)