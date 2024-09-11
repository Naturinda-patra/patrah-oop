class person:

    #constructor to initialize the phone object
    def _init_ (self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

        #method to display person data details
        def display (self):
            print('name: '+ self.name)
            print('age: '+ self.age)
            print('gender: '+ self.gender)

            #methods for introduction
            def call(self, introduction):
                print('Calling', introduction)

                #define different personalities of the person 
                man = person('isaac', '25', 1)

                #call the display method
                man.display()