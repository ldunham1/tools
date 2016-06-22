from .general import is_iterable

import pymel.core as pm
import logging


# -- Setup logger
log = logging.getLogger('ldtools.core.utils.skin')
log.setLevel(logging.INFO)


def get_skin_clusters(node_list):
    """
    Return all associated skinCluster nodes.

    :param node_list: Nodes to check for skinClusters
    :type node_list: list / tuple

    :return: Associated skinClusters.
    :rtype: list
    """
    # -- Get a valid iterable
    if not is_iterable(node_list):
        node_list = [node_list]

    results = []
    for node in node_list:
        # -- Get any skinClusters from mesh history
        # -- Get any skinClusters from joint connections
        results.extend([sk for
                        sk in set(node.listHistory(type='skinCluster') or
                                  node.listConnections(type='skinCluster')) if
                        sk not in results])

    return results


def set_move_joints_mode(node_list, state):
    """
    Set the move joints mode state to all connected skinClusters.

    :param node_list: Nodes to set associated skinCluster states on.
    :type node_list: list / tuple
    :param state: Enable/disable moveJointsMode
    :type state: bool

    :return: None
    :rtype: None
    """
    # -- Get the connected skinClusters
    skin_clusters = get_skin_clusters(node_list)

    if skin_clusters:

        # -- Set the move joints node
        for skin in skin_clusters:
            skin.moveJointsMode(state)

    else:
        log.warning('No skinClusters found.')


def enable_move_joints_mode(node_list=None):
    """
    Convenience function to enable move joints mode to all connected skinClusters.

    :param node_list: Nodes to apply on. Use scene selection by default.
    :type node_list: list / tuple / None

    :return: None
    :rtype: None
    """
    # -- Get a valid node list from arg or scene selection
    node_list = node_list or pm.selected()

    # -- Enable move joints mode
    if node_list:
        set_move_joints_mode(node_list=node_list,
                             state=True)
    else:
        log.warning('No nodes to apply on.')


def disable_move_joints_mode(node_list=None):
    """
    Convenience function to disable move joints mode to all connected skinClusters.

    :param node_list: Nodes to apply on. Use scene selection by default.
    :type node_list: list / tuple / None

    :return: None
    :rtype: None
    """
    # -- Get a valid node list from arg or scene selection
    node_list = node_list or pm.selected()

    # -- Disable move joints mode
    if node_list:
        set_move_joints_mode(node_list=node_list,
                             state=False)
    else:
        log.warning('No nodes to apply on.')
