# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/cronsqlquery/v1/cronsqlquery.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='github.com/metaprov/modelaapi/services/cronsqlquery/v1/cronsqlquery.proto',
  package='github.com.metaprov.modelaapi.services.cronsqlquery.v1',
  syntax='proto3',
  serialized_options=b'Z6github.com/metaprov/modelaapi/services/cronsqlquery/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nIgithub.com/metaprov/modelaapi/services/cronsqlquery/v1/cronsqlquery.proto\x12\x36github.com.metaprov.modelaapi.services.cronsqlquery.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x44github.com/metaprov/modelaapi/pkg/apis/data/v1alpha1/generated.proto\"\xd8\x01\n\x18ListCronSqlQuerysRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12l\n\x06labels\x18\x03 \x03(\x0b\x32\\.github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"r\n\x19ListCronSqlQuerysResponse\x12U\n\x05items\x18\x01 \x01(\x0b\x32\x46.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.CronSqlQueryList\"\x1c\n\x1a\x43reateCronSqlQueryResponse\"m\n\x19\x43reateCronSqlQueryRequest\x12P\n\x04item\x18\x01 \x01(\x0b\x32\x42.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.CronSqlQuery\"m\n\x19UpdateCronSqlQueryRequest\x12P\n\x04item\x18\x01 \x01(\x0b\x32\x42.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.CronSqlQuery\"\x1c\n\x1aUpdateCronSqlQueryResponse\"9\n\x16GetCronSqlQueryRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"y\n\x17GetCronSqlQueryResponse\x12P\n\x04item\x18\x01 \x01(\x0b\x32\x42.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.CronSqlQuery\x12\x0c\n\x04yaml\x18\x02 \x01(\t\"<\n\x19\x44\x65leteCronSqlQueryRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1c\n\x1a\x44\x65leteCronSqlQueryResponse\";\n\x18PauseCronSqlQueryRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1b\n\x19PauseCronSqlQueryResponse\"<\n\x19ResumeCronSqlQueryRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1c\n\x1aResumeCronSqlQueryResponse\"j\n\x16RunCronSqlQueryRequest\x12P\n\x04item\x18\x01 \x01(\x0b\x32\x42.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.CronSqlQuery\"\x19\n\x17RunCronSqlQueryResponse2\xd2\n\n\x13\x43ronSqlQueryService\x12\xd4\x01\n\x11ListCronSqlQuerys\x12P.github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysRequest\x1aQ.github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/cronsqlqueries\x12\xd9\x01\n\x12\x43reateCronSqlQuery\x12Q.github.com.metaprov.modelaapi.services.cronsqlquery.v1.CreateCronSqlQueryRequest\x1aR.github.com.metaprov.modelaapi.services.cronsqlquery.v1.CreateCronSqlQueryResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v1/cronsqlquerys:\x01*\x12\xd5\x01\n\x0fGetCronSqlQuery\x12N.github.com.metaprov.modelaapi.services.cronsqlquery.v1.GetCronSqlQueryRequest\x1aO.github.com.metaprov.modelaapi.services.cronsqlquery.v1.GetCronSqlQueryResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/cronsqlqueries/{name}\x12\xf6\x01\n\x12UpdateCronSqlQuery\x12Q.github.com.metaprov.modelaapi.services.cronsqlquery.v1.UpdateCronSqlQueryRequest\x1aR.github.com.metaprov.modelaapi.services.cronsqlquery.v1.UpdateCronSqlQueryResponse\"9\x82\xd3\xe4\x93\x02\x33\x1a./v1/cronsqlquerys/{cronsqlquery.metadata.name}:\x01*\x12\xde\x01\n\x12\x44\x65leteCronSqlQuery\x12Q.github.com.metaprov.modelaapi.services.cronsqlquery.v1.DeleteCronSqlQueryRequest\x1aR.github.com.metaprov.modelaapi.services.cronsqlquery.v1.DeleteCronSqlQueryResponse\"!\x82\xd3\xe4\x93\x02\x1b*\x19/v1/cronsqlqueries/{name}\x12\xd5\x01\n\x0bRunSqlQuery\x12N.github.com.metaprov.modelaapi.services.cronsqlquery.v1.RunCronSqlQueryRequest\x1aO.github.com.metaprov.modelaapi.services.cronsqlquery.v1.RunCronSqlQueryResponse\"%\x82\xd3\xe4\x93\x02\x1f\"\x1d/v1/cronsqlqueries/{name}:runB8Z6github.com/metaprov/modelaapi/services/cronsqlquery/v1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2.DESCRIPTOR,])




_LISTCRONSQLQUERYSREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysRequest.LabelsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=405,
  serialized_end=450,
)

_LISTCRONSQLQUERYSREQUEST = _descriptor.Descriptor(
  name='ListCronSqlQuerysRequest',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysRequest.labels', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LISTCRONSQLQUERYSREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=450,
)


