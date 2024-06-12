import random

class MTNSim:
    def __init__(self):
        self.sims = {}
        self.main_account = 0

    def buy_sim(self, name):
        if name in self.sims:
            return False
        else:
            sim_number = self.generate_sim_number()
            self.sims[name] = sim_number
            return sim_number

    def generate_sim_number(self):
        return '250' + str(random.randint(1000000000, 9999999999))

    def check_pin(self, sim_number, pin):
        if sim_number in self.sims and self.sims[sim_number] == pin:
            return True
        else:
            return False

    def send_money(self, sim_number, recipient_number, amount):
        if self.check_pin(sim_number, recipient_number):
            if self.main_account >= amount:
                self.main_account -= amount
                return True
            else:
                return False
        else:
            return False

    def add_money(self, sim_number, amount):
        if sim_number in self.sims:
            self.main_account += amount
            return True
        else:
            return False

# Example usage
mtn = MTNSim()

# Buy a sim card
sim_number = mtn.buy_sim('John Doe')
print(f'Your sim number is: {sim_number}')

# Set pin
pin = int(sim_number[4:])

# Add money to account
mtn.add_money(sim_number, 30000)

# Check balance
print(f'Your balance is: {mtn.main_account} RWF')

# Send money
success = mtn.send_money(sim_number, '250788888888', 2000)
if success:
    print('Money sent successfully')
else:
    print('Failed to send money')

# Check balance
print(f'Your balance is: {mtn.main_account} RWF')