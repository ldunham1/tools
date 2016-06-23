"""

"""
from .constants import *

import pymel.core as pm
import logging


# -- Constants
LOGGER_NAME = '%s.%s' % (LOGGER_NAME,
                         __name__)

# -- Setup log object
log = logging.getLogger(LOGGER_NAME)


# -----------------------------------------------------------------------------
class UndoChunk(object):
    """
    Context manager to wrap an Undo Chunk.
    """

    def __enter__(self):
        pm.undoInfo(openChunk=True)
        log.debug('Undo chunk opened.')

    def __exit__(self, exc_type, exc_val, exc_tb):
        pm.undoInfo(closeChunk=True)
        log.debug('Undo chunk closed.')

        if exc_type:
            log.exception('%s : %s' % (exc_type,
                                       exc_val))

        # If this was false, it would re-raise the exception when complete
        return True
