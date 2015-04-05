#!/usr/bin/env python

# MAC PDUs without the type fields (see mac_types.py)

from scapy.packet import Packet, bind_layers

from .gsmtap import GSMTAP
from .mac_header import MAC_UL, MAC_DL, MAC_SCH_HU

# Tables 338/339
class ACCESS_ASSIGN(Packet):
    name = 'ACCESS-ASSIGN'
    
    fields_desc = [
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
