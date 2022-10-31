#!/usr/bin/python3
import brownie
from web3.constants import ADDRESS_ZERO


def test_should_successfully_burn(accounts, token):
    total_supply = token.totalSupply()
    balance = token.balanceOf(accounts[0])
    amount = balance // 4

    # burn the tokens
    tx = token.burn(accounts[0], amount)

    # success
    assert tx.return_value is True

    # emits a transfer event with to set to the zero address
    assert len(tx.events) == 1
    assert tx.events["Transfer"].values() == [accounts[0], 0, amount]

    # the total supply has gone down
    assert token.totalSupply() == total_supply - amount

    # as has the balance of the burning address
    assert token.balanceOf(accounts[0]) == balance - amount


def test_should_fail_burn_insufficient_balance(accounts, token):
    balance = token.balanceOf(accounts[0])

    # should revert insufficient balance
    with brownie.reverts():
        token.burn(accounts[0], balance + 1)


def test_should_fail_burn_zero_address(token):
    # should revert cannot be the zero address
    with brownie.reverts():
        token.burn(ADDRESS_ZERO, 1)
