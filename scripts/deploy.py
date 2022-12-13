# third packages import
from brownie import accounts, config, FundMe, MockV3Aggregator, network

# local imports
from .extras import get_account


def deploy_fund_me():
    account = get_account()

    # if we are on a persistent network(goerli...etc), use associated price_feed address,
    #  else use mocks
    if network.show_active() != "development":
        price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
    else:
        mock_aggregator = MockV3Aggregator.deploy(18, 2000000000000000000000, {"from" : account})
        price_feed_address = mock_aggregator.address
        publish_source = False
    
    # deploying fund me contract
    publish_source = config['networks'][network.show_active()].get('verify')
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account}, 
        publish_source=publish_source
    )
    print("Fund me : ", fund_me)


def main():
    deploy_fund_me()
