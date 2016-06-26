from ...constants import *

import os.path


LOGGER_NAME = '%s.%s' %(LOGGER_NAME,
                        __package__)

LOGGING_ROOT = os.path.join(RESOURCE_ROOT,
                            'logging')
LOGGING_CONFIG = os.path.join(LOGGING_ROOT,
                              'logging_config.json')
