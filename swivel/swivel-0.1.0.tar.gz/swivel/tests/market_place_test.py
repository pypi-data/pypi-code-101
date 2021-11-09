import pytest
from swivel.helpers import call, transact

@pytest.fixture(scope='module')
def swivel_address():
    return '0x8e7bFA3106c0544b6468833c0EB41c350b50A5CA'

@pytest.fixture(scope='module')
def underlying(market_place):
    return market_place.vendor.instance.toChecksumAddress('0x5592ec0cfb4dbc12d3ab100b257153436a1f0fea')

@pytest.fixture(scope='module')
def maturity():
    return 1633988168

@pytest.fixture(scope='module')
def c_token(market_place):
    return market_place.vendor.instance.toChecksumAddress('0x6d7f0754ffeb405d23c51ce938289d4835be3b14')

def test_m_place_admin(market_place):
    addr = call(market_place.admin())
    assert addr == market_place.vendor.account

def test_swivel(market_place, swivel_address):
    #set it first...
    tx_hash = transact(market_place.set_swivel_address(swivel_address))
    tx_rcpt = market_place.vendor.instance.eth.wait_for_transaction_receipt(tx_hash)
    assert tx_rcpt != None

    addr = call(market_place.swivel())
    assert addr == swivel_address

# NOTE this test is not transact mocked as it has no other dependencies, tho we _could_ mock it out... we'll leave it for now.
def test_create_get_market(market_place, underlying, maturity, c_token):
    name = 'token'
    sym = 'tkn'
    dig = 18
    tx_hash = transact(market_place.create_market(underlying, maturity, c_token, name, sym, dig))
    tx_rcpt = market_place.vendor.instance.eth.wait_for_transaction_receipt(tx_hash)
    # should be able to retrieve the market now
    mkt = call(market_place.markets(underlying, maturity))
    # will return as a list len(3)
    assert mkt[0] == c_token

def test_c_token_addr(market_place, underlying, maturity, c_token):
    ctkn = call(market_place.c_token_address(underlying, maturity))
    assert ctkn == c_token

def test_mature_market(market_place, underlying, maturity):
    txable, opts = market_place.mature_market(underlying, maturity, { 'gas': 100000 })

    assert callable(txable)
    assert isinstance(opts, dict)

def test_mature(market_place, underlying, maturity):
    matured = call(market_place.mature(underlying, maturity))
    assert matured == False

def test_maturity_rate(market_place, underlying, maturity):
    rate = call(market_place.maturity_rate(underlying, maturity))
    assert rate == 0

def test_transfer_vault_notional(market_place, underlying, maturity):
    txable, opts = market_place.transfer_vault_notional(underlying, maturity, '0x50MeDud3', 1000, { 'gas': 200000 })

    assert callable(txable)
    assert isinstance(opts, dict)
