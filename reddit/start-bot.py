import praw
from wonderwords import RandomSentence
from termcolor import colored
import time
import sys
import os

def submit(delete=False):

    reddit = praw.Reddit(client_id ='',
                        client_secret ='',
                        user_agent ='',
                        username ='',
                        password ='')

    subreddit = reddit.subreddit('u_four-word-sentence')
    reddit.validate_on_submit = True

    random_four_word_sentence = RandomSentence()
    four_word_sentence = random_four_word_sentence.simple_sentence()

    submission = subreddit.submit(title=four_word_sentence, selftext='')
    print(colored('[TIMESTAMP]: ', 'cyan') + colored(time.ctime(), 'magenta'))
    print(colored('[TITLE]: ', 'cyan') + colored(f'{submission.title}\n', 'magenta'))

    if delete == True:

        submission.delete()

if __name__ == '__main__':

    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored('\n-------------------------\nfour-word-sentence.py v0.2 beta\n\nby critiqalfish\n-------------------------\n', 'red', attrs=['bold']))

    while True:

        time.sleep(600 - time.time() % 600)

        submit()
