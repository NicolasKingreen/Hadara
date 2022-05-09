class Statue:

    def __init__(self, culture, counter, victory_points, selected_value=None):
        self.culture = culture
        self.counter = counter
        self.victory_points = victory_points
        self.selected_value = selected_value

    def __repr__(self):
        return f"<Structure({self.culture}, {self.counter}, {self.victory_points})>"

    def __str__(self):
        return f"Culture required: {self.culture} " \
               f"Bonus: {self.counter} to ({self.selected_value or 'has to be chosen'}) " \
               f"Victory points: {self.victory_points}"

    def set_bonus_value(self, bonus_value):
        self.selected_value = bonus_value
