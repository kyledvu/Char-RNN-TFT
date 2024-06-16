import pandas as pd

tweets = pd.read_csv('rawText/rayditzfn_tweets.csv')
tweets['text'].to_csv('rayditz_tweets_text.txt', index=False, header=False)