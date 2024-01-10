"""Example of 'class' and 'package' implementation for cars."""

import car_package.car_classes as crs

#############################################################################
# Setup the cars

def set_cars():

    # Instantiate several cars.

    # Make, Model, Year, Engine-Type, Color, Drive-Type
    # Mileage, Tire-Miles, Inspection, License, Toll-Tag,
    # (Oil-Miles or Battery Range)

    taycan = crs.Ec_Car( 
        'Porsche', 'Taycan', 2020, 'Electric', 'White', 'all-wheel',
        17100, 0, '9/2024', 'NSS 9353', 'HCTR1-1697792', 246 )

    p911 = crs.Ff_Car( 
        'Porsche', '911', 2008, 'Gasoline', 'Baltic Blue', 'all-wheel',
         9925, 9721, '5/2024', 'HSM 610', 'HCTRA03615043', 6700 )

    tesla = crs.Ec_Car( 
        'Tesla', 'S-P100D', 2017, 'Electric', 'White', 'all-wheel',
         55000, 6700, '4/2024', 'SUVIVR', 'HCTR08587921', 276 )

    yukon = crs.Ff_Car(
        'GMC', 'Yukon XL', 2017, 'Gasoline', 'Dark Gray', 'rear-wheel',
        65753, 58616, '5/2024', 'LYD 0892', 'HCTRA10668298', 65751 )

    sl = crs.Ff_Car(
        'Mercedes', 'SL65 AMG', 2007, 'Gasoline', 'Capri Blue', 'rear-wheel',
        28600, 18000, '2/2024', 'GWL 9350', 'HCTRA03830620', 25035 )

    a5 = crs.Ff_Car(
        'Audi', 'A5', 2012, 'Gasoline', 'White', 'rear-wheel',
        110000, 0, '9/2024', 'CRP 6302', 'HCTRA06418388', 90000 )

    arteon = crs.Ff_Car(
        'Volkswagen', 'Arteon', 2022, 'Gasoline', 'White', 'rear-wheel',
        46000, 450000, '2/2024', 'RTZ 0525', 'HCTR13111680', 40000 )
    
    # Return the 'car objects' in a 'list'
    cars=[taycan, p911, tesla, yukon, sl, a5, arteon]
    
    
    return cars

###########################################################################
# Main
    
# Setup the cars
cars = set_cars()

# Report on the information specified for the cars.

for car in cars:
    info = car.report_car()
    print( "\n", info )


# Update the milage on the Tesla. This data could be moved up above, but 
# this shows the update functions work.

for car in cars:
    if car.make == 'Tesla':
        car.update_tire_miles( 59342 )
        car.update_miles( 59347 )
        info = car.report_car()
        print( "\n", info )
