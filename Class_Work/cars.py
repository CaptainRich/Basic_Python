"""Example of 'class' and 'package' implementation for cars."""

import class_package.car_classes as crs

# Instantiate several cars.

taycan = crs.Car( 
    'Porsche', 'Taycan', 2020, 'Electric', 'White', 'all-wheel',
    17100, 0, 0, '9/2024', 'NSS 9353', 'HCTR1-1697792' )

p911 = crs.Car( 
    'Porsche', '911', 2008, 'Gasoline', 'Baltic Blue', 'all-wheel',
     9925, 0, 6700, '5/2024', 'HSM 610', 'HCTRA03615043' )

tesla = crs.Car( 
    'Tesla', 'S-P100D', 2017, 'Electric', 'White', 'all-wheel',
     55000, 0, 6700, '4/2024', 'SUVIVR', 'HCTR08587921' )

yukon = crs.Car(
    'GMC', 'Yukon XL', 2017, 'Gasoline', 'Dark Gray', 'rear-wheel',
    70000, 65000, 0, '5/2024', 'LYD 0892', 'HCTRA10668298' )

sl = crs.Car(
    'Mercedes', 'SL65 AMG', 2007, 'Gasoline', 'Capri Blue', 'rear-wheel',
    28600, 27000, 0, '2/2024', 'GWL 9350', 'HCTRA03830620' )

a5 = crs.Car(
    'Audi', 'A5', 2012, 'Gasoline', 'White', 'rear-wheel',
    110000, 90000, 0, '2/2024', 'CRP 6302', 'HCTRA06418388' )

arteon = crs.Car(
    'Volkswagen', 'Arteon', 2022, 'Gasoline', 'White', 'rear-wheel',
    46000, 40000, 450000, '2/2024', 'RTZ 0525', 'HCTR13111680' )


# REport on the information specified above.

taycan_info = taycan.report_car()
print( "\n", taycan_info )

p911_info = p911.report_car()
print( "\n", p911_info )

tesla_info = tesla.report_car()
print( "\n", tesla_info )

yukon_info = yukon.report_car()
print( "\n", yukon_info )

sl_info = sl.report_car()
print( "\n", sl_info )

a5_info = a5.report_car()
print( "\n", a5_info )

arteon_info = arteon.report_car()
print( "\n", arteon_info )


# Update the milage on the Tesla
tesla.update_tire_miles( 59342 )
tesla.update_miles( 59347 )
tesla_info = tesla.report_car()
print( "\n", tesla_info )