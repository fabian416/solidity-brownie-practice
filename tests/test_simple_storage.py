from brownie import SimpleStorage, accounts

def test_deploy():
    # Arrange -> organizar o arreglar
    account = accounts[0]
    
    #Act -> do something
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    
    #Assert -> check that something has gone well
    assert starting_value == expected 
    
def test_updating_storage():
    #Arrange 
    account = accounts[0]
    
    #Act
    simple_storage = SimpleStorage.deploy({"from": account })
    txn = simple_storage.store(42, {"from": account})
    txn.wait(1)
    expected = 42
    
    #Assert
    assert simple_storage.retrieve() == expected    
    
    