"""Example of 'class' and 'package' implementation for cars."""

import car_package.car_classes as crs

#############################################################################
# Setup the cars

def set_cars():

    # Instantiate several cars.

    # Make, Model, Year, Engine-Type, Color, Drive-Type,
    # Mileage, Tire-Miles, Next Inspection, License, Toll-Tag,
    # (Oil-Miles or Battery Range), purchase date, sell date
    
	# Ec - Electric Car        Ff - Fossil fuel car

    taycan = crs.Ec_Car( 
        'Porsche', 'Taycan', 2020, 'Electric', 'White', 'all-wheel',
        20500, 18127, '9/2024', 'NSS 9353', 'HCTR1-1697792', 250,
        'Sept 2020', 'active' )

    p911 = crs.Ff_Car( 
        'Porsche', '911', 2008, 'Gasoline', 'Baltic Blue', 'all-wheel',
         10220, 9721, '5/2025', 'HSM 610', 'HCTRA03615043', 10210,
          'Apr 2008', 'active' )

    tesla = crs.Ec_Car( 
        'Tesla', 'S-Plaid', 2024, 'Electric', 'White', 'all-wheel',
          233, 233, '8/2025', 'SUVIVR', 'MTAH00559616', 256, 
          'Aug 2024', 'active' )

    yukon = crs.Ff_Car(
        'GMC', 'Yukon XL', 2017, 'Gasoline', 'Dark Gray', 'rear-wheel',
        73325, 66907, '5/2025', 'LYD 0892', 'HCTRA10668298', 73325,
         'Apr 2019', 'active' )

    sl = crs.Ff_Car(
        'Mercedes', 'SL65 AMG', 2007, 'Gasoline', 'Capri Blue', 'rear-wheel',
        29120, 29110, '2/2025', 'GWL 9350', 'HCTRA03830620', 25035,
         'Mar 2008', 'active' )

    a5 = crs.Ff_Car(
        'Audi', 'A5', 2012, 'Gasoline', 'White', 'rear-wheel',
        135010, 0, '9/2024', 'CRP 6302', 'HCTRA06418388', 90000,
         'Jun 2014', 'May 2024' )

    arteon = crs.Ff_Car(
        'Volkswagen', 'Arteon', 2022, 'Gasoline', 'White', 'rear-wheel',
        46000, 450000, '2/2024', 'RTZ 0525', 'HCTR13111680', 40000,
         'Jul 2022', 'active' )
    
    # Return the 'car objects' in a 'list'
    cars=[taycan, p911, tesla, yukon, sl, a5, arteon]
    
    
    return cars

###########################################################################
# Display all of the information for all of the cars.
def display_all_cars( cars ):
    """ Display all of the information for the cars in the 'cars' list. """

    for car in cars:
        info = car.report_car()
        print( "\n", info ) 


###########################################################################
# Main
    
# Setup the cars
cars = set_cars()

"""
# Report on the information specified for the cars.

for car in cars:
    info = car.report_car()
    print( "\n", info ) """

"""
# Update the milage on the Tesla. This data could be moved up above, but 
# this shows the update functions work.

for car in cars:
    if car.make == 'Tesla':
        car.update_tire_miles( 59342 )
        car.update_miles( 59347 )
        info = car.report_car()
        print( "\n", info )  """

########
# Display a list of the current cars and ask what display action should be taken.
num_cars = len(cars)
print( f"\n There are {num_cars} cars defined (1/9/2024)." )
ans = input( " Display information on (a)ll or just (o)ne car?  ").upper()

if( ans != 'A' and ans != 'O' ):    # Verify the response
    print( " \n Invalid option specified.\n" )
    exit()


if( ans == 'A' ):
    display_all_cars( cars )
    exit()

# Prompt for which car's information should be displayed.
print( f"\n Select which car's information should be displayed:\n")

for index, car in enumerate(cars):
    print( f"({index}) {car.make.title()} {car.model}")

ans   = input( "\n Which car should be displayed? " )
index = int( ans )

if( index > num_cars-1 ):    # Verify the response
    print( " \n Invalid index specified.\n" )
    exit() 

info  = cars[index].report_car()  # Report on the selected car
print( "\n", info )

