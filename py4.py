class StoreItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        pass

class MusicalInstrument(StoreItem):
    def __init__(self, name, price, category):
        super().__init__(name, price)
        self.category = category

    def get_description(self):
        return f"{self.name} - {self.category} - ${self.price}"

class CD(StoreItem):
    def __init__(self, name, price, artist):
        super().__init__(name, price)
        self.artist = artist

    def get_description(self):
        return f"{self.name} by {self.artist} - ${self.price}"

class Guitar(MusicalInstrument):
    def __init__(self, name, price, category, strings):
        super().__init__(name, price, category)
        self.strings = strings

    def get_description(self):
        return f"{self.name} {self.category} Guitar with {self.strings} strings - ${self.price}"

class Piano(MusicalInstrument):
    def __init__(self, name, price, category, keys):
        super().__init__(name, price, category)
        self.keys = keys

    def get_description(self):
        return f"{self.name} {self.category} Piano with {self.keys} keys - ${self.price}"

class MusicStore:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def display_inventory(self):
        print(f"Inventory of {self.name}:")

        for item in self.inventory:
            print(item.get_description())

if __name__ == "__main__":
    store = MusicStore("Melody Music Store")

    guitar = Guitar("Fender Stratocaster", 1200, "Electric", 6)
    piano = Piano("Yamaha Grand", 5000, "Grand", 88)
    cd = CD("Greatest Hits", 15, "Various Artists")

    store.add_item(guitar)
    store.add_item(piano)
    store.add_item(cd)

    store.display_inventory()
