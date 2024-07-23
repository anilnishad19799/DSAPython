from design_vending_machine.item_shelf import ItemShelf

class Inventory:
    def __init__(self, item_count):
        self.inventory = [ItemShelf() for _ in range(item_count)]
        self.initial_empty_inventory()

    def initial_empty_inventory(self):
        start_code = 101
        for i, space in enumerate(self.inventory):
            space.code = start_code
            space.sold_out = True
            start_code += 1

    def add_item(self, item, code_number):
        for item_shelf in self.inventory:
            if item_shelf.code == code_number:
                if item_shelf.sold_out:
                    item_shelf.item = item
                    item_shelf.sold_out = False
                else:
                    raise Exception("Item already present, cannot add item here")

    def get_item(self, code_number):
        for item_shelf in self.inventory:
            if item_shelf.code == code_number:
                if item_shelf.sold_out:
                    raise Exception("Item already sold out")
                return item_shelf.item
        raise Exception("Invalid Code")

    def update_sold_out_item(self, code_number):
        for item_shelf in self.inventory:
            if item_shelf.code == code_number:
                item_shelf.sold_out = True
