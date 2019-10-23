import pandas as pd


def to_link(s):
  return 'tt' + ('0' * (7 - len(s)) + s)

df = pd.read_csv('links.csv')
df['url'] = df.imdbId.map(lambda s: 'https://www.imdb.com/title/' + to_link(str(s)))

with open('urllist.py', 'w') as f:
  f.write('URLLIST = [\n')
  for url in df['url']:
    f.write("  '" + url + "',\n")
  f.write("]\n")
