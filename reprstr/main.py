class location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location(latitude = {self.latitude}, longitude = {self.longitude})"

    def __str__(self):
        return f"Location(latitude = {self.latitude}, longitude = {self.longitude})"


bham_academy = location(52.54764, -1.3243242)
print(bham_academy)