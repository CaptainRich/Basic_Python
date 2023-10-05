# An example of reading a PDF file

from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

############################################################################
# Main
"""A routine to read a specific PDF file (Pride_and_Prejudice.pdf)."""

# Build the path to the current working directory and then append the PDF name.
current_path = Path.cwd()
input_path   = current_path / "Pride_and_Prejudice.pdf"
output_path  = current_path / "New_Parital_Pride_and_Predjudice.pdf"

# In setting up the PdfFileReader instance, convert the path to a string - required
# because the PdfReader can't handle a 'path' object.
pdf = PdfReader( str( input_path ) )

# Report the number of pages in this PDF.
print( "\nFor ", input_path, ":" )
num_pages = len(pdf.pages)
print( "    Number of pages: ", num_pages )
print( "    Document information: ", pdf.metadata )
author = pdf.metadata.author 
print( "    Author: ", author )
title = pdf.metadata.title

# Access the fist page and display it.
first_page = pdf.pages[0]
print( "\nThe first page of this PDF is: " )
print( first_page.extract_text() )

# Output the first 5 pages of the PDF to a text file.  The file is automatically
# closed when the scope of 'with' is exited.
out_text = Path.cwd() / "Pride_and_Prejudice.txt"
with out_text.open( mode='w' ) as out_file:
    out_file.write( f"{title}\nby {author} has {num_pages} pages.\n" )
    out_file.write( "The first 5 pages of the document are printed below.\n" )

    for i in range( 0, 5 ):
        text = pdf.pages[i].extract_text()
        out_file.write( text )


# Output the first 5 pages to a new PDF file.
pdfw = PdfWriter()

for i in range( 0, 5 ):
    page = pdf.pages[i]               # Get the page
    pdfw.add_page( page )             # Add the page to the PDF writer instance

# Note that the output file object is passed as an argument to the PdfWrite object.
with output_path.open( mode="wb" ) as output_pdf:
    pdfw.write( output_pdf )




