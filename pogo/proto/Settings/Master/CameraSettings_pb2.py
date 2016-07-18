# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Settings/Master/CameraSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Enums import CameraTarget_pb2 as Enums_dot_CameraTarget__pb2
from Enums import CameraInterpolation_pb2 as Enums_dot_CameraInterpolation__pb2

from Enums.CameraTarget_pb2 import *
from Enums.CameraInterpolation_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Settings/Master/CameraSettings.proto',
  package='POGOProtos.Settings.Master',
  syntax='proto3',
  serialized_pb=_b('\n$Settings/Master/CameraSettings.proto\x12\x1aPOGOProtos.Settings.Master\x1a\x18\x45nums/CameraTarget.proto\x1a\x1f\x45nums/CameraInterpolation.proto\"\xd7\x03\n\x0e\x43\x61meraSettings\x12\x13\n\x0bnext_camera\x18\x01 \x01(\t\x12<\n\rinterpolation\x18\x02 \x03(\x0e\x32%.POGOProtos.Enums.CameraInterpolation\x12\x33\n\x0btarget_type\x18\x03 \x03(\x0e\x32\x1e.POGOProtos.Enums.CameraTarget\x12\x15\n\rease_in_speed\x18\x04 \x03(\x02\x12\x16\n\x0e\x65\x61st_out_speed\x18\x05 \x03(\x02\x12\x18\n\x10\x64uration_seconds\x18\x06 \x03(\x02\x12\x14\n\x0cwait_seconds\x18\x07 \x03(\x02\x12\x1a\n\x12transition_seconds\x18\x08 \x03(\x02\x12\x14\n\x0c\x61ngle_degree\x18\t \x03(\x02\x12\x1b\n\x13\x61ngle_offset_degree\x18\n \x03(\x02\x12\x14\n\x0cpitch_degree\x18\x0b \x03(\x02\x12\x1b\n\x13pitch_offset_degree\x18\x0c \x03(\x02\x12\x13\n\x0broll_degree\x18\r \x03(\x02\x12\x17\n\x0f\x64istance_meters\x18\x0e \x03(\x02\x12\x16\n\x0eheight_percent\x18\x0f \x03(\x02\x12\x16\n\x0evert_ctr_ratio\x18\x10 \x03(\x02P\x00P\x01\x62\x06proto3')
  ,
  dependencies=[Enums_dot_CameraTarget__pb2.DESCRIPTOR,Enums_dot_CameraInterpolation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CAMERASETTINGS = _descriptor.Descriptor(
  name='CameraSettings',
  full_name='POGOProtos.Settings.Master.CameraSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_camera', full_name='POGOProtos.Settings.Master.CameraSettings.next_camera', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interpolation', full_name='POGOProtos.Settings.Master.CameraSettings.interpolation', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_type', full_name='POGOProtos.Settings.Master.CameraSettings.target_type', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ease_in_speed', full_name='POGOProtos.Settings.Master.CameraSettings.ease_in_speed', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='east_out_speed', full_name='POGOProtos.Settings.Master.CameraSettings.east_out_speed', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration_seconds', full_name='POGOProtos.Settings.Master.CameraSettings.duration_seconds', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wait_seconds', full_name='POGOProtos.Settings.Master.CameraSettings.wait_seconds', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transition_seconds', full_name='POGOProtos.Settings.Master.CameraSettings.transition_seconds', index=7,
      number=8, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle_degree', full_name='POGOProtos.Settings.Master.CameraSettings.angle_degree', index=8,
      number=9, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle_offset_degree', full_name='POGOProtos.Settings.Master.CameraSettings.angle_offset_degree', index=9,
      number=10, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pitch_degree', full_name='POGOProtos.Settings.Master.CameraSettings.pitch_degree', index=10,
      number=11, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pitch_offset_degree', full_name='POGOProtos.Settings.Master.CameraSettings.pitch_offset_degree', index=11,
      number=12, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roll_degree', full_name='POGOProtos.Settings.Master.CameraSettings.roll_degree', index=12,
      number=13, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance_meters', full_name='POGOProtos.Settings.Master.CameraSettings.distance_meters', index=13,
      number=14, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height_percent', full_name='POGOProtos.Settings.Master.CameraSettings.height_percent', index=14,
      number=15, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vert_ctr_ratio', full_name='POGOProtos.Settings.Master.CameraSettings.vert_ctr_ratio', index=15,
      number=16, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=128,
  serialized_end=599,
)

_CAMERASETTINGS.fields_by_name['interpolation'].enum_type = Enums_dot_CameraInterpolation__pb2._CAMERAINTERPOLATION
_CAMERASETTINGS.fields_by_name['target_type'].enum_type = Enums_dot_CameraTarget__pb2._CAMERATARGET
DESCRIPTOR.message_types_by_name['CameraSettings'] = _CAMERASETTINGS

CameraSettings = _reflection.GeneratedProtocolMessageType('CameraSettings', (_message.Message,), dict(
  DESCRIPTOR = _CAMERASETTINGS,
  __module__ = 'Settings.Master.CameraSettings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Master.CameraSettings)
  ))
_sym_db.RegisterMessage(CameraSettings)


# @@protoc_insertion_point(module_scope)
