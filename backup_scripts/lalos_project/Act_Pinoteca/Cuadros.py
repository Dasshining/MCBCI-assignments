class Paintings:
    def __init__(self, code, paint_name, painter_name, painting_in_gallery=None, paint_length=None,
                 paint_width=None, date=None, technique=None) -> None:
        self._code = code
        self._paint_name = paint_name
        self._painter_name = painter_name
        self._painting_in_gallery = painting_in_gallery
        self._paint_length = paint_length
        self._paint_width = paint_width
        self._date = date
        self._technique = technique

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):

        self._code = code

    @property
    def paint_name(self):
        return self._paint_name

    @paint_name.setter
    def paint_name(self, paint_name):
        self._paint_name = paint_name

    @property
    def painter_name(self):
        return self._painter_name

    @painter_name.setter
    def painter_name(self, painter_name):
        self._painter_name = painter_name

    @property
    def painting_in_gallery(self):
        return self._painting_in_gallery

    @painting_in_gallery.setter
    def painting_in_gallery(self, painting_in_gallery):
        self._painting_in_gallery = painting_in_gallery

    @property
    def paint_length(self):
        return self._paint_length

    @paint_length.setter
    def paint_length(self, paint_length):
        self._paint_length = paint_length

    @property
    def paint_width(self):
        return self._paint_width

    @paint_width.setter
    def paint_width(self, paint_width):
        self._paint_width = paint_width

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def technique(self):
        return self._technique

    @technique.setter
    def technique(self, technique):
        self._technique = technique

    def __str__(self):
        return f"ID: {self.code}, Name: {self.paint_name}, Painter: {self.painter_name}, " \
               f"Gallery: {self.painting_in_gallery}, Length(m): {self.paint_length}, Width(m): {self.paint_width}, " \
               f"Date: {self.date}, Technique: {self.technique}"
