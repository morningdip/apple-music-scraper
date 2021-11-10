import argparse
import string
from bs4 import BeautifulSoup
import urllib.request
import re


if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description='Download the clear album cover from Apple Music')
  parser.add_argument(
    'url', metavar='https://...', type=str, help='Apple music album URL')
  args = parser.parse_args()

  url = args.url

  if re.findall(r'[\u4e00-\u9fff]+', url):
    album = args.url.split('/')[-2]
    url = urllib.parse.quote(url, safe=string.printable)
  else:
    unquote_url = urllib.parse.unquote(url)
    album = unquote_url.split('/')[-2]

  result = urllib.request.urlopen(url)
  html = result.read().decode('utf-8')
  soup = BeautifulSoup(html, "html.parser")
  images = soup.findAll('img')

  for image in images:
    if image['class'][0] == 'product-lockup__artwork-for-radiosity-effect':
      target_image = image['src']
      target_image = target_image.replace('44x44br', '1500x1500')
      urllib.request.urlretrieve(target_image, album + ".png")
