#!/usr/local/bin/python3
__header__ = 'Content-type: text/html'
__html_head__ = '''
<head>
    <title>{0}</title>
    <meta charset='utf-8'>
    <style>
     {1}
    </style>
</head>
        '''
__base_td__ = '<tr><td><a href="{0}" target="_blank">{1} </a></td></tr>\n'


def get_header():
    return __header__


def get_html_head(title, style):
    return __html_head__.format(title, style)


def get_body_start():
    return '<body>'


def get_body_end():
    return '</body>'


def get_html_start():
    return '<html>'


def get_html_end():
    return '</html>'


def get_a_in_tr(title, link):
    return __base_td__.format(link, title)


def get_base_td():
    return __base_td__
