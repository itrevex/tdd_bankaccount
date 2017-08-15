import pytest

from wallet import Wallet, InsufficientBalance

def test_default_initial_balance():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_balance():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    wallet = Wallet(30)
    wallet.spend_cash(10)
    assert wallet.balance == 20

def test_wallet_spend_cash_raises_insufficient_balance_exception():
    wallet = Wallet()
    with pytest.raises(InsufficientBalance):
        wallet.spend_cash(100)
