# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Inventory/InventoryUpgrades.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Inventory import InventoryUpgrade_pb2 as Inventory_dot_InventoryUpgrade__pb2
Inventory_dot_ItemId__pb2 = Inventory_dot_InventoryUpgrade__pb2.Inventory_dot_ItemId__pb2
Inventory_dot_InventoryUpgradeType__pb2 = Inventory_dot_InventoryUpgrade__pb2.Inventory_dot_InventoryUpgradeType__pb2

from Inventory.InventoryUpgrade_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Inventory/InventoryUpgrades.proto',
  package='POGOProtos.Inventory',
  syntax='proto3',
  serialized_pb=_b('\n!Inventory/InventoryUpgrades.proto\x12\x14POGOProtos.Inventory\x1a Inventory/InventoryUpgrade.proto\"W\n\x11InventoryUpgrades\x12\x42\n\x12inventory_upgrades\x18\x01 \x03(\x0b\x32&.POGOProtos.Inventory.InventoryUpgradeP\x00\x62\x06proto3')
  ,
  dependencies=[Inventory_dot_InventoryUpgrade__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INVENTORYUPGRADES = _descriptor.Descriptor(
  name='InventoryUpgrades',
  full_name='POGOProtos.Inventory.InventoryUpgrades',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inventory_upgrades', full_name='POGOProtos.Inventory.InventoryUpgrades.inventory_upgrades', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=93,
  serialized_end=180,
)

_INVENTORYUPGRADES.fields_by_name['inventory_upgrades'].message_type = Inventory_dot_InventoryUpgrade__pb2._INVENTORYUPGRADE
DESCRIPTOR.message_types_by_name['InventoryUpgrades'] = _INVENTORYUPGRADES

InventoryUpgrades = _reflection.GeneratedProtocolMessageType('InventoryUpgrades', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYUPGRADES,
  __module__ = 'Inventory.InventoryUpgrades_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.InventoryUpgrades)
  ))
_sym_db.RegisterMessage(InventoryUpgrades)


# @@protoc_insertion_point(module_scope)
