from ooc.counter import Player, Gate, PLAYER_DEFAULTS
from ooc.config import Config
import pytest

def test_init_counter_with_invalid_file():
    gates = [Gate((350, 320), 50, 115)]
    with pytest.raises(ValueError):
        Player('some_path_to/invalid_video.mp4', gates=gates)

def test_init_counter_with_valid_file():
    gates = [Gate((350, 320), 50, 115)]
    Player('C:\\Users\\Blair\\Videos\\object-counting-videos\\Traffic_Laramie_1.mp4', gates=gates)
    assert True

def test_arguments_direct_set():
    options = {
        'gates': [Gate((350, 320), 50, 115)],
        'ksize': (31, 31),
        'sigma_x': 1,
        'show': False,
        'debug': True
    }
    
    player = Player('C:\\Users\\Blair\\Videos\\object-counting-videos\\Traffic_Laramie_1.mp4',
        gates=options['gates'], ksize=options['ksize'], show=options['show'],
        debug=options['debug'])
    
    if (player.gates == options['gates'] and
        player.ksize == options['ksize'] and
        player.sigma_x == options['sigma_x'] and
        player.show == options['show'] and
        player.debug == options['debug']):
        assert True

def test_arguments_default():
    player = Player('C:\\Users\\Blair\\Videos\\object-counting-videos\\Traffic_Laramie_1.mp4')
    
    if (player.gates == PLAYER_DEFAULTS['gates'] and
        player.ksize == PLAYER_DEFAULTS['ksize'] and
        player.sigma_x == PLAYER_DEFAULTS['sigma_x'] and
        player.show == PLAYER_DEFAULTS['show'] and
        player.debug == PLAYER_DEFAULTS['debug']):
        assert True

# def test_arguments_config():
#     config = Config()
#     player = Player('C:\\Users\\Blair\\Videos\\object-counting-videos\\Traffic_Laramie_1.mp4',
#         config = config)
    
#     if (player.gates == config['gates'] and 
#         player.ksize == config['blur']['ksize'] and
#         player.sigma_x == config['blur']['sigma_x'] and
#         player.show == config['show'] and
#         player.debug == config['debug']):
#         assert True

def test_counter_start():
    gates = [Gate((350, 320), 50, 115)]
    player = Player('C:\\Users\\Blair\\Videos\\object-counting-videos\\Traffic_Laramie_1.mp4', gates=gates)
    player.start()
    assert True