class Dogs:

    def __init__(self, name, activities):
        self.name = name
        self.activities = activities

    def __repr__(self):
        return f"Dog {self.name}: is doing - {self.activities}"
