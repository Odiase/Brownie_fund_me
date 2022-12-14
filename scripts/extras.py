# third packages imports
from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3


DECIMALS = 18
STARTING_PRICE = 2000
LOCAL_BLOCKCHIAN_ENVIRONMENTS = ["development", "ganache-local"]

def get_account():
    '''Getting Account To Work With.'''

    if network.show_active() in LOCAL_BLOCKCHIAN_ENVIRONMENTS:
        return accounts[0]
        # getting my connected blockchain network
    return accounts.add(config['wallets']['private_key'])


def deploy_mocks():
    account = get_account()
    # if we are on a persistent network(goerli...etc), use associated price_feed address,
    #  else use mocks
    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, 'ether'), 
            {"from": account}
        )
        
    price_feed_address = MockV3Aggregator[-1].address

    return price_feed_address