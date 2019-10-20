import pandas as pd


df = pd.read_csv('links.csv')
df['url'] = df.imdbId.map(lambda s: 'https://www.imdb.com/title/tt0' + str(s))

with open('urllist.py', 'w') as f:
  f.write('URLLIST = [\n')
  for url in df['url']:
    f.write("  '" + url + "',\n")
  f.write("]\n")
