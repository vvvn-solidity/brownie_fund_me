from brownie import FunMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FunMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})
    print("Fund!!")


def withdraw():
    fund_me = FunMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    # withdraw()
