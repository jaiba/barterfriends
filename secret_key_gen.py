import os

PROJECT_PATH = '/home/%s/sites/%s' % (env.user, env.host)
try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(PROJECT_PATH, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            import random

            SECRET_KEY = ''.join(
                [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = open(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % SECRET_FILE)
