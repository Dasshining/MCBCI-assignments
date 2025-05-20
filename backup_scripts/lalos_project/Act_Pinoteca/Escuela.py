class School:
    def __init__(self, s_name, s_country) -> None:
        self._s_name = s_name
        self._s_country = s_country

    @property
    def s_name(self):
        return self._s_name

    @s_name.setter
    def s_name(self, s_name):
        self._s_name = s_name

    @property
    def s_country(self):
        return self._s_country

    @s_country.setter
    def s_country(self, s_country):
        self._s_country = s_country

    def __str__(self):
        return f"Name: {self.s_name}, Country: {self.s_country}"
