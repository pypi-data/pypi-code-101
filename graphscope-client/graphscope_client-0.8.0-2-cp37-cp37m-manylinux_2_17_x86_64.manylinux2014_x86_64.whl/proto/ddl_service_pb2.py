# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/ddl_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import graph_def_pb2 as proto_dot_graph__def__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/ddl_service.proto',
  package='gs.rpc.ddl_service.v1',
  syntax='proto3',
  serialized_options=b'\n com.alibaba.graphscope.proto.ddlP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17proto/ddl_service.proto\x12\x15gs.rpc.ddl_service.v1\x1a\x15proto/graph_def.proto\"\x88\x05\n\x12\x42\x61tchSubmitRequest\x12\x16\n\x0e\x66ormat_version\x18\x01 \x01(\x05\x12\x17\n\x0fsimple_response\x18\x02 \x01(\x08\x12\x43\n\x05value\x18\x03 \x03(\x0b\x32\x34.gs.rpc.ddl_service.v1.BatchSubmitRequest.DDLRequest\x1a\xfb\x03\n\nDDLRequest\x12T\n\x1a\x63reate_vertex_type_request\x18\x01 \x01(\x0b\x32..gs.rpc.ddl_service.v1.CreateVertexTypeRequestH\x00\x12P\n\x18\x63reate_edge_type_request\x18\x02 \x01(\x0b\x32,.gs.rpc.ddl_service.v1.CreateEdgeTypeRequestH\x00\x12J\n\x15\x61\x64\x64_edge_kind_request\x18\x03 \x01(\x0b\x32).gs.rpc.ddl_service.v1.AddEdgeKindRequestH\x00\x12P\n\x18remove_edge_kind_request\x18\x04 \x01(\x0b\x32,.gs.rpc.ddl_service.v1.RemoveEdgeKindRequestH\x00\x12P\n\x18\x64rop_vertex_type_request\x18\x05 \x01(\x0b\x32,.gs.rpc.ddl_service.v1.DropVertexTypeRequestH\x00\x12L\n\x16\x64rop_edge_type_request\x18\x06 \x01(\x0b\x32*.gs.rpc.ddl_service.v1.DropEdgeTypeRequestH\x00\x42\x07\n\x05value\"Z\n\x13\x42\x61tchSubmitResponse\x12\x16\n\x0e\x66ormat_version\x18\x01 \x01(\x05\x12+\n\tgraph_def\x18\x02 \x01(\x0b\x32\x18.gs.rpc.graph.GraphDefPb\"D\n\x17\x43reateVertexTypeRequest\x12)\n\x08type_def\x18\x01 \x01(\x0b\x32\x17.gs.rpc.graph.TypeDefPb\"B\n\x15\x43reateEdgeTypeRequest\x12)\n\x08type_def\x18\x01 \x01(\x0b\x32\x17.gs.rpc.graph.TypeDefPb\"\\\n\x12\x41\x64\x64\x45\x64geKindRequest\x12\x12\n\nedge_label\x18\x01 \x01(\t\x12\x18\n\x10src_vertex_label\x18\x02 \x01(\t\x12\x18\n\x10\x64st_vertex_label\x18\x03 \x01(\t\"_\n\x15RemoveEdgeKindRequest\x12\x12\n\nedge_label\x18\x01 \x01(\t\x12\x18\n\x10src_vertex_label\x18\x02 \x01(\t\x12\x18\n\x10\x64st_vertex_label\x18\x03 \x01(\t\"&\n\x15\x44ropVertexTypeRequest\x12\r\n\x05label\x18\x01 \x01(\t\"$\n\x13\x44ropEdgeTypeRequest\x12\r\n\x05label\x18\x01 \x01(\t\"!\n\x12GetGraphDefRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"B\n\x13GetGraphDefResponse\x12+\n\tgraph_def\x18\x01 \x01(\x0b\x32\x18.gs.rpc.graph.GraphDefPb2\xd7\x01\n\tClientDdl\x12\x64\n\x0b\x62\x61tchSubmit\x12).gs.rpc.ddl_service.v1.BatchSubmitRequest\x1a*.gs.rpc.ddl_service.v1.BatchSubmitResponse\x12\x64\n\x0bgetGraphDef\x12).gs.rpc.ddl_service.v1.GetGraphDefRequest\x1a*.gs.rpc.ddl_service.v1.GetGraphDefResponseB$\n com.alibaba.graphscope.proto.ddlP\x01\x62\x06proto3'
  ,
  dependencies=[proto_dot_graph__def__pb2.DESCRIPTOR,])




