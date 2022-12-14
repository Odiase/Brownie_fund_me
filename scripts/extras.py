# third packages imports
from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3


def get_account():
    '''Getting Account To Work With.'''

    if network.show_active() == "development":
        return accounts[0]
        # getting my connected blockchain network
    return accounts.add(config['wallets']['private_key'])


def deploy_mocks():
    account = get_account()
    # if we are on a persistent network(goerli...etc), use associated price_feed address,
    #  else use mocks
    if network.show_active() != "development":
        price_feed_address = config['networks'][network.show_active(
        )]['eth_usd_price_feed']
    else:
        if len(MockV3Aggregator) <= 0:
            mock_aggregator = MockV3Aggregator.deploy(
                18, Web3.toWei(2000, 'ether'), 
                {"from": account}
            )
        
    price_feed_address = MockV3Aggregator[-1].address

    return price_feed_address