# An example of reading a PDF file

from PyPDF2 import PdfReader
from pathlib import Path

############################################################################
# Main
"""A routine to read a specific PDF file."""

# Build the path to the current working directory and then append the PDF name.
current_path = Path.cwd() / "Pride_and_Prejudice.pdf"

# In setting up the PdfFileReader instance, convert the path to a string - required
# because the PdfReader can't handle a 'path' object.
pdf = PdfReader( str( current_path ) )

# Report the number of pages in this PDF.
print( "\nFor ", current_path, ":" )
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

# Output the first 5 pages of the PDF to a text file.
out_path = Path.cwd() / "Pride_and_Prejudice.txt"
with out_path.open( mode='w' ) as out_file:
    out_file.write( f"{title}\nby {author} has {num_pages} pages.\n\n" )

    i = 0
    for page in pdf.pages:
        text = page.extract_text()
        out_file.write( text )
        i = i + 1
        if( i > 5 ):
            break
        



