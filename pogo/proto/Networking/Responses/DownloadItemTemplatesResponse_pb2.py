# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Responses/DownloadItemTemplatesResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Settings.Master import ItemSettings_pb2 as Settings_dot_Master_dot_ItemSettings__pb2
Enums_dot_ItemCategory__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Enums_dot_ItemCategory__pb2
Inventory_dot_ItemId__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Inventory_dot_ItemId__pb2
Inventory_dot_ItemType__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Inventory_dot_ItemType__pb2
Settings_dot_Master_dot_Item_dot_FoodAttributes__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Settings_dot_Master_dot_Item_dot_FoodAttributes__pb2
Enums_dot_ItemEffect__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Enums_dot_ItemEffect__pb2
Settings_dot_Master_dot_Item_dot_PotionAttributes__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Settings_dot_Master_dot_Item_dot_PotionAttributes__pb2
Settings_dot_Master_dot_Item_dot_ReviveAttributes__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Settings_dot_Master_dot_Item_dot_ReviveAttributes__pb2
Settings_dot_Master_dot_Item_dot_BattleAttributes__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Settings_dot_Master_dot_Item_dot_BattleAttributes__pb2
Settings_dot_Master_dot_Item_dot_IncenseAttributes__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Settings_dot_Master_dot_Item_dot_IncenseAttributes__pb2
Enums_dot_PokemonType__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Enums_dot_PokemonType__pb2
Settings_dot_Master_dot_Item_dot_PokeballAttributes__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Settings_dot_Master_dot_Item_dot_PokeballAttributes__pb2
Enums_dot_ItemEffect__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Enums_dot_ItemEffect__pb2
Settings_dot_Master_dot_Item_dot_FortModifierAttributes__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Settings_dot_Master_dot_Item_dot_FortModifierAttributes__pb2
Settings_dot_Master_dot_Item_dot_EggIncubatorAttributes__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Settings_dot_Master_dot_Item_dot_EggIncubatorAttributes__pb2
Inventory_dot_EggIncubatorType__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Inventory_dot_EggIncubatorType__pb2
Settings_dot_Master_dot_Item_dot_ExperienceBoostAttributes__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Settings_dot_Master_dot_Item_dot_ExperienceBoostAttributes__pb2
Settings_dot_Master_dot_Item_dot_InventoryUpgradeAttributes__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Settings_dot_Master_dot_Item_dot_InventoryUpgradeAttributes__pb2
Inventory_dot_InventoryUpgradeType__pb2 = Settings_dot_Master_dot_ItemSettings__pb2.Inventory_dot_InventoryUpgradeType__pb2
from Settings.Master import MoveSettings_pb2 as Settings_dot_Master_dot_MoveSettings__pb2
Enums_dot_PokemonType__pb2 = Settings_dot_Master_dot_MoveSettings__pb2.Enums_dot_PokemonType__pb2
Enums_dot_PokemonMovementType__pb2 = Settings_dot_Master_dot_MoveSettings__pb2.Enums_dot_PokemonMovementType__pb2
from Settings.Master import BadgeSettings_pb2 as Settings_dot_Master_dot_BadgeSettings__pb2
Enums_dot_BadgeType__pb2 = Settings_dot_Master_dot_BadgeSettings__pb2.Enums_dot_BadgeType__pb2
from Settings.Master import PokemonSettings_pb2 as Settings_dot_Master_dot_PokemonSettings__pb2
Enums_dot_PokemonId__pb2 = Settings_dot_Master_dot_PokemonSettings__pb2.Enums_dot_PokemonId__pb2
Enums_dot_PokemonClass__pb2 = Settings_dot_Master_dot_PokemonSettings__pb2.Enums_dot_PokemonClass__pb2
Enums_dot_PokemonType__pb2 = Settings_dot_Master_dot_PokemonSettings__pb2.Enums_dot_PokemonType__pb2
Enums_dot_PokemonMove__pb2 = Settings_dot_Master_dot_PokemonSettings__pb2.Enums_dot_PokemonMove__pb2
Enums_dot_PokemonFamilyId__pb2 = Settings_dot_Master_dot_PokemonSettings__pb2.Enums_dot_PokemonFamilyId__pb2
Settings_dot_Master_dot_Pokemon_dot_StatsAttributes__pb2 = Settings_dot_Master_dot_PokemonSettings__pb2.Settings_dot_Master_dot_Pokemon_dot_StatsAttributes__pb2
Settings_dot_Master_dot_Pokemon_dot_CameraAttributes__pb2 = Settings_dot_Master_dot_PokemonSettings__pb2.Settings_dot_Master_dot_Pokemon_dot_CameraAttributes__pb2
Settings_dot_Master_dot_Pokemon_dot_EncounterAttributes__pb2 = Settings_dot_Master_dot_PokemonSettings__pb2.Settings_dot_Master_dot_Pokemon_dot_EncounterAttributes__pb2
Enums_dot_PokemonMovementType__pb2 = Settings_dot_Master_dot_PokemonSettings__pb2.Enums_dot_PokemonMovementType__pb2
from Settings.Master import MoveSequenceSettings_pb2 as Settings_dot_Master_dot_MoveSequenceSettings__pb2
from Settings.Master import TypeEffectiveSettings_pb2 as Settings_dot_Master_dot_TypeEffectiveSettings__pb2
Enums_dot_BadgeType__pb2 = Settings_dot_Master_dot_TypeEffectiveSettings__pb2.Enums_dot_BadgeType__pb2
from Settings.Master import CameraSettings_pb2 as Settings_dot_Master_dot_CameraSettings__pb2
Enums_dot_CameraTarget__pb2 = Settings_dot_Master_dot_CameraSettings__pb2.Enums_dot_CameraTarget__pb2
Enums_dot_CameraInterpolation__pb2 = Settings_dot_Master_dot_CameraSettings__pb2.Enums_dot_CameraInterpolation__pb2
from Settings.Master import PlayerLevelSettings_pb2 as Settings_dot_Master_dot_PlayerLevelSettings__pb2
from Settings.Master import GymLevelSettings_pb2 as Settings_dot_Master_dot_GymLevelSettings__pb2
from Settings.Master import GymBattleSettings_pb2 as Settings_dot_Master_dot_GymBattleSettings__pb2
from Settings.Master import EncounterSettings_pb2 as Settings_dot_Master_dot_EncounterSettings__pb2
from Settings.Master import IapItemDisplay_pb2 as Settings_dot_Master_dot_IapItemDisplay__pb2
Enums_dot_IapItemCategory__pb2 = Settings_dot_Master_dot_IapItemDisplay__pb2.Enums_dot_IapItemCategory__pb2
Inventory_dot_ItemId__pb2 = Settings_dot_Master_dot_IapItemDisplay__pb2.Inventory_dot_ItemId__pb2
from Settings.Master import IapSettings_pb2 as Settings_dot_Master_dot_IapSettings__pb2
from Settings.Master import PokemonUpgradeSettings_pb2 as Settings_dot_Master_dot_PokemonUpgradeSettings__pb2
from Settings.Master import EquippedBadgeSettings_pb2 as Settings_dot_Master_dot_EquippedBadgeSettings__pb2

