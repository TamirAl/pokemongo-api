# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Player/PlayerCamera.proto

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
  name='Player/PlayerCamera.proto',
  package='POGOProtos.Player',
  syntax='proto3',
  serialized_pb=_b('\n\x19Player/PlayerCamera.proto\x12\x11POGOProtos.Player\")\n\x0cPlayerCamera\x12\x19\n\x11is_default_camera\x18\x01 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PLAYERCAMERA = _descriptor.Descriptor(
  name='PlayerCamera',
  full_name='POGOProtos.Player.PlayerCamera',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_default_camera', full_name='POGOProtos.Player.PlayerCamera.is_default_camera', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=48,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['PlayerCamera'] = _PLAYERCAMERA

PlayerCamera = _reflection.GeneratedProtocolMessageType('PlayerCamera', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERCAMERA,
  __module__ = 'Player.PlayerCamera_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Player.PlayerCamera)
  ))
_sym_db.RegisterMessage(PlayerCamera)


# @@protoc_insertion_point(module_scope)
