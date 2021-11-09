import pytest
from swivel.helpers import call

@pytest.fixture(scope='module')
def key(vendor):
    return vendor.instance.toBytes(hexstr='0xfb28b03032bbb105e1199e496b23a6435a077375cbea9c6c4998b971a672873c')

@pytest.fixture(scope='module')
def orders(key):
    # we can use the same order 2x here for the purpose of this test...
    order = {
        'key': key,
        'maker': '0x7111F9Aeb2C1b9344EC274780dc9e3806bdc60Ef',
        'underlying': '0x5592EC0cfb4dbc12D3aB100b257153436a1f0FEa',
        'vault': False,
        'exit': False,
        'principal': 1000,
        'premium': 60,
        'maturity': 1655255622,
        'expiry': 1625173101,
    }

    return (order, order)

@pytest.fixture(scope='module')
def signatures(vendor):
    # again, just using same thing 2x
    sig = '06aa9b426a48ff92d3b940eea498ba8bf9cf4e3e05987bdf4c68c66382385f5e59dd5f013c2b13eb7958234ad441c53675b196d88d143eccf93192b5b9758d571b'
    return (sig, sig)

@pytest.fixture(scope='module')
def amounts():
    return (1000, 500)

def test_name(swivel):
    name = call(swivel.NAME())
    assert name == 'Swivel Finance'

def test_version(swivel):
    verz = call(swivel.VERSION())
    assert verz == '2.0.0'

def test_hold(swivel):
    hold = call(swivel.HOLD())
    assert hold == 259200

def test_domain(swivel):
    dom = call(swivel.domain())
    assert dom != None

def test_market_place_address(market_place, swivel):
    m_place_addr = call(swivel.market_place())
    assert m_place_addr == market_place.address

def test_swivel_admin(swivel):
    addr = call(swivel.admin())
    assert addr == swivel.vendor.account

def test_fenominator(swivel):
    fee1 = call(swivel.fenominator(0))
    assert fee1 == 200
    fee2 = call(swivel.fenominator(1))
    assert fee2 == 600
    fee3 = call(swivel.fenominator(2))
    assert fee3 == 400
    fee4 = call(swivel.fenominator(3))
    assert fee4 == 200

def test_initiate(swivel, orders, amounts, signatures):
    txable, opts = swivel.initiate(orders, amounts, signatures, { 'gas': 1000000 })

    # if the call encoded correctly we'll get back a callable and a dict
    assert callable(txable)
    assert isinstance(opts, dict)

def test_exit(swivel, orders, amounts, signatures):
    txable, opts = swivel.exit(orders, amounts, signatures, { 'gas': 250000 })

    assert callable(txable)
    assert isinstance(opts, dict)

def test_cancel(swivel, orders, signatures):
    txable, opts = swivel.cancel(orders[0], signatures[0], opts={ 'gas': 50000 })

    assert callable(txable)
    assert isinstance(opts, dict)

def test_split_underlying(swivel):
    txable, opts = swivel.split_underlying('0x5592ec0cfb4dbc12d3ab100b257153436a1f0fea',
        1234567890, 1000, opts={ 'gas': 17000 })

    assert callable(txable)
    assert isinstance(opts, dict)

def test_combine_tokens(swivel):
    txable, opts = swivel.combine_tokens('0x5592ec0cfb4dbc12d3ab100b257153436a1f0fea', 1234567890, 500, { 'gas': 1000 })

    assert callable(txable)
    assert isinstance(opts, dict)

def test_redeem_zctoken(swivel):
    txable, opts = swivel.redeem_zc_token('0x5592ec0cfb4dbc12d3ab100b257153436a1f0fea', 1234567890, 700, { 'gas': 2000 })

    assert callable(txable)
    assert isinstance(opts, dict)

def test_redeem_vault_interest(swivel):
    txable, opts = swivel.redeem_vault_interest('0x5592ec0cfb4dbc12d3ab100b257153436a1f0fea', 1234567899, { 'gas': 2500 })

    assert callable(txable)
    assert isinstance(opts, dict)
