from brownie import accounts, config, network

def get_account():
    '''Getting Account To Work With.'''

    if network.show_active() == "development":
        return accounts[0]
        # getting my connected blockchain network
    return accounts.add(config['wallets']['private_key'])