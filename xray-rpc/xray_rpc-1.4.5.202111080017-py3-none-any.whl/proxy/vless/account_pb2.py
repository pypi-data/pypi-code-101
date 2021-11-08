# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/vless/account.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy/vless/account.proto',
  package='xray.proxy.vless',
  syntax='proto3',
  serialized_options=b'\n\024com.xray.proxy.vlessP\001Z%github.com/xtls/xray-core/proxy/vless\252\002\020Xray.Proxy.Vless',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19proxy/vless/account.proto\x12\x10xray.proxy.vless\"7\n\x07\x41\x63\x63ount\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x66low\x18\x02 \x01(\t\x12\x12\n\nencryption\x18\x03 \x01(\tBR\n\x14\x63om.xray.proxy.vlessP\x01Z%github.com/xtls/xray-core/proxy/vless\xaa\x02\x10Xray.Proxy.Vlessb\x06proto3'
)




_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='xray.proxy.vless.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='xray.proxy.vless.Account.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flow', full_name='xray.proxy.vless.Account.flow', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='encryption', full_name='xray.proxy.vless.Account.encryption', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'proxy.vless.account_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.vless.Account)
  })
_sym_db.RegisterMessage(Account)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
