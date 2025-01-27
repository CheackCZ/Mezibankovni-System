from sqlalchemy import Column, Float, Integer
from base import Base

class Account(Base):

    __tablename__ = 'account'

    account_number = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, nullable=False, default=0.0)

    def __repr__(self):
        return f'Account [{self.account_number}]: {self.balance} CZK'