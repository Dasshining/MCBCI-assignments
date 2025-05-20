class Clients:
    def __init__(self, client_name, client_birth_date, residence) -> None:
        self._client_name = client_name
        self._client_birth_date = client_birth_date
        self._residence = residence

    @property
    def client_name(self):
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        self._client_name = client_name

    @property
    def client_birth_date(self):
        return self._client_birth_date

    @client_birth_date.setter
    def client_birth_date(self, client_birth_date):
        self._client_birth_date = client_birth_date

    @property
    def residence(self):
        return self._residence

    @residence.setter
    def residence(self, residence):
        self._residence = residence

    def __str__(self):
        return f"Name: {self.client_name}, Birth date: {self.client_birth_date}, Residence: {self.residence}"
