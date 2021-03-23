class Orange:
    def __init__(self,w,c,m=0):
        """weight in grams
        These are just physical properties"""
        self.weight = w
        self.color = c
        self.mold = m
        print('Created!')

        # This method is changing physical properties from before
    def rot(self, days, temp):
        self.mold = days * temp

orange = Orange(6, 'orange')
print(orange.mold)
orange.rot(10,33)
print('This orange will be rotten in {} days'.format(orange.mold))

