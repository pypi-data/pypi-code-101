from ctypes import c_char_p, c_void_p
from ctypes import c_int, c_int32, c_uint, c_uint32, c_uint64, c_float

from .lib import lib

# data
magic_actions_data_get_store = lib.magic_actions_data_get_store
magic_actions_data_get_store.argtypes = [c_void_p]
magic_actions_data_get_store.restype = c_char_p

magic_actions_data_get_stream = lib.magic_actions_data_get_stream
magic_actions_data_get_stream.argtypes = [c_void_p]
magic_actions_data_get_stream.restype = c_uint32

magic_actions_data_get_frame = lib.magic_actions_data_get_frame
magic_actions_data_get_frame.argtypes = [c_void_p]
magic_actions_data_get_frame.restype = c_uint64

magic_actions_data_get_width = lib.magic_actions_data_get_width
magic_actions_data_get_width.argtypes = [c_void_p]
magic_actions_data_get_width.restype = c_int

magic_actions_data_get_height = lib.magic_actions_data_get_height
magic_actions_data_get_height.argtypes = [c_void_p]
magic_actions_data_get_height.restype = c_int

magic_actions_data_get_human = lib.magic_actions_data_get_human
magic_actions_data_get_human.argtypes = [c_void_p]
magic_actions_data_get_human.restype = c_uint

magic_actions_data_get_keypoints = lib.magic_actions_data_get_keypoints
magic_actions_data_get_keypoints.argtypes = [c_void_p]
magic_actions_data_get_keypoints.restype = c_char_p

magic_actions_data_print = lib.magic_actions_data_print
magic_actions_data_print.argtypes = [c_void_p]

# output
magic_actions_output_print = lib.magic_actions_output_print
magic_actions_output_print.argtypes = [c_void_p]

magic_actions_output_send = lib.magic_actions_output_send
magic_actions_output_send.argtypes = [c_void_p, c_void_p, c_void_p, c_int32, c_void_p, c_float]
magic_actions_output_send.restype = c_char_p
