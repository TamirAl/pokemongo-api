# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Requests/Messages/ReleasePokemonMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Networking/Requests/Messages/ReleasePokemonMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\n8Networking/Requests/Messages/ReleasePokemonMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\"+\n\x15ReleasePokemonMessage\x12\x12\n\npokemon_id\x18\x01 \x01(\x06\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RELEASEPOKEMONMESSAGE = _descriptor.Descriptor(
  name='ReleasePokemonMessage',
  full_name='POGOProtos.Networking.Requests.Messages.ReleasePokemonMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='POGOProtos.Networking.Requests.Messages.ReleasePokemonMessage.pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=144,
)

DESCRIPTOR.message_types_by_name['ReleasePokemonMessage'] = _RELEASEPOKEMONMESSAGE

ReleasePokemonMessage = _reflection.GeneratedProtocolMessageType('ReleasePokemonMessage', (_message.Message,), dict(
  DESCRIPTOR = _RELEASEPOKEMONMESSAGE,
  __module__ = 'Networking.Requests.Messages.ReleasePokemonMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.ReleasePokemonMessage)
  ))
_sym_db.RegisterMessage(ReleasePokemonMessage)


# @@protoc_insertion_point(module_scope)
