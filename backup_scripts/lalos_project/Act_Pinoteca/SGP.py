import re
from Cuadros import Paintings
from Pintor import Painter
from Pinoteca import Gallery
from clientes import Clients
from Escuela import School
from Mecenas import Patron
from Ventas import Sales


class SGP:
    def __init__(self):
        self.paintings = []
        self.painters = []
        self.galleries = []
        self.clients = []
        self.schools = []
        self.sales = []
        self.patrons = []
        self.list_of_paints_in_each_gall = []

# ------------------------------------------------VAL EXPRESSIONS-----------------------------------------------------

    def val_name(self, name):
        name_er = "[a-zA-Záéíóúñ0-9 ]{3,}"
        matcher = re.compile(name_er)
        match = matcher.match(name)
        return match

    def val_date(self, date):
        db_er = "([0-2][0-9]|[3][0-1]).([0][1-9]|[1][0-2]).([0-2][0-9][0-9][0-9])"
        matcher = re.compile(db_er)
        match = matcher.fullmatch(date)
        return match

# -------------------------------------------------PAINTINGS----------------------------------------------------------
    def register_painting(self):
        print("Introduce the painting elements")

        while True:
            painting_name = input("Paint: ")
            if self.val_name(painting_name):
                break
            else:
                print("Incorrect format, input again")

        painting_id = input("Paint ID: ")

        while True:
            painter_name = input("Painter: ")
            if self.val_name(painter_name):
                break
            else:
                print("Incorrect format, input again")

        painting_in_gallery = input("Gallery: ")

        while True:
            painting_length = float(input("Length (m): "))
            painting_width = float(input("Width (m): "))
            painting_size = painting_width * painting_length
            if painting_size <= 1:
                break
            else:
                print("Painting size must not exceed 1 m2, reenter length and width")

        while True:
            painting_date = input("Date (dd.mm.yyyy): ")
            if self.val_date(painting_date):
                break
            else:
                print("Incorrect format, input again")

        painting_technique = input("Technique: ")

        existent_painter = self.painter_painting_relation(painter_name)
        existent_gallery = self.gallery_painting_relation(painting_in_gallery)
        find_dup = self.find_duplicate_painting(painting_name)

        if existent_painter and existent_gallery:
            new_paint = Paintings(painting_id, painting_name, painter_name, painting_in_gallery, painting_length,
                                  painting_width, painting_date, painting_technique)
            if find_dup:
                print("Painting name already in list, do not duplicate entries")
            if not find_dup:
                self.paintings.append(new_paint)
                print("New item added to Paintings")

        if existent_painter and not existent_gallery:
            print("Gallery not registered, please first register gallery to make association to painting")

        if existent_gallery and not existent_painter:
            print("Painter not registered, please first register painter to make association to painting")

        if not existent_gallery and not existent_painter:
            print("Painter and gallery not registered, please first register painter and gallery to make association "
                  "to painting")

    def find_duplicate_painting(self, painting_name):
        for painting in self.paintings:
            if painting.paint_name == painting_name:
                return painting
        return None

    def erase_painting(self):
        erase = input("ID:  ")
        for painting in self.paintings:
            if painting.code == erase:
                self.paintings.remove(painting)
                break
        print("Item removed")

    def modify_painting(self):
        print("What painting would you like to modify?")
        self.show_painting()
        print("\n")
        mod_item = int(input("Choose index: "))
        print("Introduce new painting elements")

        while True:
            painting_name = input("Paint: ")
            if self.val_name(painting_name):
                break
            else:
                print("Incorrect format, input again")

        painting_id = input("ID: ")

        while True:
            painting_length = float(input("Length (m): "))
            painting_width = float(input("Width (m): "))
            painting_size = painting_width * painting_length
            if painting_size <= 1:
                break
            else:
                print("Painting size must not exceed 1 m2, reenter length and width")

        while True:
            painting_date = input("Date (dd.mm.yyyy): ")
            if self.val_date(painting_date):
                break
            else:
                print("Incorrect format, input again")

        painting_technique = input("Technique: ")
        new_paint2 = Paintings(painting_id, painting_name, painting_length, painting_width,
                               painting_date, painting_technique)
        self.paintings[mod_item - 1] = new_paint2
        print("\n")
        print("Element modified")
        print(self.paintings[mod_item - 1])

    def show_painting(self):
        if self.paintings == []:
            print("Paintings list empty")
        else:
            for index, each in enumerate(self.paintings):
                print(f"{index+1}:  {each}")

    def painter_painting_relation(self, painter_n):
        for painter in self.painters:
            if painter.name == painter_n:
                return painter
        return None

    def gallery_painting_relation(self, gallery_n):
        for gallery in self.galleries:
            if gallery.name == gallery_n:
                return gallery
        return None

