# third packages import
from brownie import accounts, config, FundMe

# local imports
from .extras import get_account


def deploy_fund_me():
    account = get_account()
    pass


def main():
    deploy_fund_me()