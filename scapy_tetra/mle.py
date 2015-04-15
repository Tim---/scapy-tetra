#!/usr/bin/env python

# MLE PDUs

from scapy.packet import Packet, bind_layers
from scapy.fields import BitEnumField

from .llc import BL_ADATA, BL_DATA, BL_UDATA, BL_ACK, BL_ADATA_FCS

# Table 220: MLE service PDU layout
class MLE_PDU(Packet):
    name = 'MLE'
    fields_desc = [
        BitEnumField('protocol_discriminator', 0, 3, {
            1: 'MM',
            2: 'CMCE',
            4: 'SNDCP',
            5: 'MLE',
            6: 'TETRA Management entity',
        }),
    ]

# FIXME : create Scapy classes for Type 1, 2, 3 and 4 fields underlying protocols
#         refer to section 'E.2 PDU encoding rules for MLE PDUs'

bind_layers(BL_ADATA, MLE_PDU)
bind_layers(BL_DATA, MLE_PDU)
bind_layers(BL_UDATA, MLE_PDU)
bind_layers(BL_ACK, MLE_PDU)
bind_layers(BL_ADATA_FCS, MLE_PDU)