_BATCHSUBMITREQUEST_DDLREQUEST = _descriptor.Descriptor(
  name='DDLRequest',
  full_name='gs.rpc.ddl_service.v1.BatchSubmitRequest.DDLRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='create_vertex_type_request', full_name='gs.rpc.ddl_service.v1.BatchSubmitRequest.DDLRequest.create_vertex_type_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_edge_type_request', full_name='gs.rpc.ddl_service.v1.BatchSubmitRequest.DDLRequest.create_edge_type_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='add_edge_kind_request', full_name='gs.rpc.ddl_service.v1.BatchSubmitRequest.DDLRequest.add_edge_kind_request', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remove_edge_kind_request', full_name='gs.rpc.ddl_service.v1.BatchSubmitRequest.DDLRequest.remove_edge_kind_request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drop_vertex_type_request', full_name='gs.rpc.ddl_service.v1.BatchSubmitRequest.DDLRequest.drop_vertex_type_request', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drop_edge_type_request', full_name='gs.rpc.ddl_service.v1.BatchSubmitRequest.DDLRequest.drop_edge_type_request', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='gs.rpc.ddl_service.v1.BatchSubmitRequest.DDLRequest.value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=215,
  serialized_end=722,
)

_BATCHSUBMITREQUEST = _descriptor.Descriptor(
  name='BatchSubmitRequest',
  full_name='gs.rpc.ddl_service.v1.BatchSubmitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='format_version', full_name='gs.rpc.ddl_service.v1.BatchSubmitRequest.format_version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='simple_response', full_name='gs.rpc.ddl_service.v1.BatchSubmitRequest.simple_response', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='gs.rpc.ddl_service.v1.BatchSubmitRequest.value', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BATCHSUBMITREQUEST_DDLREQUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=722,
)


_BATCHSUBMITRESPONSE = _descriptor.Descriptor(
  name='BatchSubmitResponse',
  full_name='gs.rpc.ddl_service.v1.BatchSubmitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='format_version', full_name='gs.rpc.ddl_service.v1.BatchSubmitResponse.format_version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='graph_def', full_name='gs.rpc.ddl_service.v1.BatchSubmitResponse.graph_def', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=724,
  serialized_end=814,
)


_CREATEVERTEXTYPEREQUEST = _descriptor.Descriptor(
  name='CreateVertexTypeRequest',
  full_name='gs.rpc.ddl_service.v1.CreateVertexTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_def', full_name='gs.rpc.ddl_service.v1.CreateVertexTypeRequest.type_def', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=816,
  serialized_end=884,
)


_CREATEEDGETYPEREQUEST = _descriptor.Descriptor(
  name='CreateEdgeTypeRequest',
  full_name='gs.rpc.ddl_service.v1.CreateEdgeTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_def', full_name='gs.rpc.ddl_service.v1.CreateEdgeTypeRequest.type_def', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=886,
  serialized_end=952,
)