from Settings.Master.ItemSettings_pb2 import *
from Settings.Master.MoveSettings_pb2 import *
from Settings.Master.BadgeSettings_pb2 import *
from Settings.Master.PokemonSettings_pb2 import *
from Settings.Master.MoveSequenceSettings_pb2 import *
from Settings.Master.TypeEffectiveSettings_pb2 import *
from Settings.Master.CameraSettings_pb2 import *
from Settings.Master.PlayerLevelSettings_pb2 import *
from Settings.Master.GymLevelSettings_pb2 import *
from Settings.Master.GymBattleSettings_pb2 import *
from Settings.Master.EncounterSettings_pb2 import *
from Settings.Master.IapItemDisplay_pb2 import *
from Settings.Master.IapSettings_pb2 import *
from Settings.Master.PokemonUpgradeSettings_pb2 import *
from Settings.Master.EquippedBadgeSettings_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Networking/Responses/DownloadItemTemplatesResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n8Networking/Responses/DownloadItemTemplatesResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a\"Settings/Master/ItemSettings.proto\x1a\"Settings/Master/MoveSettings.proto\x1a#Settings/Master/BadgeSettings.proto\x1a%Settings/Master/PokemonSettings.proto\x1a*Settings/Master/MoveSequenceSettings.proto\x1a+Settings/Master/TypeEffectiveSettings.proto\x1a$Settings/Master/CameraSettings.proto\x1a)Settings/Master/PlayerLevelSettings.proto\x1a&Settings/Master/GymLevelSettings.proto\x1a\'Settings/Master/GymBattleSettings.proto\x1a\'Settings/Master/EncounterSettings.proto\x1a$Settings/Master/IapItemDisplay.proto\x1a!Settings/Master/IapSettings.proto\x1a,Settings/Master/PokemonUpgradeSettings.proto\x1a+Settings/Master/EquippedBadgeSettings.proto\"\xf0\t\n\x1d\x44ownloadItemTemplatesResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x63\n\x0eitem_templates\x18\x02 \x03(\x0b\x32K.POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate\x12\x14\n\x0ctimestamp_ms\x18\x03 \x01(\x04\x1a\xc2\x08\n\x0cItemTemplate\x12\x13\n\x0btemplate_id\x18\x01 \x01(\t\x12\x45\n\x10pokemon_settings\x18\x02 \x01(\x0b\x32+.POGOProtos.Settings.Master.PokemonSettings\x12?\n\ritem_settings\x18\x03 \x01(\x0b\x32(.POGOProtos.Settings.Master.ItemSettings\x12?\n\rmove_settings\x18\x04 \x01(\x0b\x32(.POGOProtos.Settings.Master.MoveSettings\x12P\n\x16move_sequence_settings\x18\x05 \x01(\x0b\x32\x30.POGOProtos.Settings.Master.MoveSequenceSettings\x12I\n\x0etype_effective\x18\x08 \x01(\x0b\x32\x31.POGOProtos.Settings.Master.TypeEffectiveSettings\x12\x41\n\x0e\x62\x61\x64ge_settings\x18\n \x01(\x0b\x32).POGOProtos.Settings.Master.BadgeSettings\x12:\n\x06\x63\x61mera\x18\x0b \x01(\x0b\x32*.POGOProtos.Settings.Master.CameraSettings\x12\x45\n\x0cplayer_level\x18\x0c \x01(\x0b\x32/.POGOProtos.Settings.Master.PlayerLevelSettings\x12?\n\tgym_level\x18\r \x01(\x0b\x32,.POGOProtos.Settings.Master.GymLevelSettings\x12\x46\n\x0f\x62\x61ttle_settings\x18\x0e \x01(\x0b\x32-.POGOProtos.Settings.Master.GymBattleSettings\x12I\n\x12\x65ncounter_settings\x18\x0f \x01(\x0b\x32-.POGOProtos.Settings.Master.EncounterSettings\x12\x44\n\x10iap_item_display\x18\x10 \x01(\x0b\x32*.POGOProtos.Settings.Master.IapItemDisplay\x12=\n\x0ciap_settings\x18\x11 \x01(\x0b\x32\'.POGOProtos.Settings.Master.IapSettings\x12L\n\x10pokemon_upgrades\x18\x12 \x01(\x0b\x32\x32.POGOProtos.Settings.Master.PokemonUpgradeSettings\x12J\n\x0f\x65quipped_badges\x18\x13 \x01(\x0b\x32\x31.POGOProtos.Settings.Master.EquippedBadgeSettingsP\x00P\x01P\x02P\x03P\x04P\x05P\x06P\x07P\x08P\tP\nP\x0bP\x0cP\rP\x0e\x62\x06proto3')
  ,
  dependencies=[Settings_dot_Master_dot_ItemSettings__pb2.DESCRIPTOR,Settings_dot_Master_dot_MoveSettings__pb2.DESCRIPTOR,Settings_dot_Master_dot_BadgeSettings__pb2.DESCRIPTOR,Settings_dot_Master_dot_PokemonSettings__pb2.DESCRIPTOR,Settings_dot_Master_dot_MoveSequenceSettings__pb2.DESCRIPTOR,Settings_dot_Master_dot_TypeEffectiveSettings__pb2.DESCRIPTOR,Settings_dot_Master_dot_CameraSettings__pb2.DESCRIPTOR,Settings_dot_Master_dot_PlayerLevelSettings__pb2.DESCRIPTOR,Settings_dot_Master_dot_GymLevelSettings__pb2.DESCRIPTOR,Settings_dot_Master_dot_GymBattleSettings__pb2.DESCRIPTOR,Settings_dot_Master_dot_EncounterSettings__pb2.DESCRIPTOR,Settings_dot_Master_dot_IapItemDisplay__pb2.DESCRIPTOR,Settings_dot_Master_dot_IapSettings__pb2.DESCRIPTOR,Settings_dot_Master_dot_PokemonUpgradeSettings__pb2.DESCRIPTOR,Settings_dot_Master_dot_EquippedBadgeSettings__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE = _descriptor.Descriptor(
  name='ItemTemplate',
  full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.template_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_settings', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.pokemon_settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_settings', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.item_settings', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_settings', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.move_settings', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_sequence_settings', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.move_sequence_settings', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type_effective', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.type_effective', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='badge_settings', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.badge_settings', index=6,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='camera', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.camera', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_level', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.player_level', index=8,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gym_level', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.gym_level', index=9,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_settings', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.battle_settings', index=10,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encounter_settings', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.encounter_settings', index=11,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iap_item_display', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.iap_item_display', index=12,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iap_settings', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.iap_settings', index=13,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_upgrades', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.pokemon_upgrades', index=14,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipped_badges', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate.equipped_badges', index=15,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=872,
  serialized_end=1962,
)

_DOWNLOADITEMTEMPLATESRESPONSE = _descriptor.Descriptor(
  name='DownloadItemTemplatesResponse',
  full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_templates', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.item_templates', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.timestamp_ms', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=698,
  serialized_end=1962,
)

_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['pokemon_settings'].message_type = Settings_dot_Master_dot_PokemonSettings__pb2._POKEMONSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['item_settings'].message_type = Settings_dot_Master_dot_ItemSettings__pb2._ITEMSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['move_settings'].message_type = Settings_dot_Master_dot_MoveSettings__pb2._MOVESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['move_sequence_settings'].message_type = Settings_dot_Master_dot_MoveSequenceSettings__pb2._MOVESEQUENCESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['type_effective'].message_type = Settings_dot_Master_dot_TypeEffectiveSettings__pb2._TYPEEFFECTIVESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['badge_settings'].message_type = Settings_dot_Master_dot_BadgeSettings__pb2._BADGESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['camera'].message_type = Settings_dot_Master_dot_CameraSettings__pb2._CAMERASETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['player_level'].message_type = Settings_dot_Master_dot_PlayerLevelSettings__pb2._PLAYERLEVELSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['gym_level'].message_type = Settings_dot_Master_dot_GymLevelSettings__pb2._GYMLEVELSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['battle_settings'].message_type = Settings_dot_Master_dot_GymBattleSettings__pb2._GYMBATTLESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['encounter_settings'].message_type = Settings_dot_Master_dot_EncounterSettings__pb2._ENCOUNTERSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['iap_item_display'].message_type = Settings_dot_Master_dot_IapItemDisplay__pb2._IAPITEMDISPLAY
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['iap_settings'].message_type = Settings_dot_Master_dot_IapSettings__pb2._IAPSETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['pokemon_upgrades'].message_type = Settings_dot_Master_dot_PokemonUpgradeSettings__pb2._POKEMONUPGRADESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.fields_by_name['equipped_badges'].message_type = Settings_dot_Master_dot_EquippedBadgeSettings__pb2._EQUIPPEDBADGESETTINGS
_DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE.containing_type = _DOWNLOADITEMTEMPLATESRESPONSE
_DOWNLOADITEMTEMPLATESRESPONSE.fields_by_name['item_templates'].message_type = _DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE
DESCRIPTOR.message_types_by_name['DownloadItemTemplatesResponse'] = _DOWNLOADITEMTEMPLATESRESPONSE

DownloadItemTemplatesResponse = _reflection.GeneratedProtocolMessageType('DownloadItemTemplatesResponse', (_message.Message,), dict(

  ItemTemplate = _reflection.GeneratedProtocolMessageType('ItemTemplate', (_message.Message,), dict(
    DESCRIPTOR = _DOWNLOADITEMTEMPLATESRESPONSE_ITEMTEMPLATE,
    __module__ = 'Networking.Responses.DownloadItemTemplatesResponse_pb2'
    # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.DownloadItemTemplatesResponse.ItemTemplate)
    ))
  ,
  DESCRIPTOR = _DOWNLOADITEMTEMPLATESRESPONSE,
  __module__ = 'Networking.Responses.DownloadItemTemplatesResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.DownloadItemTemplatesResponse)
  ))
_sym_db.RegisterMessage(DownloadItemTemplatesResponse)
_sym_db.RegisterMessage(DownloadItemTemplatesResponse.ItemTemplate)


# @@protoc_insertion_point(module_scope)
