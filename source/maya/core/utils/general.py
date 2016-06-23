

def is_iterable(iter):
    """
    Conenience function to check if object is iterable.

    :param iter: Object to check is iterable.
    :type iter: any

    :return: Whether its iterable.
    :rtype: bool
    """
    return isinstance(iter,
                      (list, tuple))
