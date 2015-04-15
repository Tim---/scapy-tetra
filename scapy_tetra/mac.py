#!/usr/bin/env python

# MAC PDUs without the type fields (see mac_types.py)

from scapy.packet import Packet, bind_layers
from scapy.fields import BitField, ConditionalField

from .gsmtap import GSMTAP
from .mac_type import MAC_UL, MAC_DL, MAC_SCH_HU

# Tables 338/339
class ACCESS_ASSIGN(Packet):
    name = 'ACCESS-ASSIGN'
    
    fields_desc = [
        BitField('header', 0, 2),
        BitField('field1', 0, 6),
        BitField('field2', 0, 6),
    ]

# Table 336
class ACCESS_DEFINE(Packet):
    name = 'ACCESS-DEFINE'
    
    fields_desc = [
    ]

# Table 323
class MAC_ACCESS(Packet):
    name = 'MAC-ACCESS'
    
    fields_desc = [
    ]

# Table 325
class MAC_END_HU(Packet):
    name = 'MAC-END-HU'
    
    fields_desc = [
    ]

# Table 326
class MAC_DATA(Packet):
    name = 'MAC-DATA'
    
    fields_desc = [
    ]

# Table 329
class MAC_RESOURCE(Packet):
    name = 'MAC-RESOURCE'
    
    fields_desc = [
        BitField('fill_bits', 0, 1),
        BitField('grant', 0, 1),
        BitField('encrypt', 0, 2),
        BitField('random_access', 0, 1),
        BitField('length', 2, 6),
        BitField('address_type', 1, 3),
        ConditionalField(BitField('address', 0, 24), lambda pkt: pkt.address_type not in [0, 2]),
        ConditionalField(BitField('event_label', 0, 10), lambda pkt: pkt.address_type in [2, 5, 7]),
        ConditionalField(BitField('usage_marker', 0, 6), lambda pkt: pkt.address_type == 6),
        BitField('pwr_ctl_flag', 0, 1),
        ConditionalField(BitField('pwr_ctl', 0, 4), lambda pkt: pkt.pwr_ctl_flag == 1),
        BitField('slot_grt_flag', 0, 1),
        ConditionalField(BitField('slot_grt', 0, 8), lambda pkt: pkt.slot_grt_flag == 1),
        BitField('chan_alloc_flag', 0, 1),
        # FIXME : channel allocation element (Table 341),
    ]

# Table 330
class MAC_FRAG_DL(Packet):
    name = 'MAC-FRAG (downlink)'
    
    fields_desc = [
    ]

# Table 327
class MAC_FRAG_UL(Packet):
    name = 'MAC-FRAG (uplink)'
    
    fields_desc = [
    ]

# Table 331
class MAC_END_DL(Packet):
    name = 'MAC-END (downlink)'
    
    fields_desc = [
    ]

# Table 328
class MAC_END_UL(Packet):
    name = 'MAC-END (uplink)'
    
    fields_desc = [
    ]

# No table : traffic data
class MAC_TRAFFIC(Packet):
    name = 'MAC-TRAFFIC'
    
    fields_desc = [
    ]

# Table 337
class MAC_U_SIGNAL(Packet):
    name = 'MAC-U-SIGNAL'
    
    fields_desc = [
    ]

# Table 335
class SYNC(Packet):
    name = 'SYNC'
    
    fields_desc = [
    ]

# Table 333
class SYSINFO(Packet):
    name = 'SYSINFO'
    
    fields_desc = [
    ]


# Table 348: Mapping of the MAC PDU onto the logical channels

# ACCESS-ASSIGN
bind_layers(GSMTAP, ACCESS_DEFINE, flag_uplink=0, sub_type=2)
# ACCESS-DEFINE
bind_layers(MAC_DL, ACCESS_DEFINE, type=2, subtype=1)
# MAC-ACCESS
bind_layers(MAC_SCH_HU, MAC_ACCESS, type=0)
# MAC-END-HU
bind_layers(MAC_SCH_HU, MAC_END_HU, type=1)
# MAC-DATA
bind_layers(MAC_UL, MAC_DATA, type=0)
# MAC-RESOURCE
bind_layers(MAC_DL, MAC_RESOURCE, type=0)
# MAC-FRAG
bind_layers(MAC_UL, MAC_FRAG_UL, type=1, subtype=0)
bind_layers(MAC_DL, MAC_FRAG_DL, type=1, subtype=0)
# MAC-END
bind_layers(MAC_UL, MAC_END_UL, type=1, subtype=1)
bind_layers(MAC_DL, MAC_END_DL, type=1, subtype=1)
# MAC-TRAFFIC
bind_layers(GSMTAP, MAC_TRAFFIC, sub_type=8)
# MAC-U-SIGNAL
bind_layers(MAC_UL, MAC_U_SIGNAL, type=3)
bind_layers(MAC_DL, MAC_U_SIGNAL, type=3)
# SYNC
bind_layers(GSMTAP, SYNC, sub_type=1)
# SYSINFO
bind_layers(MAC_DL, ACCESS_DEFINE, type=2, subtype=0)
