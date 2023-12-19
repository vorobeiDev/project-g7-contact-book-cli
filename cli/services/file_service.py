import os
import pickle


def read_contacts_from_file(filename):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return None


def write_contacts_to_file(filename, book):
    with open(filename, 'wb') as file:
        pickle.dump(book, file)
