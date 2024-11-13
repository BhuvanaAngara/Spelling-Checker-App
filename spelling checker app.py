'''-------------------------------------------SPELLING CHECKER APP---------------------------------------------------------------------
This is a simple Spelling Checker App built using Python's tkinter library for the GUI and TextBlob for the spelling correction feature.

----------------------------Features---------------------------------
User-friendly graphical interface.
Takes a word or sentence as input and displays the corrected spelling.
Provides instant feedback with a single click.

-----------Tech Stack----------
Language: Python
Libraries: tkinter, TextBlob'''


# tkinter and its components are imported to build the GUI.
import tkinter as tk

#TextBlob is imported from the textblob library to use its spelling correction feature.
# pip install textblob
from textblob import TextBlob

#----------Main window setup----------
# root is the main window, with a title, dimensions, and a background color.
root = tk.Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

#-----------Function to check spelling-----------
# check_spelling() is defined to get the input text, correct the spelling using TextBlob, and update the label with the corrected text.
def check_spelling():
    word = enter_text.get()
    if word.strip() == "":
        spell.config(text="Please enter a word", fg="red")
        return
    corrected_word = str(TextBlob(word).correct())
    spell.config(text=f"Correct text: {corrected_word}", fg="#364971")

#----------Heading----------
# Heading Label: Displays the title "Spelling Checker".
heading = tk.Label(root,text = "Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady = (50, 0))

#----------Text entry----------
# Entry Widget: For user input of text that needs spell-checking
enter_text = tk.Entry(root, justify = "center", width = 30, font = ("poppins", 25),bg = "white",border = 2)
enter_text.pack(pady = 10)
enter_text.focus()

#----------Check button----------
# Button: To trigger the check_spelling function.
button = tk.Button(root,text = "Check", font = ("arial", 20, "bold"), fg = "white", bg = "red", command = check_spelling)
button.pack()

#----------Corrected text display----------
# Label: To display the corrected text.
spell = tk.Label(root, font = ("poppins", 20), bg = "#dae6f6", fg = "#364971")
spell.pack(pady = 20)

#----------Run the main loop----------
root.mainloop()