_ADDEDGEKINDREQUEST = _descriptor.Descriptor(
  name='AddEdgeKindRequest',
  full_name='gs.rpc.ddl_service.v1.AddEdgeKindRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='edge_label', full_name='gs.rpc.ddl_service.v1.AddEdgeKindRequest.edge_label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='src_vertex_label', full_name='gs.rpc.ddl_service.v1.AddEdgeKindRequest.src_vertex_label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dst_vertex_label', full_name='gs.rpc.ddl_service.v1.AddEdgeKindRequest.dst_vertex_label', index=2,
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
  serialized_start=954,
  serialized_end=1046,
)


_REMOVEEDGEKINDREQUEST = _descriptor.Descriptor(
  name='RemoveEdgeKindRequest',
  full_name='gs.rpc.ddl_service.v1.RemoveEdgeKindRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='edge_label', full_name='gs.rpc.ddl_service.v1.RemoveEdgeKindRequest.edge_label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='src_vertex_label', full_name='gs.rpc.ddl_service.v1.RemoveEdgeKindRequest.src_vertex_label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dst_vertex_label', full_name='gs.rpc.ddl_service.v1.RemoveEdgeKindRequest.dst_vertex_label', index=2,
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
  serialized_start=1048,
  serialized_end=1143,
)


_DROPVERTEXTYPEREQUEST = _descriptor.Descriptor(
  name='DropVertexTypeRequest',
  full_name='gs.rpc.ddl_service.v1.DropVertexTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='gs.rpc.ddl_service.v1.DropVertexTypeRequest.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1145,
  serialized_end=1183,
)


_DROPEDGETYPEREQUEST = _descriptor.Descriptor(
  name='DropEdgeTypeRequest',
  full_name='gs.rpc.ddl_service.v1.DropEdgeTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='gs.rpc.ddl_service.v1.DropEdgeTypeRequest.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1185,
  serialized_end=1221,
)


_GETGRAPHDEFREQUEST = _descriptor.Descriptor(
  name='GetGraphDefRequest',
  full_name='gs.rpc.ddl_service.v1.GetGraphDefRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='gs.rpc.ddl_service.v1.GetGraphDefRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1223,
  serialized_end=1256,
)


_GETGRAPHDEFRESPONSE = _descriptor.Descriptor(
  name='GetGraphDefResponse',
  full_name='gs.rpc.ddl_service.v1.GetGraphDefResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='graph_def', full_name='gs.rpc.ddl_service.v1.GetGraphDefResponse.graph_def', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1258,
  serialized_end=1324,
)

_BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['create_vertex_type_request'].message_type = _CREATEVERTEXTYPEREQUEST
_BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['create_edge_type_request'].message_type = _CREATEEDGETYPEREQUEST
_BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['add_edge_kind_request'].message_type = _ADDEDGEKINDREQUEST
_BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['remove_edge_kind_request'].message_type = _REMOVEEDGEKINDREQUEST
_BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['drop_vertex_type_request'].message_type = _DROPVERTEXTYPEREQUEST
_BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['drop_edge_type_request'].message_type = _DROPEDGETYPEREQUEST
_BATCHSUBMITREQUEST_DDLREQUEST.containing_type = _BATCHSUBMITREQUEST
_BATCHSUBMITREQUEST_DDLREQUEST.oneofs_by_name['value'].fields.append(
  _BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['create_vertex_type_request'])
_BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['create_vertex_type_request'].containing_oneof = _BATCHSUBMITREQUEST_DDLREQUEST.oneofs_by_name['value']
_BATCHSUBMITREQUEST_DDLREQUEST.oneofs_by_name['value'].fields.append(
  _BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['create_edge_type_request'])
_BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['create_edge_type_request'].containing_oneof = _BATCHSUBMITREQUEST_DDLREQUEST.oneofs_by_name['value']
_BATCHSUBMITREQUEST_DDLREQUEST.oneofs_by_name['value'].fields.append(
  _BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['add_edge_kind_request'])
_BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['add_edge_kind_request'].containing_oneof = _BATCHSUBMITREQUEST_DDLREQUEST.oneofs_by_name['value']
_BATCHSUBMITREQUEST_DDLREQUEST.oneofs_by_name['value'].fields.append(
  _BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['remove_edge_kind_request'])
_BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['remove_edge_kind_request'].containing_oneof = _BATCHSUBMITREQUEST_DDLREQUEST.oneofs_by_name['value']
_BATCHSUBMITREQUEST_DDLREQUEST.oneofs_by_name['value'].fields.append(
  _BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['drop_vertex_type_request'])
_BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['drop_vertex_type_request'].containing_oneof = _BATCHSUBMITREQUEST_DDLREQUEST.oneofs_by_name['value']
_BATCHSUBMITREQUEST_DDLREQUEST.oneofs_by_name['value'].fields.append(
  _BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['drop_edge_type_request'])
_BATCHSUBMITREQUEST_DDLREQUEST.fields_by_name['drop_edge_type_request'].containing_oneof = _BATCHSUBMITREQUEST_DDLREQUEST.oneofs_by_name['value']
_BATCHSUBMITREQUEST.fields_by_name['value'].message_type = _BATCHSUBMITREQUEST_DDLREQUEST
_BATCHSUBMITRESPONSE.fields_by_name['graph_def'].message_type = proto_dot_graph__def__pb2._GRAPHDEFPB
_CREATEVERTEXTYPEREQUEST.fields_by_name['type_def'].message_type = proto_dot_graph__def__pb2._TYPEDEFPB
_CREATEEDGETYPEREQUEST.fields_by_name['type_def'].message_type = proto_dot_graph__def__pb2._TYPEDEFPB
_GETGRAPHDEFRESPONSE.fields_by_name['graph_def'].message_type = proto_dot_graph__def__pb2._GRAPHDEFPB
DESCRIPTOR.message_types_by_name['BatchSubmitRequest'] = _BATCHSUBMITREQUEST
DESCRIPTOR.message_types_by_name['BatchSubmitResponse'] = _BATCHSUBMITRESPONSE
DESCRIPTOR.message_types_by_name['CreateVertexTypeRequest'] = _CREATEVERTEXTYPEREQUEST
DESCRIPTOR.message_types_by_name['CreateEdgeTypeRequest'] = _CREATEEDGETYPEREQUEST
DESCRIPTOR.message_types_by_name['AddEdgeKindRequest'] = _ADDEDGEKINDREQUEST
DESCRIPTOR.message_types_by_name['RemoveEdgeKindRequest'] = _REMOVEEDGEKINDREQUEST
DESCRIPTOR.message_types_by_name['DropVertexTypeRequest'] = _DROPVERTEXTYPEREQUEST
DESCRIPTOR.message_types_by_name['DropEdgeTypeRequest'] = _DROPEDGETYPEREQUEST
DESCRIPTOR.message_types_by_name['GetGraphDefRequest'] = _GETGRAPHDEFREQUEST
DESCRIPTOR.message_types_by_name['GetGraphDefResponse'] = _GETGRAPHDEFRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BatchSubmitRequest = _reflection.GeneratedProtocolMessageType('BatchSubmitRequest', (_message.Message,), {

  'DDLRequest' : _reflection.GeneratedProtocolMessageType('DDLRequest', (_message.Message,), {
    'DESCRIPTOR' : _BATCHSUBMITREQUEST_DDLREQUEST,
    '__module__' : 'proto.ddl_service_pb2'
    # @@protoc_insertion_point(class_scope:gs.rpc.ddl_service.v1.BatchSubmitRequest.DDLRequest)
    })
  ,
  'DESCRIPTOR' : _BATCHSUBMITREQUEST,
  '__module__' : 'proto.ddl_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.ddl_service.v1.BatchSubmitRequest)
  })
_sym_db.RegisterMessage(BatchSubmitRequest)
_sym_db.RegisterMessage(BatchSubmitRequest.DDLRequest)

