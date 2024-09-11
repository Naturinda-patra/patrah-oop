class pet:

    #constructor to initialize the phone object
    def _init_ (self, name, age, type):
        self.name = name
        self.age = age
        self.gender = type

        #method to display person data details
        def display (self):
            print('name: '+ self.name)
            print('age: '+ self.age)
            print('type: '+ self.type)

            #methods for introduction
            def call(self, introduction):
                print('Calling', introduction)

                #define different kinds of the pet 
                dog = pet('dom', '2', 1)

                #call the display method
                dog.display()