# ---------------------------------------------------PAINTER----------------------------------------------------------

    def register_painter(self):
        print("Introduce the painter elements")

        while True:
            painter_name = input("Name: ")
            if self.val_name(painter_name):
                break
            else:
                print("Incorrect format, input again")

        painter_country = input("Country: ")
        painter_city = input("City: ")
        painter_school = input("School: ")
        painter_patron = input("Patron: ")

        while True:
            painter_bd = input("Birth date (dd.mm.yyyy): ")
            if self.val_date(painter_bd):
                break
            else:
                print("Incorrect format, input again")

        while True:
            painter_dd = input("Death date (dd.mm.yyyy): ")
            if self.val_date(painter_dd):
                break
            else:
                print("Incorrect format, input again")

        existent_school = self.painter_school_relation(painter_school)
        existent_patron = self.painter_patron_relation(painter_patron)
        find_dup = self.find_duplicate_painter(painter_name)

        if existent_school and existent_patron:
            new_painter = Painter(painter_name, painter_country, painter_city, painter_school, painter_patron,
                                  painter_bd, painter_dd)
            if find_dup:
                print("Painter name already in list, do not duplicate entries")
            if not find_dup:
                self.painters.append(new_painter)
                print("New item added to Painters")

        if existent_school and not existent_patron:
            print("Patron not registered, please first register patron to make association to painter")

        if existent_patron and not existent_school:
            print("School not registered, please first register school to make association to painting")

        if not existent_school and not existent_patron:
            print("School and Patron not registered, please first register school and patron to make association "
                  "to painter")

    def find_duplicate_painter(self, painter_name):
        for painter in self.painters:
            if painter.name == painter_name:
                return painter
        return None

    def erase_painter(self):
        erase = input("Painter: ")
        for painter in self.painters:
            if painter.name == erase:
                self.painters.remove(painter)
                break
        print("Item removed")

    def modify_painter(self):
        print("What painter would you like to modify?")
        self.show_painter()
        print("\n")
        mod_item = int(input("Choose index: "))
        print("Introduce new painter elements")

        while True:
            painter_name = input("Name: ")
            if self.val_name(painter_name):
                break
            else:
                print("Incorrect format, input again")

        painter_country = input("Country: ")
        painter_city = input("City: ")

        while True:
            painter_bd = input("Birth date (dd.mm.yyyy): ")
            if self.val_date(painter_bd):
                break
            else:
                print("Incorrect format, input again")

        while True:
            painter_dd = input("Death date (dd.mm.yyyy): ")
            if self.val_date(painter_dd):
                break
            else:
                print("Incorrect format, input again")

        new_painter2 = Painter(painter_name, painter_country, painter_city, painter_bd, painter_dd)
        self.painters[mod_item - 1] = new_painter2
        print("\n")
        print("Element modified")
        print(self.painters[mod_item - 1])

    def show_painter(self):
        if self.painters == []:
            print("Painters list empty")
        else:
            for index, each in enumerate(self.painters):
                print(f"{index+1}:  {each}")

    def painter_school_relation(self, school_n):
        for school in self.schools:
            if school.s_name == school_n:
                return school
        return None

    def painter_patron_relation(self, patron_n):
        for patron in self.patrons:
            if patron.pat_name == patron_n:
                return patron
        return None

