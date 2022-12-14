# third packages import
from brownie import accounts, config, FundMe, MockV3Aggregator, network
from web3 import Web3

# local imports
from .extras import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config['networks'][network.show_active(
        )]['eth_usd_price_feed']
        publish_source = config['networks'][network.show_active()].get('verify')
    else:
        price_feed_address = deploy_mocks()
        publish_source = False

    # deploying fund me contract
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=publish_source
    )


def main():
    deploy_fund_me()
