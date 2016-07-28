#!/usr/local/bin/python3
import sys
import io
import requests
import re
from bs4 import BeautifulSoup
import html_helper

import cgi

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

base_url_mp4ba = 'http://www.mp4ba.com'
get_url = '/search.php'
field = cgi.FieldStorage()
keyword = field.getvalue('keyword')
style = '''body{
      width: 600px;
      margin: 100px auto;
      font-size: 25px;
    }
    #content{
      margin: 50px 0
    }
	.keyword{
	background:#ff0;
	}
        '''
html_main_content = '''<div style="font-family:monospace;font-size:34px;text-align:center;margin:50px;">Life is SHORT!! Let's use <span style="font-size:50px">Python!!</span></div><div id="content">
        <table>
            {0}
        </table>
    </div>'''
result_list = []


def get_html(p):
    req = requests.get(base_url_mp4ba + get_url, params=p)
    # print(req.url)
    return req.text


def solve_movie_item(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_result = soup('a', href=re.compile('^show.php\?hash'))
    movie_list = []
    for result_item in all_result:
        link = base_url_mp4ba + result_item['href']
        title = str(result_item.contents[1]) + str(result_item.contents[2])
        movie_list.append((link, title))
    return movie_list


if __name__ == '__main__':
    # keyword = '复仇者'
    params = {'keyword': keyword}
    result_list = solve_movie_item(get_html(params))
    print(html_helper.get_header())
    print()
    print(html_helper.get_html_head('Result', style))
    print(html_helper.get_body_start())
    td_list = ''
    for item in result_list:
        td_list += html_helper.get_base_td().format(item[0], item[1])
    print(html_main_content.format(td_list))
    print(html_helper.get_body_end())
    print(html_helper.get_html_end())
