class Dogs:
    def __init__(self, name, activities):
        self.name = name
        self.activities = activities

    def __repr__(self):
        return f"{self.name} is {self.activities}"