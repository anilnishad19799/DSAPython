from State import State
from IdleState import IdleState

class DispenseState(State):
    def __init__(self, machine=None, code_number=None):
        if machine and code_number is not None:
            self.machine = machine
            self.code_number = code_number
            print("Currently Vending machine is in DispenseState")
            self.dispense_product(machine, code_number)

    def click_on_insert_coin_button(self, machine):
        raise Exception("insert coin button cannot be clicked in Dispense state")

    def click_on_start_product_selection_button(self, machine):
        raise Exception("product selection button cannot be clicked in Dispense state")

    def insert_coin(self, machine, coin):
        raise Exception("coin cannot be inserted in Dispense state")

    def choose_product(self, machine, code_number):
        raise Exception("product cannot be chosen in Dispense state")

    def get_change(self, return_change_money):
        raise Exception("change cannot be returned in Dispense state")

    def refund_full_money(self, machine):
        raise Exception("refund cannot happen in Dispense state")

    def dispense_product(self, machine, code_number):
        print("Product has been dispensed")
        item = machine.get_inventory().get_item(code_number)
        machine.get_inventory().update_sold_out_item(code_number)
        machine.set_vending_machine_state(IdleState(machine))
        return item

    def update_inventory(self, machine, item, code_number):
        raise Exception("inventory cannot be updated in Dispense state")
