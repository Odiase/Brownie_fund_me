#third packages imports
from brownie import accounts, FundMe, config

# local imports
from .extras import get_account


def fund():
    # getting contract and account
    fund_me = FundMe[-1]
    account = get_account()

    entrance_fee = fund_me.get_entrance_fee()
    fund_me.fund({"from" : account, "value" : entrance_fee})
    print("Funded with ", entrance_fee)

def withdraw():
    fund_me = FundMe[-1]
    account = accounts[0]

    fund_me.withdraw({"from" : account})
    print("Funds Withdrawn...")

def main():
    fund()
    withdraw()