class employee:

    #constructor to initialize the phone object
    def _init_ (self, name, age, salary):
        self.name = name
        self.age = age
        self.gender = salary

        #method to display person data details
        def display (self):
            print('name: '+ self.name)
            print('age: '+ self.age)
            print('gender: '+ self.salary)

            #methods for introduction
            def call(self, introduction):
                print('Calling', introduction)

                #define different personalities of the person 
                man = employee('eddie', '35', 1000)

                #call the display method
                man.display()