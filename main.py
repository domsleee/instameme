from PIL import Image
import requests
from io import BytesIO
import json
import argparse
import pytesseract

def main(args):
  print('meme')
  obj = parse_json(args.json)
  for entry in obj:
    url = entry['node']['display_url']
    print(url, image_to_text(url))


def parse_json(file):
  with open(file) as f:
    data = json.load(f)
  return data


def image_to_text(url):
  response = requests.get(url)
  img = Image.open(BytesIO(response.content))
  return pytesseract.image_to_string(img, lang='eng')


if __name__ == '__main__':
  parser = argparse.ArgumentParser('cool')
  parser.add_argument('json', help='json file to parse')
  main(parser.parse_args())



#./main.py <JSON>
