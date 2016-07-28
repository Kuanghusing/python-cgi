#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import requests
import re
import html_helper
import io
import sys


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
style = '''body{
            width: 650px;
        margin: 200px auto;
        font-size: 25px;
      }
      #content{
        margin: 50px 0
      }
      #header{
          width: 460px;
          margin: 0px auto;
          height: 100px;
      }
      #header{
          text-align: center;
      }
      .py{
         font-family:monospace;
          text-align:center;
          margin:50px auto;
      }
'''
main_content = '''
                <div id="header">
          <form action="search_result.py">
          <div style="border:2px solid #ccc;border-radius:4px;float:left">
              <input type="text" id="movie_name" name="keyword" style="border:0px;line-height:2;padding:2px;width:400px" placeholder="life is short, search by python"/>
          </div>
              <input type="submit" value="search" style="border:0px;float:right;margin-top:8px"/>
          </form>
      </div>


        <div id="content">
          <table>
              {0}
          </table>
          <div class="py">From Python to trade</div>
          <div class="py">print(\'\'\'Life is short, I use Python\'\'\')</div>
      </div>
'''
base_url_mp4ba = 'http://www.mp4ba.com/'
movie_list = []


def get_html(url):
    req = requests.get(url)
    return req.text


def solve_movie_item(html):
    soup = BeautifulSoup(html, 'html.parser')
    a_movie = soup('a', href=re.compile('^show.php\?hash'))
    for item in a_movie:
        link = base_url_mp4ba + item['href']
        title = item.string
        movie_list.append((link, title))


def write_html(l):
    print(html_helper.get_header())
    print()
    print(html_helper.get_html_head('Search Movie', style))
    print(html_helper.get_body_start())
    all_td = ''
    for item in l:
        all_td += html_helper.get_base_td().format(item[0], item[1])
    print(main_content.format(all_td))
    print(html_helper.get_body_end())
    print(html_helper.get_html_end())


if __name__ == '__main__':
    solve_movie_item(get_html(base_url_mp4ba))
    write_html(movie_list)
