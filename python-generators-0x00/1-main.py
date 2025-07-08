#!/usr/bin/python3
from itertools import islice

stream_users = __import__('0-stream_users').stream_users

generator = stream_users()

# Print the first 6 rows
for user in islice(generator, 6):
    print(user)


try:
    next(generator)
except StopIteration:
    pass