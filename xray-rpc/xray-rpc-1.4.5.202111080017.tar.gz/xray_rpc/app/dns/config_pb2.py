# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/dns/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_rpc.common.net import address_pb2 as common_dot_net_dot_address__pb2
from xray_rpc.common.net import destination_pb2 as common_dot_net_dot_destination__pb2
from xray_rpc.app.router import config_pb2 as app_dot_router_dot_config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/dns/config.proto',
  package='xray.app.dns',
  syntax='proto3',
  serialized_options=b'\n\020com.xray.app.dnsP\001Z!github.com/xtls/xray-core/app/dns\252\002\014Xray.App.Dns',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x61pp/dns/config.proto\x12\x0cxray.app.dns\x1a\x18\x63ommon/net/address.proto\x1a\x1c\x63ommon/net/destination.proto\x1a\x17\x61pp/router/config.proto\"\xe1\x02\n\nNameServer\x12*\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x19.xray.common.net.Endpoint\x12\x43\n\x12prioritized_domain\x18\x02 \x03(\x0b\x32\'.xray.app.dns.NameServer.PriorityDomain\x12%\n\x05geoip\x18\x03 \x03(\x0b\x32\x16.xray.app.router.GeoIP\x12=\n\x0eoriginal_rules\x18\x04 \x03(\x0b\x32%.xray.app.dns.NameServer.OriginalRule\x1aP\n\x0ePriorityDomain\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .xray.app.dns.DomainMatchingType\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x1a*\n\x0cOriginalRule\x12\x0c\n\x04rule\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\r\"\xbb\x03\n\x06\x43onfig\x12\x32\n\x0bNameServers\x18\x01 \x03(\x0b\x32\x19.xray.common.net.EndpointB\x02\x18\x01\x12-\n\x0bname_server\x18\x05 \x03(\x0b\x32\x18.xray.app.dns.NameServer\x12\x32\n\x05Hosts\x18\x02 \x03(\x0b\x32\x1f.xray.app.dns.Config.HostsEntryB\x02\x18\x01\x12\x11\n\tclient_ip\x18\x03 \x01(\x0c\x12\x36\n\x0cstatic_hosts\x18\x04 \x03(\x0b\x32 .xray.app.dns.Config.HostMapping\x12\x0b\n\x03tag\x18\x06 \x01(\t\x1aI\n\nHostsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain:\x02\x38\x01\x1aq\n\x0bHostMapping\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .xray.app.dns.DomainMatchingType\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\n\n\x02ip\x18\x03 \x03(\x0c\x12\x16\n\x0eproxied_domain\x18\x04 \x01(\tJ\x04\x08\x07\x10\x08*E\n\x12\x44omainMatchingType\x12\x08\n\x04\x46ull\x10\x00\x12\r\n\tSubdomain\x10\x01\x12\x0b\n\x07Keyword\x10\x02\x12\t\n\x05Regex\x10\x03\x42\x46\n\x10\x63om.xray.app.dnsP\x01Z!github.com/xtls/xray-core/app/dns\xaa\x02\x0cXray.App.Dnsb\x06proto3'
  ,
  dependencies=[common_dot_net_dot_address__pb2.DESCRIPTOR,common_dot_net_dot_destination__pb2.DESCRIPTOR,app_dot_router_dot_config__pb2.DESCRIPTOR,])

_DOMAINMATCHINGTYPE = _descriptor.EnumDescriptor(
  name='DomainMatchingType',
  full_name='xray.app.dns.DomainMatchingType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Full', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Subdomain', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Keyword', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Regex', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=921,
  serialized_end=990,
)
_sym_db.RegisterEnumDescriptor(_DOMAINMATCHINGTYPE)

DomainMatchingType = enum_type_wrapper.EnumTypeWrapper(_DOMAINMATCHINGTYPE)
Full = 0
Subdomain = 1
Keyword = 2
Regex = 3



_NAMESERVER_PRIORITYDOMAIN = _descriptor.Descriptor(
  name='PriorityDomain',
  full_name='xray.app.dns.NameServer.PriorityDomain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='xray.app.dns.NameServer.PriorityDomain.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain', full_name='xray.app.dns.NameServer.PriorityDomain.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=349,
  serialized_end=429,
)

_NAMESERVER_ORIGINALRULE = _descriptor.Descriptor(
  name='OriginalRule',
  full_name='xray.app.dns.NameServer.OriginalRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rule', full_name='xray.app.dns.NameServer.OriginalRule.rule', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='xray.app.dns.NameServer.OriginalRule.size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=431,
  serialized_end=473,
)

_NAMESERVER = _descriptor.Descriptor(
  name='NameServer',
  full_name='xray.app.dns.NameServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='xray.app.dns.NameServer.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prioritized_domain', full_name='xray.app.dns.NameServer.prioritized_domain', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geoip', full_name='xray.app.dns.NameServer.geoip', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='original_rules', full_name='xray.app.dns.NameServer.original_rules', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NAMESERVER_PRIORITYDOMAIN, _NAMESERVER_ORIGINALRULE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=473,
)


