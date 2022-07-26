#This is my project
#importing the items I need for the project 
import tkinter as tk 
from tkinter import ttk
from PyPDF2 import PdfFileReader
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

def open_file():
    browse_text.set("loading...") #this will set the text to "loading" when the user selects a PDF 

    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PdfFileReader(file) # fixed usage of Class PdfFileReader that you imported from PyPDF2

        # CH maybe read more than just page 0?
        num_pages = len(read_pdf.pages)
        print("pdf contains", num_pages, "pages")

        page = read_pdf.getPage(0)
        page_content = page.extractText()
        
        # delete any old text
        text_box.delete('1.0', tk.END)
        # You could make this dependent on a append new text toggle. If that's on,
        # the new text will be inserted at the end of the existing text, if not,
        # you delete everything first


        # Inserting text
        text_box.insert(tk.END, page_content)
        #text_box.tag_configure("center", justify="center") #centering text in the text box # CH why centered?
        #text_box.tag_add("center", 1.0, "end")

        browse_text.set("Browse") #this will set the text back to "Browse" after the user has browsed for a PDF 
        
root = tk.Tk()

# grid setup
# logo, instructions and button are in the 2. of 3 columns
# textbox starts at the 1. column (0) and spans 3 columns, its width (50) essentially defines the overall width
# All widgets have a padx and pady for a "fluffier" layout  


#logo 
logo = Image.open('Assets Folder/logo.png') # fixed file location
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0, columnspan=1, padx=30, pady=30, sticky=tk.EW)


#instructions 
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font= "Raleway")
instructions.grid(column=1, row=1, columnspan=1, padx=30, pady=10, sticky=tk.EW)


#browse button 
browse_text = tk.StringVar()
browse_btn = tk.Button(root,  textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="blue", highlightbackground='#3E4149', fg="black", height=3, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2, columnspan=1, padx=30, pady=10, sticky=tk.EW)

#Text box for the user, but now inside a frame so we can stick a scroll bar opn the side 
textframe = tk.Frame(root)
textframe.grid(column=0, row=3, columnspan=3,  padx=30, pady=10, sticky=tk.EW)      

# create and pack the text area
text_box=tk.Text(textframe, padx=10, pady=10, height=30, width=50, wrap=tk.WORD) # pad here is an internal padding
text_box.pack(side=tk.LEFT, fill=tk.BOTH)

# yview callback gets called when the scroll bar or its arrows are moved
# that will reposition the text in text_box
text_scroll = tk.Scrollbar(textframe, command=text_box.yview)
text_scroll.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop() 



 
