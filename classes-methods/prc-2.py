class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18

hamlet = Piglet()
print(hamlet.pig_years())

hamlet.years = 2
print(hamlet.pig_years())