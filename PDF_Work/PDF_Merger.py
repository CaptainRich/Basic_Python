# A routine to merge a number of PDFs into a single PDF.
"""
This routine merges PDFs into a single PDF using the '.append' method. The
assumption with this routine is that three expense files will be merged, where
the file names 'expense report x.pdf' - where x=1, 2, 3.  The new output PDF
is named 'expense_reports.pdf'.  All files are assumed to be in the 
'current working directory'.
"""

from PyPDF2 import PdfWriter
from pathlib import Path


############################################################################################
# Main driver routine

# Build the path to the current working directory.
cwd = Path.cwd()

# Assuming the expense reports are in 'cwd', build a list of these files (using a wildcard),
# then sort the list, and finally report the list contents.

expense_report_list = list( cwd.glob( "Exp*.pdf" ) )
expense_report_list.sort()                            # Sort the list 'in-place'
print( "\nThe expense report files are:" )
for path in expense_report_list:
    print( path.name )

# Add (append) each of these PDFs into the 'merger' instance.
pdf_merger = PdfWriter()

for path in expense_report_list:
    pdf_merger.append( str(path) )    # Note the conversion to a string

# Finally write the contents of the 'merger' to the output PDF.
out_file = cwd / "expense_reports.pdf"
with out_file.open( mode='wb') as output_PDF:
    pdf_merger.write( output_PDF )

print( "The combined PDF is: ", out_file )


