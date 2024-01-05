"""Example of 'class' and 'package' implementation for cars."""

import class_package.car_classes as crs

# Instantiate several cars.

taycan = crs.Car( 
    'Porsche', 'Taycan', 2020, 'Electric', 'White', 'all-wheel',
    16700, 0, 0, '9/2024' )

p911 = crs.Car( 
    'Porsche', '911', 2008, 'Gasoline', 'Baltic Blue', 'all-wheel',
     9925, 0, 6700, '9/2024' )

tesla = crs.Car( 
    'Tesla', 'S-P100D', 2017, 'Electric', 'White', 'all-wheel',
     9925, 0, 6700, '9/2024' )

yukon = crs.Car(
    'GMC', 'Yukon XL', 2017, 'Gasoline', 'Dark Gray', 'rear-wheel',
    70000, 65000, 0, '9/2024' )

sl = crs.Car(
    'Mercedes', 'SL-65 AMG', 2007, 'Gasoline', 'Capri Blue', 'rear-wheel',
    28600, 27000, 0, '9/2024' )


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