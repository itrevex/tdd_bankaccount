import pytest

from wallet import Wallet, InsufficientBalance

@pytest.fixture
def empty_wallet():
    return Wallet()

@pytest.fixture
def wallet():
    return Wallet(50)

def test_default_initial_balance(empty_wallet):
        assert empty_wallet.balance == 0

def test_setting_initial_balance(wallet):
    assert wallet.balance == 50

def test_wallet_add_cash(empty_wallet):
    empty_wallet.add_cash(40)
    assert empty_wallet.balance == 40

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 40

def test_wallet_spend_cash_raises_insufficient_balance_exception(empty_wallet):
    with pytest.raises(InsufficientBalance):
        empty_wallet.spend_cash(100)
