#!/usr/bin/env python

# CMCE PDUs

from scapy.packet import Packet, bind_layers
from scapy.fields import BitField, BitEnumField, ConditionalField, BitFieldLenField

from .mle import MLE_PDU

# Table 70: D-STATUS PDU contents
class D_STATUS(Packet):
    name = 'D-STATUS'
    fields_desc = [
        BitField('calling_type_ident', 0, 2),
        BitField('calling_address', 0, 24),
        BitField('precoded_status', 0, 16),
        # Fixme : other fields
    ]

# Table 69: D-SDS-DATA PDU contents
class D_SDS_DATA(Packet):
    name = 'D-SDS-DATA'
    fields_desc = [
        BitField('calling_type_ident', 0, 2),
        BitField('calling_address', 0, 24),
        BitField('sdti', 0, 2),
        ConditionalField(BitFieldLenField('length', 0, 11, length_of="data4"), lambda pkt: pkt.sdti == 3),
        ConditionalField(BitField('proto', 0, 8), lambda pkt: pkt.sdti == 3),
        # FIXME : differentiate data1, data2, data3, data4 and extract padding
    ]

# Section 14.7: PDU descriptions
class CMCE_PDU(Packet):
    name = 'CMCE'
    fields_desc = [
        BitEnumField('pdu_type', 0, 5, {
            15: 'D-SDS-DATA'
        }),
    ]

bind_layers(MLE_PDU, CMCE_PDU, protocol_discriminator=2)
bind_layers(CMCE_PDU, D_SDS_DATA, pdu_type=15)