# --------------------------------------------------GALLERY-----------------------------------------------------------

    def register_gallery(self):
        print("Introduce the gallery elements")

        gall_dir = input("Direction: ")
        gall_name = input("Name: ")
        gall_city = input("City: ")
        gall_length = float(input("Length (m): "))
        gall_width = float(input("Width (m): "))
        new_gall = Gallery(gall_dir, gall_name, gall_city, gall_length, gall_width)
        find_dup = self.find_duplicate_gallery(gall_name)

        if find_dup:
            print("Gallery name already in list, do not duplicate entries")
        if not find_dup:
            self.galleries.append(new_gall)
            print("New item added to Galleries")

    def find_duplicate_gallery(self, gall_name):
        for gallery in self.galleries:
            if gallery.name == gall_name:
                return gallery
        return None

    def erase_gallery(self):
        erase = input("Gallery: ")
        for gallery in self.galleries:
            if gallery.name == erase:
                self.galleries.remove(gallery)
                break
        print("Item removed")

    def modify_gallery(self):
        print("What gallery would you like to modify?")
        self.show_gallery()
        print("\n")
        mod_item = int(input("Choose index: "))
        print("Introduce new gallery elements")

        gall_dir = input("Direction: ")
        gall_name = input("Name: ")
        gall_city = input("City: ")
        gall_length = float(input("Length (m): "))
        gall_width = float(input("Width (m): "))
        new_gall2 = Gallery(gall_dir, gall_name, gall_city, gall_length, gall_width)

        self.galleries[mod_item - 1] = new_gall2
        print("\n")
        print("Element modified")
        print(self.galleries[mod_item - 1])

    def show_gallery(self):
        if self.galleries == []:
            print("Galleries list empty")
        else:
            for index, each in enumerate(self.galleries):
                print(f"{index+1}:  {each}")

# ---------------------------------------------------CLIENTS-----------------------------------------------------------
    def register_client(self):
        print("Introduce the client elements")

        while True:
            client_name = input("Client name: ")
            if self.val_name(client_name):
                break
            else:
                print("Incorrect format, input again")

        while True:
            client_bd = input("Birth date (dd.mm.yyyy): ")
            if self.val_date(client_bd):
                break
            else:
                print("Incorrect format, input again")

        client_residence = input("Residence: ")
        new_client = Clients(client_name, client_bd, client_residence)
        find_dup = self.find_duplicate_client(client_name)

        if find_dup:
            print("Client name already in list, do not duplicate entries")
        if not find_dup:
            self.clients.append(new_client)
            print("New item added to Clients")

    def find_duplicate_client(self, client_name):
        for client in self.clients:
            if client.client_name == client_name:
                return client
        return None

    def erase_client(self):
        erase = input("Client: ")
        for client in self.clients:
            if client.client_name == erase:
                self.clients.remove(client)
                break
        print("Item removed")

    def modify_client(self):
        print("What client would you like to modify?")
        self.show_client()
        print("\n")
        mod_item = int(input("Choose index: "))
        print("Introduce new client elements")

        while True:
            client_name = input("Client name: ")
            if self.val_name(client_name):
                break
            else:
                print("Incorrect format, input again")

        while True:
            client_bd = input("Birth date (dd.mm.yyyy): ")
            if self.val_date(client_bd):
                break
            else:
                print("Incorrect format, input again")

        client_residence = input("Residence: ")
        new_client2 = Clients(client_name, client_bd, client_residence)

        self.clients[mod_item - 1] = new_client2
        print("\n")
        print("Element modified")
        print(self.clients[mod_item - 1])

    def show_client(self):
        if self.clients == []:
            print("Clients list empty")
        else:
            for index, each in enumerate(self.clients):
                print(f"{index+1}:  {each}")

# --------------------------------------------------SCHOOLS----------------------------------------------------------

    def register_school(self):
        print("Introduce the school elements")
        school_name = input("Name: ")
        school_country = input("Country: ")
        new_school = School(school_name, school_country)
        find_dup = self.find_duplicate_school(school_name)
        if find_dup:
            print("School name already in list, do not duplicate entries")
        if not find_dup:
            self.schools.append(new_school)
            print("New item added to Schools")

    def find_duplicate_school(self, school_name):
        for school in self.schools:
            if school.s_name == school_name:
                return school
        return None

    def erase_school(self):
        erase = input("School: ")
        for school in self.schools:
            if school.s_name == erase:
                self.schools.remove(school)
                break
        print("Item removed")

    def modify_school(self):
        print("What school would you like to modify?")
        self.show_school()
        print("\n")
        mod_item = int(input("Choose index: "))
        print("Introduce new school elements")

        school_name = input("Name: ")
        school_country = input("Country: ")
        new_school2 = School(school_name, school_country)

        self.schools[mod_item - 1] = new_school2
        print("\n")
        print("Element modified")
        print(self.schools[mod_item - 1])

    def show_school(self):
        if self.schools == []:
            print("Schools list empty")
        else:
            for index, each in enumerate(self.schools):
                print(f"{index+1}:  {each}")

