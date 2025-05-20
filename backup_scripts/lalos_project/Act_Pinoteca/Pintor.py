class Painter:
    def __init__(self, name, country, city, school=None, patron=None,
                 birth_date=None, death_date=None) -> None:
        self._name = name
        self._country = country
        self._city = city
        self._school = school
        self._patron = patron
        self._birth_date = birth_date
        self._death_date = death_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def school(self):
        return self._school

    @school.setter
    def school(self, school):
        self._school = school

    @property
    def patron(self):
        return self._patron

    @patron.setter
    def patron(self, patron):
        self._patron = patron

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self._birth_date = birth_date

    @property
    def death_date(self):
        return self._death_date

    @death_date.setter
    def death_date(self, death_date):
        self._death_date = death_date

    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}, City: {self.city}, School: {self.school}, " \
               f"Patron: {self.patron}, Birth date: {self.birth_date}, Death date: {self.death_date}"
