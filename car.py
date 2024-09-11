class car:

    #constructor to initialize the phone object
    def _init_ (self, brand, model, year):
        self.brand = brand
        self.model= model
        self.year = year

        #method to display person data details
        def display (self):
            print('brand: '+ self.brand)
            print('model: '+ self.model)
            print('year: '+ self.year)

            #methods to call
            def drive(self, number):
                print('driving', number)

                #create an object of the car class 
                toyota = car('vitz', 'vitz old', 2000)

                #drive the display method
                toyota.display()