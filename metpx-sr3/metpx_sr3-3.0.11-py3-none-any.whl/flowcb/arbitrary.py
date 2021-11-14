import logging
from sarracenia.flowcb import FlowCB

logger = logging.getLogger(__name__)


class Arbitrary(FlowCB):
    def __init__(self, options):

        # FIXME: should a logging module have a logLevel setting?
        #        just put in a cookie cutter for now...
        if hasattr(options, 'logLevel'):
            logger.setLevel(getattr(logging, options.logLevel.upper()))
        else:
            logger.setLevel(logging.INFO)

    def after_accept(self, worklist):
        new_incoming=[]
        for msg in worklist.incoming:
            if msg['integrity']['method'] == 'arbitrary':
                logger.warning('Good!')
                new_incoming.append(msg)
            else:
                logger.warning('rejecting! %s' % msg['integrity'])
                worklist.rejected.append(msg)
        worklist.incoming=new_incoming
