from github import Github
import random
import time
import os
from dotenv import load_dotenv
from termcolor import colored

# Load variables from .env file
load_dotenv()

# Access the ACCESS_KEY variable
access_key = os.getenv('ACCESS_KEY')


# Authenticate with Github using an access token or username/password
g = Github(access_key)

while True:
    try: 
        # Get a random public repository
        repos = g.get_user().get_repos()
        random_repo = random.choice(list(repos))

        # Get a random file from the repository
        files = random_repo.get_contents("")
        random_file = random.choice(files)
         # Choose a random color for each character
        color = random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan'])
        # Print the contents of the file character by character
        try :
            for char in random_file.decoded_content.decode('utf-8'):    
                print(colored(char, color), end='', flush=True)
                time.sleep(0.01)  # pause for 0.1 seconds between characters
        except UnicodeDecodeError:
            pass
    except Exception as e:
        print(e)
        pass
    print('\n\n')  # add some spacing between files

    