_LISTCRONSQLQUERYSRESPONSE = _descriptor.Descriptor(
  name='ListCronSqlQuerysResponse',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysResponse.items', index=0,
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
  serialized_start=452,
  serialized_end=566,
)


_CREATECRONSQLQUERYRESPONSE = _descriptor.Descriptor(
  name='CreateCronSqlQueryResponse',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.CreateCronSqlQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=568,
  serialized_end=596,
)


_CREATECRONSQLQUERYREQUEST = _descriptor.Descriptor(
  name='CreateCronSqlQueryRequest',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.CreateCronSqlQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.CreateCronSqlQueryRequest.item', index=0,
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
  serialized_start=598,
  serialized_end=707,
)


_UPDATECRONSQLQUERYREQUEST = _descriptor.Descriptor(
  name='UpdateCronSqlQueryRequest',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.UpdateCronSqlQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.UpdateCronSqlQueryRequest.item', index=0,
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
  serialized_start=709,
  serialized_end=818,
)


_UPDATECRONSQLQUERYRESPONSE = _descriptor.Descriptor(
  name='UpdateCronSqlQueryResponse',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.UpdateCronSqlQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=820,
  serialized_end=848,
)


_GETCRONSQLQUERYREQUEST = _descriptor.Descriptor(
  name='GetCronSqlQueryRequest',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.GetCronSqlQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.GetCronSqlQueryRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.GetCronSqlQueryRequest.name', index=1,
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
  serialized_start=850,
  serialized_end=907,
)


_GETCRONSQLQUERYRESPONSE = _descriptor.Descriptor(
  name='GetCronSqlQueryResponse',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.GetCronSqlQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.GetCronSqlQueryResponse.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaml', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.GetCronSqlQueryResponse.yaml', index=1,
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
  serialized_start=909,
  serialized_end=1030,
)


_DELETECRONSQLQUERYREQUEST = _descriptor.Descriptor(
  name='DeleteCronSqlQueryRequest',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.DeleteCronSqlQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.DeleteCronSqlQueryRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.DeleteCronSqlQueryRequest.name', index=1,
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
  serialized_start=1032,
  serialized_end=1092,
)


_DELETECRONSQLQUERYRESPONSE = _descriptor.Descriptor(
  name='DeleteCronSqlQueryResponse',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.DeleteCronSqlQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1094,
  serialized_end=1122,
)


_PAUSECRONSQLQUERYREQUEST = _descriptor.Descriptor(
  name='PauseCronSqlQueryRequest',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.PauseCronSqlQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.PauseCronSqlQueryRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.PauseCronSqlQueryRequest.name', index=1,
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
  serialized_start=1124,
  serialized_end=1183,
)


_PAUSECRONSQLQUERYRESPONSE = _descriptor.Descriptor(
  name='PauseCronSqlQueryResponse',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.PauseCronSqlQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_end=1212,
)


_RESUMECRONSQLQUERYREQUEST = _descriptor.Descriptor(
  name='ResumeCronSqlQueryRequest',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.ResumeCronSqlQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.ResumeCronSqlQueryRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.ResumeCronSqlQueryRequest.name', index=1,
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
  serialized_start=1214,
  serialized_end=1274,
)


_RESUMECRONSQLQUERYRESPONSE = _descriptor.Descriptor(
  name='ResumeCronSqlQueryResponse',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.ResumeCronSqlQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1276,
  serialized_end=1304,
)


_RUNCRONSQLQUERYREQUEST = _descriptor.Descriptor(
  name='RunCronSqlQueryRequest',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.RunCronSqlQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.RunCronSqlQueryRequest.item', index=0,
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
  serialized_start=1306,
  serialized_end=1412,
)


_RUNCRONSQLQUERYRESPONSE = _descriptor.Descriptor(
  name='RunCronSqlQueryResponse',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.RunCronSqlQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1414,
  serialized_end=1439,
)

