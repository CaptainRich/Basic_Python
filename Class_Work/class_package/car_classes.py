""" Class structure for the 'restaurant' exercise."""

class Car:

    def __init__ ( self, make, model, year, engine, color, drive_train,
                   mileage, oil_change_miles, tire_miles, 
                   inspection_date ):
        """Initialize the attributes for a car."""
        self.make             = make
        self.model            = model
        self.year             = year
        self.engine           = engine
        self.color            = color
        self.drive_train      = drive_train
        self.mileage          = mileage
        self.oil_change_miles = oil_change_miles
        self.tire_miles       = tire_miles
        self.inspection_date  = inspection_date

    def report_car( self ):
        """ Report all of the information for a car. """
        car_info = f"{self.year} {self.make} {self.model} \n" \
                   + f" Engine Type: {self.engine} \n" \
                   + f" Color: {self.color} \n" \
                   + f" Drive Train: {self.drive_train} \n" \
                   + f" Odometer: {self.mileage} \n" \
                   + f" Oil Changed at (miles): {self.oil_change_miles} \n" \
                   + f" Tires Changed at (miles): {self.tire_miles} \n" \
                   + f" Inspection Date: {self.inspection_date} \n"

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

        if( new_miles >= self.tire_change_miles ):
            self.tire_change_miles = new_miles
        else:
            print( "Error, new tire mileage can't be less than current mileage.")

        
    def update_inspection( self, new_date ):
        """ Update the date of the last inspection for the car. """

        self.inspection_date = new_date
      