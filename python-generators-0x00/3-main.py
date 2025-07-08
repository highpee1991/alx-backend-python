#!/usr/bin/python3
from itertools import islice
import sys
lazy_paginator = __import__('2-lazy_paginate').lazy_pagination


# Create a flattened generator of all users
def all_users_lazy(page_size):
    for page in lazy_paginator(page_size):
        for user in page:
            yield user

#  Print only the first 4 users
for user in islice(all_users_lazy(100), 100):
    print(user)
