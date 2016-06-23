from .general import is_iterable

import pymel.core as pm


# -- Colour constants
_colour_map = (
    (0, 'default', (0.27, 0.27, 0.27)),
    (1, 'black', (0, 0, 0)),
)


def validate_colour(colour):
    """
    Return a valid colour index for Maya.

    :param colour: Colour to validate.
    :type colour: int / str / rgb (list / tuple)

    :return: Valid colour index
    :rtype: int
    """
    return colour


def set_colour(node_list, colour):
    """
    Set override colour to given nodes.

    :param node_list: Nodes to apply colour override on.
    :type node_list: list
    :param colour: Colour value to apply.
    :type colour: int / str / rgb (tuple / list)

    :return: None
    :rtype: None
    """
    # -- Get a valid iterable
    if not is_iterable(node_list):
        node_list = [node_list]

    for node in node_list:
        node.overrideEnabled.set(True)
        node.overrideColor(colour)


def set_colour_shapes(node_list, colour):
    """
    Set override colour for shapes.

    :param node_list: Nodes to apply colour override on.
    :type node_list: list
    :param colour: Colour value to apply.
    :type colour: int / str / rgb (tuple / list)

    :return: None
    :rtype: None
    """
    # -- Get a valid iterable
    if not is_iterable(node_list):
        node_list = [node_list]

    shape_list = []

    for node in node_list:
        try:
            shape_list.extend(node.getShapes())
        except RuntimeError:
            shape_list.append(node)

    if shape_list:
        set_colour(node_list=shape_list,
                   colour=colour)
