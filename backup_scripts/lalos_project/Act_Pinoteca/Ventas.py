class Sales:
    def __init__(self, paint_sold=None, sale_date=None, sale_client=None, sale_price=None, sale_id=None, gallery=None) -> None:
        self._paint_sold = paint_sold
        self._sale_date = sale_date
        self._sale_client = sale_client
        self._sale_price = sale_price
        self._sale_id = sale_id
        self._gallery = gallery

    @property
    def paint_sold(self):
        return self._paint_sold

    @paint_sold.setter
    def paint_sold(self, paint_sold):
        self._paint_sold = paint_sold

    @property
    def sale_date(self):
        return self._sale_date

    @sale_date.setter
    def sale_date(self, sale_date):
        self._sale_date = sale_date

    @property
    def sale_client(self):
        return self._sale_client

    @sale_client.setter
    def sale_client(self, sale_client):
        self._sale_client = sale_client

    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, sale_price):
        self._sale_price = sale_price

    @property
    def sale_id(self):
        return self._sale_id

    @sale_id.setter
    def sale_id(self, sale_id):
        self._sale_id = sale_id

    @property
    def gallery(self):
        return self._gallery

    @gallery.setter
    def gallery(self, gallery):
        self._gallery = gallery

    def __str__(self):
        return f"Paint Sold: {self.paint_sold}, Date of sale: {self.sale_date}, Client: {self.sale_client}, " \
               f"Price: {self.sale_price}, ID: {self.sale_id}, Gallery: {self.gallery}"
