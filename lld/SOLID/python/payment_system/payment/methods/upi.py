from ..interface.processable import Processable
from ..interface.refundable import Refundable
from ..interface.validatable import Validatable


class UPI(Processable, Refundable, Validatable):
    def process(self):
        return "UPI is processing"

    def refund(self):
        return "Rufunding using UPI"

    def validate(self):
        return "Validating UPI"
