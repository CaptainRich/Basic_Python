# A routine to rotate certain pages in  a PDF.
"""
This routine rotates pages in a PDF file based on the /Rotate key of the
page.  If the key value is -90, the page has been rotated 90 deg counterclockwise.
If this is the case, rotate the page back so that all pages in the document can
be properly read/displayed.  This routine assumes the PDF document is: 
'ugly_rotated.pdf'.
"""

from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

#############################################################################################
# 'PdfFileRotater' is the class that does all the work
class PdfFileRotater:

    ########################################################################################
    # Initializer / Constructor
    def __init__( self, input_pdf_path, output_pdf_path ):
        """This the 'class' constructor for the PDF file rotater."""
        self.path_in   = input_pdf_path   
        self.writer1   = PdfWriter()
        self.reader1   = ""
        self.path_out  = output_pdf_path  

    #########################################################################################
    # Instance methods for Class 'PdfFileRotater'
    def rotate( self ):
        """This method rotates pages in the PDF file based on the '/Rotate' key."""

        self.reader1 = PdfReader( str( self.path_in ) )

        for i in range( len(self.reader1.pages ) ):
            page = self.reader1.pages[i]
            rotate_value = page["/Rotate"]

            # Based on the rotate value, rotate the page in the opposite direction
            # if necessary.  If there is no rotate value, or the rotate value is
            # zero, no (un)rotation is necessary.

            if rotate_value != 0:
                page.rotate( -rotate_value )     # Rotate in the opposite direction

            self.writer1.add_page( page ) 

        return
    
    ##########################################################################################
    def write( self ):
        """This class method creates the two output (PDF) files."""

        with self.path_out.open( mode="wb" ) as out_file:
            self.writer1.write( out_file )

        return

    
#################################################################################################
# Main
"""This is the main driver for the PDF rotater."""

# Prompt for the name of the PDF file to (un)rotate.
pdf_name    = input( "\nWhat is the name of the PDF file to fix (un-rotate)? " )

# Build the path to the PDF file to be split and the output file template name.
cwd         = Path.cwd()
input_file  = cwd / pdf_name           # Setup the pathname to the input file
print( f"\nThe PDF file to be fixed is {input_file}." )

pdf_template = pdf_name[0:-4] +  '-fixed.pdf'        # Strip off the file name suffix
output_file  = cwd / pdf_template                    # Setup the pathname to the output file

print( "The input PDF file to be split is: ", input_file )
print( "The output PDF file is: ", output_file )

# Fix the file
pdf_rotate = PdfFileRotater( input_file, output_file )

pdf_rotate.rotate()            # Fix the pages and send to the "writer".
pdf_rotate.write()             # Perform the write operation to the PDF output file.

