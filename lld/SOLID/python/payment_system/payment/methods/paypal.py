from ..interface.processable import Processable
from ..interface.refundable import Refundable
from ..interface.validatable import Validatable

class PayPal(Processable, Refundable, Validatable):
    def process(self):
        return "paypal processing"

    def validate(self):
        return "paypal validating"

    def refund(self):
        return "paypal refunding"
