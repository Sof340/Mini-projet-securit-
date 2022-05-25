import tweepy
from time import sleep

# ici on import les information saisi dans cred
from cred import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

my_file=open('texte.txt','r')
file_lines=my_file.readlines()
my_file.close()

# on cree une loop pour toutes les lines 
for line in file_lines:
  
    try:
        print(line)
        # on ajoute if pour eviter les espace blancs
        if line != '\n':
            api.update_status(line)

        # on ajoute else avec pass pour terminer la commande
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    sleep(10)
