from .constants import * # Relative file containing constants

import copy
import json
import logging


# -- Setup Logger
log = logging.getLogger(LOGGER_NAME)
log.setLevel(logging.INFO)


def configure_dict_config(file_data):
    """
    Configure and validate logging dictConfig data.
    This allows us to configure the dict config data, allowing user specific
    logging events.

    :param file_data: Dict config to configure and validate.
    :type: dict

    :return: dict
    """
    # -- Essentially we want to get all of the data, then check if the user is
    # -- specified to use particulars (log debug to filepath). If so then we
    # -- alter the data to reflect the settings for the user.

    # -- Validate data type
    if not isinstance(file_data, dict):
        raise TypeError('File data is not a dictionary: %s ' % file_data)
        return

    # -- Copy given data to configure for a return value
    config_data = copy.deepcopy(file_data)

    # -- Check for user specific logging events
    if 'users' in config_data:

        # -- Pull the unsupported data out
        users_data = config_data.pop('users')

        # -- Get data specifically for user
        user_data = users_data.get(USER)
        if user_data:

            # -- Configure the data from the user's specifications
            # -- We can expect; levels, handlers, loggers
            loggers = config_data.get('loggers')
            if loggers:

                update_data = {}

                # -- Here we specify the extra data we'll want to use
                # -- Levels
                if 'level' in user_data:
                    update_data['level'] = user_data['level']

                # -- Handlers
                if 'handlers' in user_data:
                    update_data['handlers'] = user_data['handlers']

                # -- If any data is specified, edit all loggers to use
                for key in loggers:
                    config_data['loggers'][key].update(update_data)

    return config_data


def load():
    """
    Load configured logging config data.

    :return: None
    """
    # if os.path.isfile(LOGGING_CONFIG):
    # -- Get config data from file
    with open(LOGGING_CONFIG, 'r') as f:

        file_data = json.loads(f.read())
        config_dict = configure_dict_config(file_data)

    if config_dict:
        logging.dictConfig(config_dict)

    else:
