class SetupCard:
    def __init__(self, initiative_value, coins, track_values):
        self.initiative_value = initiative_value
        self.coins = coins
        self.track_values = track_values

    def __repr__(self):
        return f"<SetupCard({self.initiative_value}, {self.coins}, {self.track_values})>"