_CONFIG_HOSTSENTRY = _descriptor.Descriptor(
  name='HostsEntry',
  full_name='xray.app.dns.Config.HostsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='xray.app.dns.Config.HostsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='xray.app.dns.Config.HostsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=725,
  serialized_end=798,
)

_CONFIG_HOSTMAPPING = _descriptor.Descriptor(
  name='HostMapping',
  full_name='xray.app.dns.Config.HostMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='xray.app.dns.Config.HostMapping.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain', full_name='xray.app.dns.Config.HostMapping.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='xray.app.dns.Config.HostMapping.ip', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proxied_domain', full_name='xray.app.dns.Config.HostMapping.proxied_domain', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=800,
  serialized_end=913,
)

_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='xray.app.dns.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='NameServers', full_name='xray.app.dns.Config.NameServers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name_server', full_name='xray.app.dns.Config.name_server', index=1,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Hosts', full_name='xray.app.dns.Config.Hosts', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_ip', full_name='xray.app.dns.Config.client_ip', index=3,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='static_hosts', full_name='xray.app.dns.Config.static_hosts', index=4,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tag', full_name='xray.app.dns.Config.tag', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CONFIG_HOSTSENTRY, _CONFIG_HOSTMAPPING, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=919,
)

_NAMESERVER_PRIORITYDOMAIN.fields_by_name['type'].enum_type = _DOMAINMATCHINGTYPE
_NAMESERVER_PRIORITYDOMAIN.containing_type = _NAMESERVER
_NAMESERVER_ORIGINALRULE.containing_type = _NAMESERVER
_NAMESERVER.fields_by_name['address'].message_type = common_dot_net_dot_destination__pb2._ENDPOINT
_NAMESERVER.fields_by_name['prioritized_domain'].message_type = _NAMESERVER_PRIORITYDOMAIN
_NAMESERVER.fields_by_name['geoip'].message_type = app_dot_router_dot_config__pb2._GEOIP
_NAMESERVER.fields_by_name['original_rules'].message_type = _NAMESERVER_ORIGINALRULE
_CONFIG_HOSTSENTRY.fields_by_name['value'].message_type = common_dot_net_dot_address__pb2._IPORDOMAIN
_CONFIG_HOSTSENTRY.containing_type = _CONFIG
_CONFIG_HOSTMAPPING.fields_by_name['type'].enum_type = _DOMAINMATCHINGTYPE
_CONFIG_HOSTMAPPING.containing_type = _CONFIG
_CONFIG.fields_by_name['NameServers'].message_type = common_dot_net_dot_destination__pb2._ENDPOINT
_CONFIG.fields_by_name['name_server'].message_type = _NAMESERVER
_CONFIG.fields_by_name['Hosts'].message_type = _CONFIG_HOSTSENTRY
_CONFIG.fields_by_name['static_hosts'].message_type = _CONFIG_HOSTMAPPING
DESCRIPTOR.message_types_by_name['NameServer'] = _NAMESERVER
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.enum_types_by_name['DomainMatchingType'] = _DOMAINMATCHINGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NameServer = _reflection.GeneratedProtocolMessageType('NameServer', (_message.Message,), {

  'PriorityDomain' : _reflection.GeneratedProtocolMessageType('PriorityDomain', (_message.Message,), {
    'DESCRIPTOR' : _NAMESERVER_PRIORITYDOMAIN,
    '__module__' : 'app.dns.config_pb2'
    # @@protoc_insertion_point(class_scope:xray.app.dns.NameServer.PriorityDomain)
    })
  ,

  'OriginalRule' : _reflection.GeneratedProtocolMessageType('OriginalRule', (_message.Message,), {
    'DESCRIPTOR' : _NAMESERVER_ORIGINALRULE,
    '__module__' : 'app.dns.config_pb2'
    # @@protoc_insertion_point(class_scope:xray.app.dns.NameServer.OriginalRule)
    })
  ,
  'DESCRIPTOR' : _NAMESERVER,
  '__module__' : 'app.dns.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.dns.NameServer)
  })
_sym_db.RegisterMessage(NameServer)
_sym_db.RegisterMessage(NameServer.PriorityDomain)
_sym_db.RegisterMessage(NameServer.OriginalRule)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {

  'HostsEntry' : _reflection.GeneratedProtocolMessageType('HostsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_HOSTSENTRY,
    '__module__' : 'app.dns.config_pb2'
    # @@protoc_insertion_point(class_scope:xray.app.dns.Config.HostsEntry)
    })
  ,

  'HostMapping' : _reflection.GeneratedProtocolMessageType('HostMapping', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_HOSTMAPPING,
    '__module__' : 'app.dns.config_pb2'
    # @@protoc_insertion_point(class_scope:xray.app.dns.Config.HostMapping)
    })
  ,
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'app.dns.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.dns.Config)
  })
_sym_db.RegisterMessage(Config)
_sym_db.RegisterMessage(Config.HostsEntry)
_sym_db.RegisterMessage(Config.HostMapping)


DESCRIPTOR._options = None
_CONFIG_HOSTSENTRY._options = None
_CONFIG.fields_by_name['NameServers']._options = None
_CONFIG.fields_by_name['Hosts']._options = None
# @@protoc_insertion_point(module_scope)