_LISTCRONSQLQUERYSREQUEST_LABELSENTRY.containing_type = _LISTCRONSQLQUERYSREQUEST
_LISTCRONSQLQUERYSREQUEST.fields_by_name['labels'].message_type = _LISTCRONSQLQUERYSREQUEST_LABELSENTRY
_LISTCRONSQLQUERYSRESPONSE.fields_by_name['items'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2._CRONSQLQUERYLIST
_CREATECRONSQLQUERYREQUEST.fields_by_name['item'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2._CRONSQLQUERY
_UPDATECRONSQLQUERYREQUEST.fields_by_name['item'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2._CRONSQLQUERY
_GETCRONSQLQUERYRESPONSE.fields_by_name['item'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2._CRONSQLQUERY
_RUNCRONSQLQUERYREQUEST.fields_by_name['item'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2._CRONSQLQUERY
DESCRIPTOR.message_types_by_name['ListCronSqlQuerysRequest'] = _LISTCRONSQLQUERYSREQUEST
DESCRIPTOR.message_types_by_name['ListCronSqlQuerysResponse'] = _LISTCRONSQLQUERYSRESPONSE
DESCRIPTOR.message_types_by_name['CreateCronSqlQueryResponse'] = _CREATECRONSQLQUERYRESPONSE
DESCRIPTOR.message_types_by_name['CreateCronSqlQueryRequest'] = _CREATECRONSQLQUERYREQUEST
DESCRIPTOR.message_types_by_name['UpdateCronSqlQueryRequest'] = _UPDATECRONSQLQUERYREQUEST
DESCRIPTOR.message_types_by_name['UpdateCronSqlQueryResponse'] = _UPDATECRONSQLQUERYRESPONSE
DESCRIPTOR.message_types_by_name['GetCronSqlQueryRequest'] = _GETCRONSQLQUERYREQUEST
DESCRIPTOR.message_types_by_name['GetCronSqlQueryResponse'] = _GETCRONSQLQUERYRESPONSE
DESCRIPTOR.message_types_by_name['DeleteCronSqlQueryRequest'] = _DELETECRONSQLQUERYREQUEST
DESCRIPTOR.message_types_by_name['DeleteCronSqlQueryResponse'] = _DELETECRONSQLQUERYRESPONSE
DESCRIPTOR.message_types_by_name['PauseCronSqlQueryRequest'] = _PAUSECRONSQLQUERYREQUEST
DESCRIPTOR.message_types_by_name['PauseCronSqlQueryResponse'] = _PAUSECRONSQLQUERYRESPONSE
DESCRIPTOR.message_types_by_name['ResumeCronSqlQueryRequest'] = _RESUMECRONSQLQUERYREQUEST
DESCRIPTOR.message_types_by_name['ResumeCronSqlQueryResponse'] = _RESUMECRONSQLQUERYRESPONSE
DESCRIPTOR.message_types_by_name['RunCronSqlQueryRequest'] = _RUNCRONSQLQUERYREQUEST
DESCRIPTOR.message_types_by_name['RunCronSqlQueryResponse'] = _RUNCRONSQLQUERYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListCronSqlQuerysRequest = _reflection.GeneratedProtocolMessageType('ListCronSqlQuerysRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTCRONSQLQUERYSREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTCRONSQLQUERYSREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysRequest)
  })
_sym_db.RegisterMessage(ListCronSqlQuerysRequest)
_sym_db.RegisterMessage(ListCronSqlQuerysRequest.LabelsEntry)

ListCronSqlQuerysResponse = _reflection.GeneratedProtocolMessageType('ListCronSqlQuerysResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCRONSQLQUERYSRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.ListCronSqlQuerysResponse)
  })
_sym_db.RegisterMessage(ListCronSqlQuerysResponse)

CreateCronSqlQueryResponse = _reflection.GeneratedProtocolMessageType('CreateCronSqlQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATECRONSQLQUERYRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.CreateCronSqlQueryResponse)
  })
_sym_db.RegisterMessage(CreateCronSqlQueryResponse)

CreateCronSqlQueryRequest = _reflection.GeneratedProtocolMessageType('CreateCronSqlQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECRONSQLQUERYREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.CreateCronSqlQueryRequest)
  })
_sym_db.RegisterMessage(CreateCronSqlQueryRequest)

UpdateCronSqlQueryRequest = _reflection.GeneratedProtocolMessageType('UpdateCronSqlQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECRONSQLQUERYREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.UpdateCronSqlQueryRequest)
  })
_sym_db.RegisterMessage(UpdateCronSqlQueryRequest)

UpdateCronSqlQueryResponse = _reflection.GeneratedProtocolMessageType('UpdateCronSqlQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECRONSQLQUERYRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.UpdateCronSqlQueryResponse)
  })
_sym_db.RegisterMessage(UpdateCronSqlQueryResponse)

GetCronSqlQueryRequest = _reflection.GeneratedProtocolMessageType('GetCronSqlQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCRONSQLQUERYREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.GetCronSqlQueryRequest)
  })
_sym_db.RegisterMessage(GetCronSqlQueryRequest)

GetCronSqlQueryResponse = _reflection.GeneratedProtocolMessageType('GetCronSqlQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCRONSQLQUERYRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.GetCronSqlQueryResponse)
  })
_sym_db.RegisterMessage(GetCronSqlQueryResponse)

DeleteCronSqlQueryRequest = _reflection.GeneratedProtocolMessageType('DeleteCronSqlQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECRONSQLQUERYREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.DeleteCronSqlQueryRequest)
  })
_sym_db.RegisterMessage(DeleteCronSqlQueryRequest)

