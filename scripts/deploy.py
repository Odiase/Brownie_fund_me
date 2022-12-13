# third packages import
from brownie import accounts, config, FundMe

# local imports
from .extras import get_account


def deploy_fund_me():
    account = get_account()
    
    #deploy contract
    fund_me = FundMe.deploy({"from" : account}, publish_source=True)
    print("Fund me : ", fund_me)


def main():
    deploy_fund_me()