# This routine illustrates creating and Querying a database.

########################################################################################33
# Main

import sqlite3
from pathlib import Path

# Define the data structure of the database, as well as the seed data.  Note that the 
# table definition and the data insertion are defined as 'strings'.

create_table = """
CREATE TABLE Roster(
    Name TEXT,
    Species TEXT,
    Age INT );
"""

seed_values = (
    ( "Benjamin Sisko", "Human", 40 ),
    ( "Jadzia Dax", "Trill", 300 ),
    ( "Kira Nerys", "Bajoran", 29 ),
)


# Get the current working directory - where the database will be utilized.
cwd = Path.cwd()

db_file = cwd / "test_database.db"

# Open the database connection and create the database.  Note that 'connection.close()' and
# 'connection.commit()' are not needed when using 'with'. Below the data insertion uses
# 'parameterized values' for safety/security.

with sqlite3.connect( db_file ) as connection:
    cursor = connection.cursor()
    cursor .execute( "DROP TABLE IF EXISTS Roster" )     # Necessary for reruns.
    cursor.execute( create_table )
    cursor.executemany( "INSERT INTO Roster VALUES(?, ?, ?);", seed_values )

# The database is created and populated.  Dump out all of the rows.

with sqlite3.connect( db_file ) as connection:
    cursor = connection.cursor()

    cursor.execute(
        "SELECT Name, Species, Age FROM Roster;"
    )

    for row in cursor.fetchall():
        print( row )