DeleteCronSqlQueryResponse = _reflection.GeneratedProtocolMessageType('DeleteCronSqlQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETECRONSQLQUERYRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.DeleteCronSqlQueryResponse)
  })
_sym_db.RegisterMessage(DeleteCronSqlQueryResponse)

PauseCronSqlQueryRequest = _reflection.GeneratedProtocolMessageType('PauseCronSqlQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAUSECRONSQLQUERYREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.PauseCronSqlQueryRequest)
  })
_sym_db.RegisterMessage(PauseCronSqlQueryRequest)

PauseCronSqlQueryResponse = _reflection.GeneratedProtocolMessageType('PauseCronSqlQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _PAUSECRONSQLQUERYRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.PauseCronSqlQueryResponse)
  })
_sym_db.RegisterMessage(PauseCronSqlQueryResponse)

ResumeCronSqlQueryRequest = _reflection.GeneratedProtocolMessageType('ResumeCronSqlQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESUMECRONSQLQUERYREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.ResumeCronSqlQueryRequest)
  })
_sym_db.RegisterMessage(ResumeCronSqlQueryRequest)

ResumeCronSqlQueryResponse = _reflection.GeneratedProtocolMessageType('ResumeCronSqlQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESUMECRONSQLQUERYRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.ResumeCronSqlQueryResponse)
  })
_sym_db.RegisterMessage(ResumeCronSqlQueryResponse)

RunCronSqlQueryRequest = _reflection.GeneratedProtocolMessageType('RunCronSqlQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNCRONSQLQUERYREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.RunCronSqlQueryRequest)
  })
_sym_db.RegisterMessage(RunCronSqlQueryRequest)

RunCronSqlQueryResponse = _reflection.GeneratedProtocolMessageType('RunCronSqlQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNCRONSQLQUERYRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronsqlquery.v1.cronsqlquery_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronsqlquery.v1.RunCronSqlQueryResponse)
  })
_sym_db.RegisterMessage(RunCronSqlQueryResponse)


DESCRIPTOR._options = None
_LISTCRONSQLQUERYSREQUEST_LABELSENTRY._options = None

_CRONSQLQUERYSERVICE = _descriptor.ServiceDescriptor(
  name='CronSqlQueryService',
  full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.CronSqlQueryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1442,
  serialized_end=2804,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListCronSqlQuerys',
    full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.CronSqlQueryService.ListCronSqlQuerys',
    index=0,
    containing_service=None,
    input_type=_LISTCRONSQLQUERYSREQUEST,
    output_type=_LISTCRONSQLQUERYSRESPONSE,
    serialized_options=b'\202\323\344\223\002\024\022\022/v1/cronsqlqueries',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateCronSqlQuery',
    full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.CronSqlQueryService.CreateCronSqlQuery',
    index=1,
    containing_service=None,
    input_type=_CREATECRONSQLQUERYREQUEST,
    output_type=_CREATECRONSQLQUERYRESPONSE,
    serialized_options=b'\202\323\344\223\002\026\"\021/v1/cronsqlquerys:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetCronSqlQuery',
    full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.CronSqlQueryService.GetCronSqlQuery',
    index=2,
    containing_service=None,
    input_type=_GETCRONSQLQUERYREQUEST,
    output_type=_GETCRONSQLQUERYRESPONSE,
    serialized_options=b'\202\323\344\223\002\033\022\031/v1/cronsqlqueries/{name}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateCronSqlQuery',
    full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.CronSqlQueryService.UpdateCronSqlQuery',
    index=3,
    containing_service=None,
    input_type=_UPDATECRONSQLQUERYREQUEST,
    output_type=_UPDATECRONSQLQUERYRESPONSE,
    serialized_options=b'\202\323\344\223\0023\032./v1/cronsqlquerys/{cronsqlquery.metadata.name}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteCronSqlQuery',
    full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.CronSqlQueryService.DeleteCronSqlQuery',
    index=4,
    containing_service=None,
    input_type=_DELETECRONSQLQUERYREQUEST,
    output_type=_DELETECRONSQLQUERYRESPONSE,
    serialized_options=b'\202\323\344\223\002\033*\031/v1/cronsqlqueries/{name}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RunSqlQuery',
    full_name='github.com.metaprov.modelaapi.services.cronsqlquery.v1.CronSqlQueryService.RunSqlQuery',
    index=5,
    containing_service=None,
    input_type=_RUNCRONSQLQUERYREQUEST,
    output_type=_RUNCRONSQLQUERYRESPONSE,
    serialized_options=b'\202\323\344\223\002\037\"\035/v1/cronsqlqueries/{name}:run',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CRONSQLQUERYSERVICE)

DESCRIPTOR.services_by_name['CronSqlQueryService'] = _CRONSQLQUERYSERVICE

# @@protoc_insertion_point(module_scope)
