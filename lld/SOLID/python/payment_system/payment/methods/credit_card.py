from ..interface.processable import Processable
from ..interface.refundable import Refundable
from ..interface.validatable import Validatable

class CreditCard(Processable, Validatable, Refundable):
    def process(self):
        return "Credit card is processing"

    def refund(self):
        return "Rufunding using credit card"

    def validate(self):
        return "Validating credit card"
