class Patron:
    def __init__(self, pat_name, pat_country, pat_birth_city, pat_death_date) -> None:
        self._pat_name = pat_name
        self._pat_country = pat_country
        self._pat_birth_city = pat_birth_city
        self._pat_death_date = pat_death_date

    @property
    def pat_name(self):
        return self._pat_name

    @pat_name.setter
    def pat_name(self, pat_name):
        self._pat_name = pat_name

    @property
    def pat_country(self):
        return self._pat_country

    @pat_country.setter
    def pat_country(self, pat_country):
        self._pat_country = pat_country

    @property
    def pat_birth_city(self):
        return self._pat_birth_city

    @pat_birth_city.setter
    def pat_birth_city(self, pat_birth_city):
        self._pat_birth_city = pat_birth_city

    @property
    def pat_death_date(self):
        return self._pat_death_date

    @pat_death_date.setter
    def pat_death_date(self, pat_death_date):
        self._pat_death_date = pat_death_date

    def __str__(self):
        return f"Name: {self.pat_name}, Country: {self.pat_country}, City: {self.pat_birth_city}, " \
               f"Death date: {self.pat_death_date}"
