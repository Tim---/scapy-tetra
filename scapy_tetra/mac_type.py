#!/usr/bin/env python

# Fields differentiating between several MAC PDU types

from scapy.packet import Packet, bind_layers
from scapy.fields import BitEnumField, ConditionalField

from .gsmtap import GSMTAP

# Table 321: MAC PDU types for SCH/F, SCH/HD, STCH and BSCH
class MAC_DL(Packet):
    name = 'MAC (downlink)'
    
    fields_desc = [
        BitEnumField('type', 0, 2, {
            0: 'MAC-RESOURCE',
            1: 'MAC-FRAG or MAC-END',
            2: 'Broadcast',
            3: 'MAC-U-SIGNAL'
        }),
        ConditionalField(BitEnumField('subtype', 0, 1, {
            0: 'MAC-FRAG',
            1: 'MAC-END',
        }), lambda pkt: pkt.type == 1),
        ConditionalField(BitEnumField('subtype', 0, 2, {
            0: 'SYSINFO',
            1: 'ACCESS-DEFINE',
        }), lambda pkt: pkt.type == 2),
    ]

# Table 321: MAC PDU types for SCH/F, SCH/HD, STCH and BSCH
class MAC_UL(Packet):
    name = 'MAC (uplink)'
    
    fields_desc = [
        BitEnumField('type', 0, 2, {
            0: 'MAC-DATA',
            1: 'MAC-FRAG or MAC-END',
            3: 'MAC-U-SIGNAL',
        }),
        ConditionalField(BitEnumField('subtype', 0, 1, {
            0: 'MAC-FRAG',
            1: 'MAC-END',
        }), lambda pkt: pkt.type == 1),
    ]

# Table 322: MAC PDU types for SCH/HU
class MAC_SCH_HU(Packet):
    name = 'MAC (uplink, SCH/HU)'
    
    fields_desc = [
        BitEnumField('type', 0, 1, {
            0: 'MAC-ACCESS',
            1: 'MAC-END-HU',
        }),
    ]

# SCH/F, SCH/HD, STCH, BNCH (downlink) -> MAC_Downlink
bind_layers(GSMTAP, MAC_DL, flag_uplink=0, sub_type=5)
bind_layers(GSMTAP, MAC_DL, flag_uplink=0, sub_type=4)
bind_layers(GSMTAP, MAC_DL, flag_uplink=0, sub_type=7)
bind_layers(GSMTAP, MAC_DL, flag_uplink=0, sub_type=6)
# SCH/F, SCH/HD, STCH, BNCH (uplink) -> MAC_Uplink
bind_layers(GSMTAP, MAC_UL, flag_uplink=1, sub_type=5)
bind_layers(GSMTAP, MAC_UL, flag_uplink=1, sub_type=4)
bind_layers(GSMTAP, MAC_UL, flag_uplink=1, sub_type=7)
bind_layers(GSMTAP, MAC_UL, flag_uplink=1, sub_type=6)
# SCH/HU (uplink) -> MAC_SCH_HU
bind_layers(GSMTAP, MAC_SCH_HU, flag_uplink=1, sub_type=3)