# # --------------------------------------------------SALES-----------------------------------------------------------

    def register_sale(self):
        print("Introduce the sale elements")
        paint_sold = input("Painting Sold: ")
        sale_date = input("Date of sale (dd.mm.yyyy): ")
        sale_client = input("Client: ")
        sale_price = input("Price: ")
        sale_id = input("Paint ID: ")
        sale_gallery = input("Gallery: ")

        existent_client = self.sale_client_relation(sale_client)
        existent_painting = self.sale_painting_relation(paint_sold)
        find_dup = self.find_duplicate_sale(sale_id)

        if existent_client and existent_painting:
            new_sale = Sales(paint_sold, sale_date, sale_client, sale_price, sale_id, sale_gallery)
            if find_dup:
                print("Paint ID already in list of sales, item already sold")
            if not find_dup:
                self.sales.append(new_sale)
                self.erase_painting_after_sold(paint_sold)
                print("New item added to Sales")

        if existent_client and not existent_painting:
            print("Painting not in inventory, cannot sell")

        if not existent_client and existent_painting:
            print("Client not registered, please first register client to make association to sale")

        if not existent_client and not existent_painting:
            print("Client not registered, please first register client to make association to sale")
            print("Painting not in inventory, cannot sell")

    def find_duplicate_sale(self, sale_id):
        for sale in self.sales:
            if sale.sale_id == sale_id:
                return sale
        return None

    def erase_sale(self):
        erase = input("Sale ID: ")
        for sale in self.sales:
            if sale.sale_id == erase:
                self.sales.remove(sale)
                break
        print("Item removed")

    def modify_sale(self):
        print("What sale would you like to modify?")
        self.show_sale()
        print("\n")
        mod_item = int(input("Choose index: "))
        print("Introduce new sale elements")

        paint_sold = input("Painting Sold: ")
        sale_date = input("Date of sale (dd.mm.yyyy): ")
        sale_client = input("Client: ")
        sale_price = input("Price: ")
        sale_id = input("Paint ID: ")
        sale_gallery = input("Gallery: ")
        new_sale2 = Sales(paint_sold, sale_date, sale_client, sale_price, sale_id, sale_gallery)

        self.sales[mod_item - 1] = new_sale2
        print("\n")
        print("Element modified")
        print(self.sales[mod_item - 1])

    def show_sale(self):
        if self.sales == []:
            print("Sales list empty")
        else:
            for index, each in enumerate(self.sales):
                print(f"{index+1}:  {each}")

    def sale_client_relation(self, client_n):
        for client in self.clients:
            if client.client_name == client_n:
                return client
        return None

    def sale_painting_relation(self, paint_sold):
        for painting in self.paintings:
            if painting.paint_name == paint_sold:
                return painting
        return None

    def erase_painting_after_sold(self, paint_sold):
        erase = paint_sold
        for painting in self.paintings:
            if painting.paint_name == erase:
                self.paintings.remove(painting)
                break
        print("Item sold removed from inventory")

# ---------------------------------------------------PATRONS----------------------------------------------------------

    def register_patron(self):
        print("Introduce the patron elements")
        pat_name = input("Name: ")
        pat_country = input("Country: ")
        pat_bc = input("Birth city: ")
        pat_dc = input("Death date (dd.mm.yyyy): ")
        new_patron = Patron(pat_name, pat_country, pat_bc, pat_dc)
        find_dup = self.find_duplicate_patron(pat_name)

        if find_dup:
            print("Patron name already in list, do not duplicate entries")
        if not find_dup:
            self.patrons.append(new_patron)
            print("New item added to Patrons")

    def find_duplicate_patron(self, pat_name):
        for patron in self.patrons:
            if patron.pat_name == pat_name:
                return patron
        return None

    def erase_patron(self):
        erase = input("Patron: ")
        for patron in self.patrons:
            if patron.pat_name == erase:
                self.patrons.remove(patron)
                break
        print("Item removed")

    def modify_patron(self):
        print("What patron would you like to modify?")
        self.show_patron()
        print("\n")
        mod_item = int(input("Choose index: "))
        print("Introduce new patron elements")

        pat_name = input("Name: ")
        pat_country = input("Country: ")
        pat_bc = input("Birth city: ")
        pat_dd = input("Death date: ")
        new_patron2 = Patron(pat_name, pat_country, pat_bc, pat_dd)

        self.patrons[mod_item - 1] = new_patron2
        print("\n")
        print("Element modified")
        print(self.patrons[mod_item - 1])

    def show_patron(self):
        if self.patrons == []:
            print("Patrons list empty")
        else:
            for index, each in enumerate(self.patrons):
                print(f"{index+1}:  {each}")
