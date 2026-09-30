from payment.methods.cash import Cash
from payment.methods.credit_card import CreditCard
from payment.methods.upi import UPI
from payment.methods.credit_card import CreditCard


cash = Cash()
upi = UPI()

print(cash.process())
print(upi.process())
