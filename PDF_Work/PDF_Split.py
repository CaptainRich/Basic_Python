# A routine to split a PDF into two new PDFs at a specified page.
"""
This routine splits a PDF file into two documents.  The routine prompts for 
the name of the PDF, and where (what page) the split should occur.  The routine
then creates two new PDFs, where the file names are appended with _1 and _2.
"""

from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

# 'PdfFileSplitter' is the class that does all the work
class PdfFileSplitter:

    # Initializer / Constructor
    def __init__( self, input_pdf_path ):
        """This the 'class' constructor for the PDF file splitter."""
        self.path_in   = input_pdf_path   
        self.writer1   = PdfWriter()
        self.writer2   = PdfWriter() 
        self.path_out  = "" 
        self.path_out1 = ""   
        self.path_out2 = ""

    # Instance methods for Class 'PdfFileSplitter'
    def split( self, split_point ):
        """This method divides the input PDF into two pieces, based on the split_point."""

        reader = PdfReader( str( self.path_in ) )

        for page in reader.pages[0:split_point]:
            self.writer1.add_page( page )

        for page in reader.pages[split_point:]:
            self.writer2.add_page( page )    

        return
    
    def write( self, output_pdf_path ):
        """This class method creates the two output (PDF) files."""
        self.path_out = str( output_pdf_path )

        output_file    = self.path_out  + "_1.pdf"    # Append the new file ending
        output_path    = Path( output_file )          # Convert to a 'path' object
        self.path_out1 = output_path

        with output_path.open( mode="wb" ) as out_file:
            self.writer1.write( out_file )

        output_file    = self.path_out + "_2.pdf"
        output_path    = Path( output_file )
        self.path_out2 = output_path
        
        with output_path.open( mode="wb" ) as out_file:
            self.writer2.write( out_file )   

        return
    
    def report( self ):
        """This class method returns the pathname of the two new PDFs created."""

        return self.path_out1, self.path_out2
    
#################################################################################################
# Main
"""This is the main driver for the PDF splitter."""

# Prompt for the name of the PDF file to split and where (what page) to split on.
pdf_name    = input( "\nWhat is the name of the PDF file to split? " )
split_point = int( input( "What is the page number where the file is to be split? " ) )

print( f"\nThe PDF file {pdf_name} is to be split at page {split_point}" )

# Build the path to the PDF file to be split and the output file template name.
cwd         = Path.cwd()
input_file  = cwd / pdf_name           # Setup the pathname to the input file

pdf_template = pdf_name[0:-4]          # Strip off the file name suffix
output_file  = cwd / pdf_template      # Setup the pathname to the output file

print( "The input PDF file to be split is: ", input_file )
print( "The output PDF file primary name is: ", output_file )

# Split the file
pdf_split = PdfFileSplitter( input_file )
pdf_split.split( split_point )
pdf_split.write( output_file )


# Display the (path) names of the two PDFs just created.
path1, path2 = pdf_split.report()

print( "\nThe two new PDFs created are: " )
print( path1 )
print( path2 )

