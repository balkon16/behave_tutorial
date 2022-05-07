import collections


class Transaction:

    def __init__(self, id: int, name: str, status: str):
        self.id = id
        self.name = name
        self.status = status

    def __hash__(self) -> int:
        return self.id


class TransactionSet:
    def __init__(self):
        self.transactions = set()

    def add_transaction(self, transaction: Transaction):
        self.transactions.add(transaction)

    def get_summary_by_status(self):
        summary_by_status = collections.defaultdict(int)
        for transaction in self.transactions:
            summary_by_status[transaction.status] += 1
        return summary_by_status
