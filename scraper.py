import argparse
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse


if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description='Download the clear album cover from Apple Music')
  parser.add_argument(
    'url', metavar='https://...', type=str, help='Apple music album URL')
  args = parser.parse_args()

  url = args.url
  unquote_url = urllib.parse.unquote(url)
  album = unquote_url.split('/')[-2]

  response = urllib.request.Request(url)
  res = urllib.request.urlopen(response)
  html = res.read().decode('utf-8')
  
  soup = BeautifulSoup(html, "html.parser")
  images = soup.findAll('img')

  for image in images:
    if image['class'][0] == 'product-lockup__artwork-for-radiosity-effect':
      target_image = image['src']
      target_image = target_image.replace('44x44br', '1500x1500')
      urllib.request.urlretrieve(target_image, album + ".png")
