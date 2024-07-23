from State import State
from HasMoneyState import HasMoneyState

class IdleState(State):
    def __init__(self, machine=None):
        if machine:
            self.machine = machine
            print("Currently Vending machine is in IdleState")
            self.machine.set_coin_list([])

    def click_on_insert_coin_button(self, machine):
        machine.set_vending_machine_state(HasMoneyState(machine))

    def click_on_start_product_selection_button(self, machine):
        raise Exception("first you need to click on insert coin button")

    def insert_coin(self, machine, coin):
        raise Exception("you cannot insert Coin in idle state")

    def choose_product(self, machine, code_number):
        raise Exception("you cannot choose Product in idle state")

    def get_change(self, return_change_money):
        raise Exception("you cannot get change in idle state")

    def refund_full_money(self, machine):
        raise Exception("you cannot get refunded in idle state")

    def dispense_product(self, machine, code_number):
        raise Exception("product cannot be dispensed in idle state")

    def update_inventory(self, machine, item, code_number):
        machine.get_inventory().add_item(item, code_number)
