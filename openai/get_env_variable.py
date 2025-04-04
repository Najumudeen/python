import os
import openai
import getpass

os.environ['x'] = 'abc'
print(os.getenv('x'))

os.environ['OPENAI_API_KEY'] = 'USE_YOUR_OPENAI_API_KEY'

openai.api_key = os.getenv('OPENAI_API_KEY')

key = getpass.getpass('Paste your API Key:')
openai.api_key = key

# with file key
openai.api_key = open('key.txt').read().strip('\n')


# Newest Powerfull model

prompt = 'Write a motto for a football team'

reponse = openai.ChatCompletion.create(
    model='text-davinci-003',
    prompt = prompt,
    temperature = 0.8,
    man_tokens = 1000
)

r = response['choices'][0]['text']
print(r)


import requests
import shutil  # To Copy files
from PIL import Image # install pillo 
resource = requests.get(image_url, stream=True)

print(resource.status_code)

if resource.status_code == 200:
    pass
    with open('daler.png') as f:
        shutil.copyfileobj(resource.raw, f)
else:
    print('Error accessing the image!')

Image.open('dalle1.png')
