from github import Github
import random
import time
import os
from dotenv import load_dotenv

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

        # Print the contents of the file character by character
        try :
            for char in random_file.decoded_content.decode('utf-8'):
                print(char, end='', flush=True)
                time.sleep(0.01)  # pause for 0.1 seconds between characters
        except UnicodeDecodeError:
            pass
    except Exception as e:
        print(e)
        pass
    print('\n\n')  # add some spacing between files

    
