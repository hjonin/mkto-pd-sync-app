from re import compile, search


def simple_pluralize(word):
    """
    Simply pluralize word by adding an extra 's' at the end
    taking into account some exceptions.
    >>> simple_pluralize('lead')
    'leads'
    >>> simple_pluralize('opportunity')
    'opportunities'
    """
    plural = word
    if word.endswith('y'):
        plural = plural[:-1] + 'ie'
    plural += 's'
    return plural


def is_marketo_guid(id):
    """
    Return True if the given id is a Marketo GUID, False otherwise.
    >>> is_marketo_guid('6a38a3bd-edce-4d86-bcc0-83f1feef8997')
    True
    >>> is_marketo_guid('7591021')
    False
    """
    p = compile('[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}')
    return p.match(str(id))


def compute_external_id(pd_resource_name, id_, prefix='pd'):
    return prefix + '-' + pd_resource_name + '-' + str(id_)


def get_id_part_from_external(external_id):
    """
        Return True if the given id is a Marketo GUID, False otherwise.
        >>> get_id_part_from_external('pd-organization-1234')
        '1234'
        >>> get_id_part_from_external('pd')
        ''
        >>> get_id_part_from_external('pd-pd')
        ''
        """
    ret = ''
    match = search(r'-(\d*)$', external_id)
    if match:
        ret = match.group(1)
    return ret


if __name__ == '__main__':
    import doctest
    doctest.testmod()