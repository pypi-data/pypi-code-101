import torch
import torch.nn as nn

from . import decoders
from . import encoders
from . import ops
from .decoders import RES_SHORTCUT_DECODER_22
from .encoders import RES_SHORTCUT_ENCODER_29


class Generator(nn.Module):
    def __init__(self, encoder=RES_SHORTCUT_ENCODER_29, decoder=RES_SHORTCUT_DECODER_22):

        super(Generator, self).__init__()

        if encoder not in encoders.__all__:
            raise NotImplementedError("Unknown Encoder {}".format(encoder))
        self.encoder = encoders.__dict__[encoder]()

        self.aspp = ops.ASPP(in_channel=512, out_channel=512)

        if decoder not in decoders.__all__:
            raise NotImplementedError("Unknown Decoder {}".format(decoder))
        self.decoder = decoders.__dict__[decoder]()

    def forward(self, image, guidance):
        inp = torch.cat((image, guidance), dim=1)
        embedding, mid_fea = self.encoder(inp)
        embedding = self.aspp(embedding)
        pred = self.decoder(embedding, mid_fea)

        return pred
