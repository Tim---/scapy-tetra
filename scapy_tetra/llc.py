#!/usr/bin/env python

# LLC PDUs

from scapy.packet import Packet, bind_layers
from scapy.fields import BitEnumField, BitField

from .mac import MAC_RESOURCE

# Table 307: BL-ADATA PDU without FCS contents
class BL_ADATA(Packet):
    name = 'BL ADATA (w/o FCS)'
    fields_desc = [
        BitField('nr', 0, 1),
        BitField('ns', 0, 1),
    ]

# Table 309: BL-DATA PDU without FCS contents
class BL_DATA(Packet):
    name = 'BL DATA (w/o FCS)'
    fields_desc = [
        BitField('ns', 0, 1),
    ]

# Table 311: BL-UDATA PDU without FCS contents
class BL_UDATA(Packet):
    name = 'BL UDATA (w/o FCS)'
    fields_desc = [
    ]

# Table 305: BL-ACK PDU without FCS contents
class BL_ACK(Packet):
    name = 'BL ACK (w/o FCS)'
    fields_desc = [
        BitField('nr', 0, 1),
    ]

# Table 308: BL-ADATA PDU with FCS contents
class BL_ADATA_FCS(Packet):
    name = 'BL ADATA (w/ FCS)'
    fields_desc = [
        BitField('nr', 0, 1),
        BitField('ns', 0, 1),
        # FIXME : add FCS field
    ]

# Figure 94: General format of an LLC header before the TL-SDU content
class LLC_PDU(Packet):
    name = 'LLC'
    fields_desc = [
        BitEnumField('llc_pdu_type', 0, 4, {
            0: 'BL-ADATA (w/o FCS)',
            1: 'BL-DATA (w/o FCS)',
            2: 'BL-UDATA (w/o FCS)',
            3: 'BL-ACK (w/o FCS)',
            4: 'BL-ADATA (w/ FCS)' # FIXME : other PDUs
        }),
    ]

bind_layers(MAC_RESOURCE, LLC_PDU)
bind_layers(LLC_PDU, BL_ADATA, llc_pdu_type=0)
bind_layers(LLC_PDU, BL_DATA, llc_pdu_type=1)
bind_layers(LLC_PDU, BL_UDATA, llc_pdu_type=2)
bind_layers(LLC_PDU, BL_ACK, llc_pdu_type=3)
bind_layers(LLC_PDU, BL_ADATA_FCS, llc_pdu_type=4)
