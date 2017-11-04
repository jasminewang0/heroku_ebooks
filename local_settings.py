'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = '9Gh6P0tYP12fe9oRw2jd44S9m'
MY_CONSUMER_SECRET = 'kIHwBge5Mo1T4EePaIkT0JcIQcxLRvQqGxjTuNb28oHW4cNj06'
MY_ACCESS_TOKEN_KEY = '920124656853581826-ccy0j3Q8f11d6DYs6HjdrawzzegaHiq'
MY_ACCESS_TOKEN_SECRET = 'hCbeJPWJuyAnw7IaFYV1xcPBu1r0O6oyCxms1qhTNf9wZ'

SOURCE_ACCOUNTS = ["beemovie_bot"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 1 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 2 is low and 4 is high.
SOURCE_EXCLUDE = r'^$' #Source tweets that match this regexp will not be added to the Markov chain. You might want to filter out inappropriate words for example.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "issabeebot" #The name of the account you're tweeting to.
