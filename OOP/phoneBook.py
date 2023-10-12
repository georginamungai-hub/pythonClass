# Phonebook App
# Write a Python program to implement a phonebook app that allows users to add, delete, and search for contacts.
# The app should use a dictionary to store contact information, with the contact name as the key and the phone number as the value.
# The app should have the following features:
# Add a contact: Prompt the user to enter a contact name and phone number, then add the contact to the dictionary.
# If the contact already exists, display an error message and do not add the contact.
# Delete a contact: Prompt the user to enter a contact name, then delete the contact from the dictionary if it exists.
# If the contact does not exist, display an error message.
# Search for a contact: Prompt the user to enter a contact name, then display the contact's phone number if it exists.
# If the contact does not exist, display an error message.
# Print all contacts: Display all contacts and their phone numbers in the dictionary.
class Phonebook:
    def __init__(self,name,phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def addContact(self):
        contactInfo = {
            "Name":{self.name},
            "Phone Number": {self.phoneNumber}
        }
        
    def deleteContact():
        pass

    def searchContact():
        pass

    def printContacts():
        pass