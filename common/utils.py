
def replace_multiple(old_string: str, searches: list, replacements: list) -> str:
    '''Replace multiple values at once

    Args:
        old_string (str): not modified string
        searches (list): strings for being modified
        replacements (list): strings for being replaced
    
    Raises:
        ValueError: if the number of searches doesn't match the number of replacements
    
    Returns:
        Modified string
    '''
    if len(searches) != len(replacements):
        raise ValueError('The number of searches must be the same as the one of replacements!')

    for k, s in enumerate(searches):
        old_string = old_string.replace(s, replacements[k])
    
    return old_string