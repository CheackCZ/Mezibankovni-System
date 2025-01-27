from sqlalchemy import Column, Float, Integer
from sqlalchemy import CheckConstraint
from base import Base

class Account(Base):

    __tablename__ = 'account'

    account_number = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, nullable=False, default=0.0)

    __table_args__ = {
        CheckConstraint('balance >= 0', name='check_balance_is_positive'),
        CheckConstraint('account_number > 10000 and account_number < 99999', name='check_account_number_is_valid')
    }

    def __repr__(self):
        return f'Account [{self.account_number}]: {self.balance} CZK'