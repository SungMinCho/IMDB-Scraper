import pandas as pd


df = pd.read_csv('file.csv')
DONE = set([s[:-1] for s in df.imdb_url])
