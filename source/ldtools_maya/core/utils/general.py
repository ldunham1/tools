

def is_iterable(iterable):
    """
    Convenience function to check if object is iterable.

    :param iterable: Object to check is iterable.
    :type iterable: any

    :return: Whether its iterable.
    :rtype: bool
    """
    # -- At the moment we only care about lists and tuples
    return isinstance(iterable,
                      (list, tuple))
