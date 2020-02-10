class User():
    def __init__(self,name="bot", age=35):
        self.name = name
        self.age = age

    def print_all(self):
        return "{} возрастом {}".format(self.name, str(self.age))

    def print_to_file(self, file_name):
        file = open(file_name, "wt")
        file.write(self.print_all())
        file.close()

    def read_from_file(self, file_name):
        file = open(file_name, "rt")
        read_file = file.read()
        file.close()
        # something changed
        
        return read_file
