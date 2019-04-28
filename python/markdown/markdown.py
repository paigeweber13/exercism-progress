"""
converts markdown to html
"""

import re

def check_for_headings(line):
    """
    converts lines which are headings to html, returns the new line
    if line is not a heading, returns line unchanged.
    """
    result = line
    match = re.match('(?P<num_hash>#+)', line)
    if match:
        heading_level = len(match.group('num_hash'))
        result = '<h' + str(heading_level) + '>' + line[heading_level + 1:] \
            + '</h' + str(heading_level) + '>'
    return result

def check_for_bold(line):
    """
    converts bold sections to html 'strong', returns changed line
    """
    result = line
    match = re.match('(.*)__(.*)__(.*)', line)
    if match:
        result = match.group(1) + '<strong>' + \
            match.group(2) + '</strong>' + match.group(3)
    return result

def check_for_italics(line):
    """
    converts italics sections to html 'em', returns changed line
    """
    result = line
    match = re.match('(.*)_(.*)_(.*)', line)
    if match:
        result = match.group(1) + '<em>' + match.group(2) + \
            '</em>' + match.group(3)
    return result

def start_list(line):
    """
    starts a list by adding <ul> tag
    """
    return '<ul>' + line

def add_list_item(list_item):
    """
    surrounds line in <li> tags
    """
    return '<li>' + list_item + '</li>'

def end_list(line):
    """
    ends line by appending </ul>
    """
    return line + '</ul>'

def add_p_tag(line):
    """
    surrounds line by p
    """
    return '<p>' + line + '</p>'

def parse_markdown(markdown):
    """
    checks for all markdown; calls other functions
    """
    result = ''
    in_list = False

    for line in markdown.split('\n'):
        line = check_for_bold(line)
        line = check_for_italics(line)
        line = check_for_headings(line)

        match = re.match(r'\* (.*)', line)
        if match:
            line = match.group(1)
            if not in_list:
                line = add_list_item(line)
                line = start_list(line)
                in_list = True
            else:
                line = add_list_item(line)

        else:
            if in_list:
                line = end_list(line)
                in_list = False

        match = re.match(r'<h|<ul|<li', line)
        if match is None:
            line = add_p_tag(line)
        result += line

    if in_list:
        result = end_list(result)
    return result