BatchSubmitResponse = _reflection.GeneratedProtocolMessageType('BatchSubmitResponse', (_message.Message,), {
  'DESCRIPTOR' : _BATCHSUBMITRESPONSE,
  '__module__' : 'proto.ddl_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.ddl_service.v1.BatchSubmitResponse)
  })
_sym_db.RegisterMessage(BatchSubmitResponse)

CreateVertexTypeRequest = _reflection.GeneratedProtocolMessageType('CreateVertexTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVERTEXTYPEREQUEST,
  '__module__' : 'proto.ddl_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.ddl_service.v1.CreateVertexTypeRequest)
  })
_sym_db.RegisterMessage(CreateVertexTypeRequest)

CreateEdgeTypeRequest = _reflection.GeneratedProtocolMessageType('CreateEdgeTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEEDGETYPEREQUEST,
  '__module__' : 'proto.ddl_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.ddl_service.v1.CreateEdgeTypeRequest)
  })
_sym_db.RegisterMessage(CreateEdgeTypeRequest)

AddEdgeKindRequest = _reflection.GeneratedProtocolMessageType('AddEdgeKindRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDEDGEKINDREQUEST,
  '__module__' : 'proto.ddl_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.ddl_service.v1.AddEdgeKindRequest)
  })
_sym_db.RegisterMessage(AddEdgeKindRequest)

RemoveEdgeKindRequest = _reflection.GeneratedProtocolMessageType('RemoveEdgeKindRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEEDGEKINDREQUEST,
  '__module__' : 'proto.ddl_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.ddl_service.v1.RemoveEdgeKindRequest)
  })
_sym_db.RegisterMessage(RemoveEdgeKindRequest)

DropVertexTypeRequest = _reflection.GeneratedProtocolMessageType('DropVertexTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _DROPVERTEXTYPEREQUEST,
  '__module__' : 'proto.ddl_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.ddl_service.v1.DropVertexTypeRequest)
  })
_sym_db.RegisterMessage(DropVertexTypeRequest)

DropEdgeTypeRequest = _reflection.GeneratedProtocolMessageType('DropEdgeTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _DROPEDGETYPEREQUEST,
  '__module__' : 'proto.ddl_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.ddl_service.v1.DropEdgeTypeRequest)
  })
_sym_db.RegisterMessage(DropEdgeTypeRequest)

GetGraphDefRequest = _reflection.GeneratedProtocolMessageType('GetGraphDefRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGRAPHDEFREQUEST,
  '__module__' : 'proto.ddl_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.ddl_service.v1.GetGraphDefRequest)
  })
_sym_db.RegisterMessage(GetGraphDefRequest)

GetGraphDefResponse = _reflection.GeneratedProtocolMessageType('GetGraphDefResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETGRAPHDEFRESPONSE,
  '__module__' : 'proto.ddl_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.ddl_service.v1.GetGraphDefResponse)
  })
_sym_db.RegisterMessage(GetGraphDefResponse)


DESCRIPTOR._options = None

_CLIENTDDL = _descriptor.ServiceDescriptor(
  name='ClientDdl',
  full_name='gs.rpc.ddl_service.v1.ClientDdl',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1327,
  serialized_end=1542,
  methods=[
  _descriptor.MethodDescriptor(
    name='batchSubmit',
    full_name='gs.rpc.ddl_service.v1.ClientDdl.batchSubmit',
    index=0,
    containing_service=None,
    input_type=_BATCHSUBMITREQUEST,
    output_type=_BATCHSUBMITRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getGraphDef',
    full_name='gs.rpc.ddl_service.v1.ClientDdl.getGraphDef',
    index=1,
    containing_service=None,
    input_type=_GETGRAPHDEFREQUEST,
    output_type=_GETGRAPHDEFRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLIENTDDL)

DESCRIPTOR.services_by_name['ClientDdl'] = _CLIENTDDL

# @@protoc_insertion_point(module_scope)
