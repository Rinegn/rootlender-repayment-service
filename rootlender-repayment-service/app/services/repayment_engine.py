from decimal import Decimal

class RepaymentEngine:

    @staticmethod
    def validate_payment(amount_due: Decimal, amount_paid: Decimal):
        if amount_paid <= 0:
            raise ValueError("Payment amount must be greater than zero")
        if amount_paid > amount_due:
            raise ValueError("Overpayments are not allowed")
