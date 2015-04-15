#!/usr/bin/env python

# Text message transfer SDU

from scapy.packet import Packet, bind_layers
from scapy.fields import BitField, ConditionalField

from .sdstl import SDS_TRANSFER

# Table 446: Text message transfer SDU contents
class TEXT_MESSAGE_TRANSFER(Packet):
    name = 'Text Message Transfer SDU'
    fields_desc = [
        BitField('tstp_used', 0, 1),
        BitField('text_coding', 0, 7),
        ConditionalField(BitField('timestamp', 0, 24), lambda pkt: pkt.tstp_used == 1),
    ]

# FIXME : this is just wrong. We should rely on the value of D_SDS_DATA.proto
# but Scapy does not allow us to use the fields of an "ancestor" layer.
bind_layers(SDS_TRANSFER, TEXT_MESSAGE_TRANSFER)
