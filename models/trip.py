class Trip:
    def __init__(self, city_id, country_id, reason, season, timeframe, id=None):
        self.city_id = city_id
        self.country_id = country_id
        self.reason = reason
        self.season = season
        self.timeframe = timeframe
        self.id = id
