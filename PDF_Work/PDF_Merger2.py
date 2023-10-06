# A routine to merge a number of PDFs into a single PDF.
"""
This routine merges PDFs into a single PDF using the '.merge' method. The
assumption with this routine is that a 'table of contents' PDF needs to be inserted
into a 'quarterly report' PDF  All files are assumed to be in the 
'current working directory': report.pdf and toc.pdf.
"""

from PyPDF2 import PdfMerger
from pathlib import Path


def setup_files( cwd ):
    """This function completes the file paths and checks for existence."""

    # Construct the assumed file (path) names, and verify both exist.
    report_file = cwd / 'report.pdf'
    toc_file    = cwd / 'toc.pdf'

    if( not report_file.exists() ):
        print( 'Sorry, the report file does not exist in this directory.' )
        exit()

    if( not toc_file.exists() ):
        print( 'Sorry, the TOC file does not exist in this directory.' )
        exit()

    return ( report_file, toc_file )

############################################################################################
# Main driver routine


# Build the path to the current working directory.
cwd = Path.cwd()
report_file, toc_file = setup_files( cwd )

# Setup the "PDF Merger" object and load it with the primary report file (PDF).
pdf_merger = PdfMerger()
pdf_merger.append( str( report_file ) )

# Now insert the TOC PDF. Pages are indexed starting with 0.  The TOC should be 
# BEFORE page (index) 1 of the REPORT PDF.
pdf_merger.merge( position=1, fileobj=str(toc_file), pages=(0,1) )

# Finally write out the 'merged' PDF
final_report = cwd / 'Final_Quarterly_Report.pdf'
with final_report.open( mode='wb' ) as output_file:
    pdf_merger.write( output_file )









