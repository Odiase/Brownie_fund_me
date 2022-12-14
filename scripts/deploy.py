# third packages import
from brownie import accounts, config, FundMe, MockV3Aggregator, network
from web3 import Web3

# local imports
from .extras import get_account, deploy_mocks


def deploy_fund_me():
    account = get_account()
    publish_source = config['networks'][network.show_active()].get('verify')
    price_feed_address = deploy_mocks()

    # deploying fund me contract
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=publish_source
    )


def main():
    deploy_fund_me()
