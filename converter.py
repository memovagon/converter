class Converter:

   def __init__(self):
    self.y2m = 0.91
    self.m2y = 1.09361

   def yard_to_meter(self, value):
       return value * self.y2m

   def meter_to_yard(self, value):
       return value * self.m2y

