from State import State
from SelectionState import SelectionState

class HasMoneyState(State):
    def __init__(self, machine=None):
        if machine:
            self.machine = machine
            print("Currently Vending machine is in HasMoneyState")

    def click_on_insert_coin_button(self, machine):
        return

    def click_on_start_product_selection_button(self, machine):
        machine.set_vending_machine_state(SelectionState(machine))

    def insert_coin(self, machine, coin):
        print("Accepted the coin")
        machine.get_coin_list().append(coin)

    def choose_product(self, machine, code_number):
        raise Exception("you need to click on start product selection button first")

    def get_change(self, return_change_money):
        raise Exception("you cannot get change in hasMoney state")

    def dispense_product(self, machine, code_number):
        raise Exception("product cannot be dispensed in hasMoney state")

    def refund_full_money(self, machine):
        print("Returned the full amount back in the Coin Dispense Tray")
        machine.set_vending_machine_state(IdleState(machine))
        return machine.get_coin_list()

    def update_inventory(self, machine, item, code_number):
        raise Exception("you cannot update inventory in hasMoney state")
