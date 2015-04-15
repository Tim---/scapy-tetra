#!/usr/bin/env python

# GSMTAP dissector
# The reference implementation is located at :
# http://cgit.osmocom.org/libosmocore/tree/include/osmocom/core/gsmtap.h

from scapy.packet import Packet, bind_layers
from scapy.fields import ByteField, ByteEnumField, BitField, IntField, ConditionalField
from scapy.layers.inet import UDP

class GSMTAP(Packet):
    name = 'GSMTAP'
    
    fields_desc = [
        ByteField('version', 2),
        ByteField('hdr_len', 4),
        ByteEnumField('type', 0, {
            0x01: 'UM',
            0x02: 'ABIS',
            0x03: 'UM BURST',
            0x04: 'SIM',
            0x05: 'TETRA I1',
            0x06: 'TETRA I1 BURST',
            0x07: 'WMX BURST',
            0x08: 'GB LLC',
            0x09: 'GB SNDCP',
            0x0a: 'GMR1 UM',
            0x0b: 'UMTS RLC MAC',
            0x0c: 'UMTS RRC',
            0x0d: 'LTE RRC',
            0x0e: 'LTE MAC'
        }),
        ByteField('timeslot', 0),
        BitField('flag_pcs', 0, 1),
        BitField('flag_uplink', 0, 1),
        BitField('arfcn', 0, 14),
        ByteField('signal_dbm', 0),
        ByteField('snr_db', 0),
        IntField('frame_number', 0),
        ConditionalField(ByteField('sub_type', 0), lambda pkt: pkt.type != 0x05),
        ConditionalField(ByteEnumField('sub_type', 0, {
            0: 'Unknown',
            1: 'BSCH',
            2: 'AACH',
            3: 'SCH/HU',
            4: 'SCH/HD',
            5: 'SCH/F',
            6: 'BNCH',
            7: 'STCH',
            8: 'TCH/F'
        }), lambda pkt: pkt.type == 0x05),
        ByteField('antenna_nr', 0),
        ByteField('sub_slot', 0),
        ByteField('res', 0),
    ]

bind_layers(UDP, GSMTAP, dport=4729)
