#!/usr/bin/env python

# CMCE PDUs

from scapy.packet import Packet, bind_layers
from scapy.fields import BitField, BitEnumField, ConditionalField

from .cmce import D_SDS_DATA

# Table 446: Text message transfer SDU contents
class SDS_TRANSFER(Packet):
    name = 'SDS-Transfer'
    fields_desc = [
        BitField('delivery_report_request', 0, 2),
        BitField('short_form_report', 0, 1),
        BitField('storage', 0, 1),
        BitField('message_ref', 0, 8),
        ConditionalField(BitField('validity_period', 0, 5), lambda pkt: pkt.storage == 1),
        ConditionalField(BitField('fwd_addr_type', 0, 5), lambda pkt: pkt.storage == 1),
        # FIXME : More conditionnal fields
    ]

# Table 428: PDU layout
class SDS_TL_PDU(Packet):
    name = 'SDS-TL'
    fields_desc = [
        BitEnumField('message_type', 0, 4, {
            0: 'SDS-TRANSFER'
        }),
    ]

# Table 439: Protocol identifier information element contents
# FIXME : SDS-TL is only used for protocols >=128 (except 134...)
bind_layers(D_SDS_DATA, SDS_TL_PDU, proto=130)
bind_layers(SDS_TL_PDU, SDS_TRANSFER, message_type=0)
