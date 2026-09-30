from ..interface.processable import Processable
from ..interface.refundable import Refundable
from ..interface.validatable import Validatable

class Cash(Processable, Validatable):
    def process(self):
        return "Cash is processing"

    def validate(self):
        return "Validating cash"
