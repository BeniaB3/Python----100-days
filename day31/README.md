 # Flashcard App

 An application for learning the French language using flashcards.

 ### Requirements

 - Python 3.6 or newer
 - tkinter library (included by default in Python)

 ### Installation

 1. Clone the repository
 2. Run main.py

 ### How to use

 After launching the application, a flashcard with a French word will appear on the screen.
 After 3 seconds, the flashcard will flip, showing the translation in English.
 If you knew the word, click the button with the green checkmark.
 If you didn't know the word, click the button with the red cross.
 The app will keep track of the words you know and will save the remaining words to learn in a CSV file.
 When you've learned all the words, a message box will appear, congratulating you on completing the learning process.

 ### Features

 - Randomly displays French words from a CSV file
 - Automatically flips the flashcard to reveal the English translation after 3 seconds
 - Tracks your progress by saving the words you know
 - Saves the remaining words to learn in a separate CSV file
 - Displays a message box when you have learned all the words

 ### Customization

 You can easily customize the application to learn other languages or subjects by following these steps:

 1. Create a new CSV file containing the data you want to learn, with the format:
    Term,Translation
    Example: maison,house
 2. Replace the French words CSV file with your custom CSV file.
 3. Update the `name` variable in the script to reflect the name of the subject or language you're learning.


