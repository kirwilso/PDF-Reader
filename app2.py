#This is my project
#importing the items I need for the project 
import tkinter as tk 
from tkinter import ttk
from PyPDF2 import PdfFileReader
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

def open_file():
    browse_text.set("loading...") #this will set the text to "loading" when the user selects a PDF 

    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("Pdf file", "*pdf")])
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

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3) 

#logo 
logo = Image.open('Assets Folder/logo.png') # fixed file location
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


#instructions 
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font= "Raleway")
instructions.grid(columnspan=3, column=0, row=1)


#Text box for the user 
# CH you should not do that inside your function b/c that will create a new widget every time
# Instead create it once and just clear and re-fill it
text_box = tk.Text(root, height=10, width=50, padx=15, pady=15) #creating text box for PDF file to show up for user 
text_box.grid(column=1, row=3)


#browse button 
browse_text = tk.StringVar()
browse_btn = tk.Button(root,  textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="blue", highlightbackground='#3E4149', fg="black", height=3, width=15)
#ERROR having trouble on line above, getting the button to turn blue. bg="blue" I think that this is a mac problem maybe? CH:  could be. Looks dark blue on my Win 10 PC
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)


#Making the canvas larger so it does not look weird 
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3,)




root.mainloop() 



 
