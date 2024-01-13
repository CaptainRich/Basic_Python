""" A script illustrating a table in 'rich'. """

from rich.console import Console
from rich.table import Table

console = Console()


# Define the table and its title
table = Table( title = "Noble Gases" )

# Define the table columns
table.add_column( "Name", style="cyan", justify="center")
table.add_column( "Symbol", style="magenta", justify="center")
table.add_column( "Atomic Number", style="yellow", justify="right")
table.add_column( "Atomic Mass", style="green", justify="right")
table.add_column( "Main Properties", style="blue", justify="right")

# Define the data for the table, as a list of dictionaries
nobel_gases = [
    {"name": "Helium", "symbol": "He", "atomic_number": 2,
     "atomic_mass": 4.0026, "properties": "Intert Gas"},
    {"name": "Neon", "symbol": "Ne", "atomic_number": 10,
     "atomic_mass": 20.1797, "properties": "Intert Gas:" },
    {"name": "Argon", "symbol": "Ar", "atomic_number": 18,
     "atomic_mass": 39.948, "properties": "Intert Gas:" }, 
]


# Add the data to the table
for nobel_gas in nobel_gases:
    table.add_row( nobel_gas["name"], nobel_gas["symbol"],
                  str(nobel_gas["atomic_number"]), str(nobel_gas["atomic_mass"]),
                  nobel_gas["properties"] )
    
# Display the table
console.print( table )

