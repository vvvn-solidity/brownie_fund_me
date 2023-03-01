from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import accounts, network, exceptions
import pytest


def test_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entance_fee

    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing!!")
    fun_me = deploy_fund_me()
    bad_actor = accounts.add()  # this will give us a blank random account
    with pytest.raises(exceptions.VirtualMachineError):
        fun_me.withdraw({"from": bad_actor})
