#encoding =utf-8

import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        os.unlink(filename)
        print(filename)