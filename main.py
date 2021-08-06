# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math


class StraightLine:

    def __init__(self, numx1, numy1, name, numx2, numy2, name2):
        self.numx1 = numx1
        self.numy1 = numy1
        self.name = name
        self.numx2 = numx2
        self.numy2 = numy2
        self.name2 = name2

    def input_attributes(self):
        self.numx1 = float(input("faka ux wepoyinti yoluqala    :"))
        self.numy1 = float(input("faka uy wepoyinti yoluqala    :"))
        self.name  = input("Bhala igama lepoyinti yoluqala      :")
        self.numx2 = float(input("faka ux wepoyinti yesibini    :"))
        self.numy2 = float(input("faka uy wepoyinti yesibini    :"))
        self.name2 = input("Faka igama le poyinti yesibini      :")

    def calculate_dist(self):
        return math.sqrt(math.pow(self.numx2 - self.numx1, 2) + math.pow(self.numy2 - self.numy1, 2))

    def equation(self):
        return (self.numy2 - self.numy1) / (self.numx2 - self.numx1)

    def quadrant(self):
        if self.numx1 > 0 and self.numy1 > 0:
            print("Ikwi gumbi elise North est")

        elif self.numx1 < 0 and self.numy1 > 0:
            print("Ikwi gumbi elise North west")

        elif self.numx1 < 0 and self.numy1 < 0:
            print("Ikwi gumbi elise South west")

        elif self.numx1 > 0 and self.numy1 < 0:
            print("Ikwi gumbi elise South est")

        elif self.numx1 == 0 and self.numy1 == 0:
            print("isesiphakathini")
        else:
            print("ayikho nakwelinye igumbi")

    def ref_pointx(self):

        if (self.numx1 > 0 and self.numy1 > 0):
            print("Isithunzi sayo xa uyithelekisa ne x-axis ", self.numx1, ","+"-", self.numy1);

        elif self.numx1 < 0 and self.numy1 > 0:
            print("Isithunzi sayo xa uyithelekisa ne x-axis  ", self.numx1, ","+"-", self.numy1);

        elif self.numx1 < 0 and self.numy1 < 0:
            print("Isithunzi sayo xa uyithelekisa ne x-axis  ", self.numx1, ",", self.numy1);

        elif self.numx1 > 0 and self.numy1 < 0:
            print("Isithunzi sayo xa uyithelekisa ne x-axis ", self.numx1, ",", self.numy1);

        elif self.numx1 == 0 and self.numy1 == 0:
            print("Isesiphakathini,akho sithunzi")

    def ref_pointy(self):

        if self.numx1 > 0 and self.numy1 > 0:
            print("Isithunzi sayo xa uyithelekisa ne y-axis "+"-", self.numx1, ",", self.numy1)

        elif self.numx1 < 0 and self.numy1 > 0:
            print("Isithunzi sayo xa uyithelekisa ne y-axis  ", self.numx1, ",", self.numy1)

        elif self.numx1 < 0 and self.numy1 < 0:
            print("Isithunzi sayo xa uyithelekisa ne y-axis  ", self.numx1, ",", self.numy1)

        elif self.numx1 > 0 and self.numy1 < 0:
            print("Isithunzi sayo xa uyithelekisa ne x-axis  "+"-", self.numx1, ",", self.numy1)

        elif self.numx1 == 0 and self.numy1 == 0:
            print("Isesiphakathini,akho sithunzi ")


    def output(self):
        print("umahluko phakathi kwezi poyint ngu ", self.calculate_dist(), "meters")
        self.quadrant()
        self.ref_pointy()
        self.ref_pointx()
        print("\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = StraightLine(2.0, 5.8, "poi", 4.8, 10.10, "mile")
    a.output()
    obj=StraightLine(0.0,0.0,"",0.0,0.0,"")
    a.input_attributes()
    a.output()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
