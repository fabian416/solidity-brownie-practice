from brownie import accounts, SimpleStorage, network, config

def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account}) # always specify from which account 
    
    stored_value = simple_storage.retrieve() # does not make any changes in the blockchain
    print(stored_value)
    
    transaction = simple_storage.store(42, {"from": account}) # you have to put from again cause now is making changes in the blockchain
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)
    


def get_account():
    if network.show_active() == "development":
        return accounts.add(config["wallets"]["from_key"])
    else:
        return accounts.load("first-account")
    
def main():
    deploy_simple_storage()
    