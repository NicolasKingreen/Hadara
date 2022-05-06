class Structure:

    def __init__(self, culture, counter, victory_points):
        self.culture = culture
        self.counter = counter
        self.selected_value = None
        self.victory_points = victory_points

    def __repr__(self):
        return f"<Structure({self.culture}, {self.counter}, {self.victory_points})>"
