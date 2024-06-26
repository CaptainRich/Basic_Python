""" Class structure for the 'car' objects."""

class Car:

    def __init__ ( self, make, model, year, engine, color, drive_train,
                   mileage, tire_miles, inspection_date, 
                   buy_date, sell_date,
                   plate, tag ):
        """Initialize the attributes for a general car."""
        self.make             = make
        self.model            = model
        self.year             = year
        self.engine           = engine
        self.color            = color
        self.drive_train      = drive_train
        self.mileage          = mileage
        self.tire_miles       = tire_miles
        self.inspection_date  = inspection_date
        self.license_plate    = plate
        self.toll_tag         = tag    
        self.buy_date         = buy_date    
        self.sell_date        = sell_date

    def report_car( self ):
        """ Report all of the information for a general car. """
        car_info = f"\t{self.year} {self.make} {self.model} \n" \
                   + f" Engine Type: \t\t\t{self.engine} \n" \
                   + f" Color: \t\t\t{self.color} \n" \
                   + f" Drive Train: \t\t\t{self.drive_train} \n" \
                   + f" Purchase Date: \t\t{self.buy_date} \n" \
                   + f" Odometer: \t\t\t{self.mileage} \n" \
                   + f" Tires Changed at (miles): \t{self.tire_miles} \n" \
                   + f" Inspection Date: \t\t{self.inspection_date} \n" \
                   + f" License Plate: \t\t{self.license_plate} \n" \
                   + f" Toll Tag:  \t\t\t{self.toll_tag} \n" \
                   + f" Sold Date: \t\t\t{self.sell_date} \n"

        return car_info

    def update_miles( self, new_miles ):
        """ Update the mileage (odometer) for the car. """

        if( new_miles >= self.mileage ):
            self.mileage = new_miles
        else:
            print( "Error, new mileage can't be less than current mileage.")

        
    def update_oil_miles( self, new_miles ):
        """ Update the mileage for the last oil change for the car. """

        if( new_miles >= self.oil_change_miles ):
            self.oil_change_miles = new_miles
        else:
            print( "Error, new oil mileage can't be less than current mileage.")

        
    def update_tire_miles( self, new_miles ):
        """ Update the mileage for the last tire change for the car. """

        if( new_miles >= self.tire_miles and new_miles >= self.mileage ):
            self.tire_miles = new_miles
        else:
            print( "Error, new tire mileage can't be less than current mileage.")

        
    def update_inspection( self, new_date ):
        """ Update the date of the last inspection for the car. """

        self.inspection_date = new_date

################################################################################

""" Subclasses to differentiate electric cars from fossil fuel cars. """

# The Electric car class.
class Ec_Car( Car ):

    def __init__ ( self, make, model, year, engine, color, drive_train,
                   mileage, tire_miles, inspection_date, 
                   plate, tag, max_range, buy_date, sell_date ):
         """ Initialize the attributes for an electric car. """ 
         self.max_range = max_range

         # Initialize the remaining attributes of the 'Car' class.
         super().__init__( make, model, year, engine, color, drive_train,
                   mileage, tire_miles, inspection_date, buy_date, sell_date,
                   plate, tag )
         
    def report_car( self ):
        """" Get the car's information from the parent class. """
        car_info = super().report_car( )
        car_info += f" Max Range (@90%):  \t\t{self.max_range} \n" # add EC_Car specifics

        return car_info


################################################################################

""" Subclasses to differentiate fossil fuel cars from electric cars. """

# The Fossil Fuel car class.
class Ff_Car( Car ):

    def __init__ ( self, make, model, year, engine, color, drive_train,
                   mileage, tire_miles, inspection_date,  
                   plate, tag, oil_change_miles, buy_date, sell_date ):
         
         """ Initialize the attributes for a Fossil fuel car. """ 
         self.oil_change_miles = oil_change_miles

         # Initialize the remaining attributes of the 'Car' class.
         super().__init__( make, model, year, engine, color, drive_train,
                   mileage, tire_miles, inspection_date, buy_date,
                   sell_date, plate, tag )
         
    def report_car( self ):
        """" Get the car's information from the parent class. """
        car_info = super().report_car( )

        # Add Fossil fuel car specifics
        car_info += f" Oil Changed at (miles): \t{self.oil_change_miles} \n"

        return car_info
