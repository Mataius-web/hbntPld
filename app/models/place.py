@property
def latitude(self):
    return self._latitude

@latitude.setter
def latitude(self, value):
    if not -90 <= value <= 90:
        raise ValueError("la latitude doit etre comprise entre -90 et 90")
    self._latitude = value
