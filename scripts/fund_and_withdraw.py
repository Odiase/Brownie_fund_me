#third packages imports
from brownie import accounts, FundMe, config

# local imports
from .extras import get_account


def fund():
    # getting contract and account
    fund_me = FundMe[-1]
    account = get_account()

    print(fund_me)

def main():
    fund()