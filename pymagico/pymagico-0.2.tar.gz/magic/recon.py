from ctypes import c_char_p, c_void_p, c_size_t
from ctypes import c_int, c_int32, c_uint, c_float

from .lib import lib

magic_recon_header_print = lib.magic_recon_header_print
magic_recon_header_print.argtypes = [c_void_p]

magic_recon_get_frame_size = lib.magic_recon_get_frame_size
magic_recon_get_frame_size.argtypes = [c_size_t]
magic_recon_get_frame_size.restype = c_size_t

magic_recon_get_frame = lib.magic_recon_get_frame
magic_recon_get_frame.argtypes = [c_void_p]
magic_recon_get_frame.restype = c_void_p

# output
magic_recon_output_new = lib.magic_recon_output_new
magic_recon_output_new.restype = c_void_p

magic_recon_output_create = lib.magic_recon_output_create
magic_recon_output_create.argtypes = [c_void_p]
magic_recon_output_create.restype = c_void_p

magic_recon_output_delete = lib.magic_recon_output_delete
magic_recon_output_delete.argtypes = [c_void_p]

magic_recon_output_print = lib.magic_recon_output_print
magic_recon_output_print.argtypes = [c_void_p]

magic_recon_output_add_object = lib.magic_recon_output_add_object
magic_recon_output_add_object.argtypes = [c_void_p, c_int, c_char_p, c_float]

magic_recon_output_send = lib.magic_recon_output_send
magic_recon_output_send.argtypes = [c_void_p, c_void_p, c_void_p, c_int32, c_void_p]
magic_recon_output_send.restype = c_uint
