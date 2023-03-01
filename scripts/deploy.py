from brownie import FunMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    mocks_deploy,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contract
    # if we are on a persistent nerwork like goerli,use the assciated address
    # otherwise,deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        mocks_deploy()
        # just use the most recently deployed MockV3Aggregator
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FunMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"contract deployed to {fund_me.address}")
    return fund_me


def main():
    print(f"111111111{network.show_active()}")
    deploy_fund_me()
