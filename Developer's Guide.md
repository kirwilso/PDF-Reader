# Developer's Guide for PDF File Reader 
Add this to the doc folder in Github and hand in on Canvas

###Overview 

This is an app to extract text from a PDF using a GUI built with Visual Studio, Tkinter, PYPDF 2 and Pillow. The app will allow a user to open and select a PDF off their computer, and then it will extract the text. The app will feature a GUI that allows a user to browse for PDF’s in the industry standard way.  


###Condensed Version of the Final Planning Specs

When a user clicks the browse button on the GUI, on release of click the system triggers a browse modal to pop up.  

When the user selects a PDF the app sends information that it is a PDF and proceeds to run the code that extracts the text. 

When the user uploads a PDF and sees the text displayed in the GUI, there is a scroll bar on the GUI

The app limits the user to a PDF file only and all other file types are disabled.

###Install/deployment/admin issues:

This app is very straight forward and simple. There should  ot be any install, deployment or admin issues for the user. 


###(End) User interaction and flow through your code ("Happy Path")

WHEN I run the app on my source code editor

THEN I see a GUI that says “PDF Extract Text” 

AND I see a button that says “Browse”  

WHEN I click the “Browse” button  

THEN I am prompted to search for PDFs and anything that is NOT a PDF will be unselectable 

WHEN I select a PDF  

THEN a plain text box appears with the extracted text  
 
###Flow of Code

Code Outline:

* Importing items from modules 
* Function that:
    * Sets loading on click
    * Opens file on click
    * Deletes any old text
    * Reads more than just one page of PDF
    * For loop that extracts the text from the PDF
    * Inserting text box for GUI
    * Sets text back to "browse" after selection
* Creation of TK Canvas
* Logo for GUI
* Instructions on GUI
* Creation of browse button 
* Text box that sets scroll bar 
* Creating and packing text into the text area 
* Scroll bar repositioning 
* Final adjustments to canvas for style 

###Known Issues: 
Minor: Mac os has issues with showing GUI design correctly

###Future work:

Possible future additons are:

* Modifying the app to be able to edit PDFs.
* Modifying the app to be able to save/rename PDFs.
* Modifying the app to look better. 
* Modifying the app to allow the user to select which pages of a PDF they want to view. 
