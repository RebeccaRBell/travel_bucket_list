class Trip:
    def __init__(
        self,
        continent_id,
        country_id,
        city_id,
        reason,
        season,
        timeframe,
        completed,
        id=None,
    ):
        self.continent_id = continent_id
        self.country_id = country_id
        self.city_id = city_id
        self.reason = reason
        self.season = season
        self.timeframe = timeframe
        self.completed = completed
        self.id = id
