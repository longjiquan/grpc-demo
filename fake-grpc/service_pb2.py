# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import service_msg_pb2 as service__msg__pb2
import schema_pb2 as schema__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='milvus.proto.service',
  syntax='proto3',
  serialized_options=_b('ZAgithub.com/zilliztech/milvus-distributed/internal/proto/servicepb'),
  serialized_pb=_b('\n\rservice.proto\x12\x14milvus.proto.service\x1a\x0c\x63ommon.proto\x1a\x11service_msg.proto\x1a\x0cschema.proto2\xda\x08\n\rMilvusService\x12X\n\x10\x43reateCollection\x12%.milvus.proto.schema.CollectionSchema\x1a\x1b.milvus.proto.common.Status\"\x00\x12U\n\x0e\x44ropCollection\x12$.milvus.proto.service.CollectionName\x1a\x1b.milvus.proto.common.Status\"\x00\x12[\n\rHasCollection\x12$.milvus.proto.service.CollectionName\x1a\".milvus.proto.service.BoolResponse\"\x00\x12i\n\x12\x44\x65scribeCollection\x12$.milvus.proto.service.CollectionName\x1a+.milvus.proto.service.CollectionDescription\"\x00\x12Y\n\x0fShowCollections\x12\x1a.milvus.proto.common.Empty\x1a(.milvus.proto.service.StringListResponse\"\x00\x12U\n\x0f\x43reatePartition\x12#.milvus.proto.service.PartitionName\x1a\x1b.milvus.proto.common.Status\"\x00\x12S\n\rDropPartition\x12#.milvus.proto.service.PartitionName\x1a\x1b.milvus.proto.common.Status\"\x00\x12Y\n\x0cHasPartition\x12#.milvus.proto.service.PartitionName\x1a\".milvus.proto.service.BoolResponse\"\x00\x12\x66\n\x11\x44\x65scribePartition\x12#.milvus.proto.service.PartitionName\x1a*.milvus.proto.service.PartitionDescription\"\x00\x12\x62\n\x0eShowPartitions\x12$.milvus.proto.service.CollectionName\x1a(.milvus.proto.service.StringListResponse\"\x00\x12V\n\x06Insert\x12\x1e.milvus.proto.service.RowBatch\x1a*.milvus.proto.service.IntegerRangeResponse\"\x00\x12J\n\x06Search\x12\x1b.milvus.proto.service.Query\x1a!.milvus.proto.service.QueryResult\"\x00\x42\x43ZAgithub.com/zilliztech/milvus-distributed/internal/proto/servicepbb\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,service__msg__pb2.DESCRIPTOR,schema__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_MILVUSSERVICE = _descriptor.ServiceDescriptor(
  name='MilvusService',
  full_name='milvus.proto.service.MilvusService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=87,
  serialized_end=1201,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateCollection',
    full_name='milvus.proto.service.MilvusService.CreateCollection',
    index=0,
    containing_service=None,
    input_type=schema__pb2._COLLECTIONSCHEMA,
    output_type=common__pb2._STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DropCollection',
    full_name='milvus.proto.service.MilvusService.DropCollection',
    index=1,
    containing_service=None,
    input_type=service__msg__pb2._COLLECTIONNAME,
    output_type=common__pb2._STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HasCollection',
    full_name='milvus.proto.service.MilvusService.HasCollection',
    index=2,
    containing_service=None,
    input_type=service__msg__pb2._COLLECTIONNAME,
    output_type=service__msg__pb2._BOOLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeCollection',
    full_name='milvus.proto.service.MilvusService.DescribeCollection',
    index=3,
    containing_service=None,
    input_type=service__msg__pb2._COLLECTIONNAME,
    output_type=service__msg__pb2._COLLECTIONDESCRIPTION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ShowCollections',
    full_name='milvus.proto.service.MilvusService.ShowCollections',
    index=4,
    containing_service=None,
    input_type=common__pb2._EMPTY,
    output_type=service__msg__pb2._STRINGLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreatePartition',
    full_name='milvus.proto.service.MilvusService.CreatePartition',
    index=5,
    containing_service=None,
    input_type=service__msg__pb2._PARTITIONNAME,
    output_type=common__pb2._STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DropPartition',
    full_name='milvus.proto.service.MilvusService.DropPartition',
    index=6,
    containing_service=None,
    input_type=service__msg__pb2._PARTITIONNAME,
    output_type=common__pb2._STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HasPartition',
    full_name='milvus.proto.service.MilvusService.HasPartition',
    index=7,
    containing_service=None,
    input_type=service__msg__pb2._PARTITIONNAME,
    output_type=service__msg__pb2._BOOLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribePartition',
    full_name='milvus.proto.service.MilvusService.DescribePartition',
    index=8,
    containing_service=None,
    input_type=service__msg__pb2._PARTITIONNAME,
    output_type=service__msg__pb2._PARTITIONDESCRIPTION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ShowPartitions',
    full_name='milvus.proto.service.MilvusService.ShowPartitions',
    index=9,
    containing_service=None,
    input_type=service__msg__pb2._COLLECTIONNAME,
    output_type=service__msg__pb2._STRINGLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Insert',
    full_name='milvus.proto.service.MilvusService.Insert',
    index=10,
    containing_service=None,
    input_type=service__msg__pb2._ROWBATCH,
    output_type=service__msg__pb2._INTEGERRANGERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='milvus.proto.service.MilvusService.Search',
    index=11,
    containing_service=None,
    input_type=service__msg__pb2._QUERY,
    output_type=service__msg__pb2._QUERYRESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MILVUSSERVICE)

DESCRIPTOR.services_by_name['MilvusService'] = _MILVUSSERVICE

# @@protoc_insertion_point(module_scope)