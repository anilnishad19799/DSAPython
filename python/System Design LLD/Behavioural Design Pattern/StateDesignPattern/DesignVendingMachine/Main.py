from VendingMachine import VendingMachine
from Coin import Coin
from ItemType import ItemType
from Item import Item

def fill_up_inventory(vending_machine):
    slots = vending_machine.get_inventory().get_inventory()
    for i in range(len(slots)):
        new_item = Item(None, 0)
        if 0 <= i < 3:
            new_item.set_type(ItemType.COKE)
            new_item.set_price(12)
        elif 3 <= i < 5:
            new_item.set_type(ItemType.PEPSI)
            new_item.set_price(9)
        elif 5 <= i < 7:
            new_item.set_type(ItemType.JUICE)
            new_item.set_price(13)
        elif 7 <= i < 10:
            new_item.set_type(ItemType.SODA)
            new_item.set_price(7)
        slots[i].set_item(new_item)
        slots[i].set_sold_out(False)

def display_inventory(vending_machine):
    slots = vending_machine.get_inventory().get_inventory()
    for slot in slots:
        print(f"CodeNumber: {slot.get_code()} Item: {slot.get_item().get_type().name} Price: {slot.get_item().get_price()} isAvailable: {not slot.is_sold_out()}")

if __name__ == "__main__":
    vending_machine = VendingMachine()
    try:
        print("|")
        print("Filling up the inventory")
        print("|")

        fill_up_inventory(vending_machine)
        display_inventory(vending_machine)

        print("|")
        print("Clicking on InsertCoinButton")
        print("|")

        vending_state = vending_machine.get_vending_machine_state()
        vending_state.click_on_insert_coin_button(vending_machine)

        vending_state = vending_machine.get_vending_machine_state()
        vending_state.insert_coin(vending_machine, Coin.NICKEL)
        vending_state.insert_coin(vending_machine, Coin.QUARTER)
        # vending_state.insert_coin(vending_machine, Coin.NICKEL)

        print("|")
        print("Clicking on ProductSelectionButton")
        print("|")
        vending_state.click_on_start_product_selection_button(vending_machine)

        vending_state = vending_machine.get_vending_machine_state()
        vending_state.choose_product(vending_machine, 102)

        display_inventory(vending_machine)

    except Exception as e:
        display_inventory(vending_machine)
        print(f"Exception: {e}")
