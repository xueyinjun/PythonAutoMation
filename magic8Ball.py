#encoding=utf-8

import random

messages = [
    'It is certain', 'Yes definitely', 'Rely hazy try again',
    'Ask again later', 'Concentrate and ask again', 'My reply is no',
    'Outlook not so good', 'Very doubtful'
]
print(messages[random.randint(0, len(messages)-1)])
