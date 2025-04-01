import multiprocessing as mp
from dotenv import load_dotenv
from os import getenv

load_dotenv()


workers = mp.cpu_count() * 2 + 1
bind = f'{getenv('HOST', '0.0.0.0')}:{getenv('PORT', 5000)}'
accesslog = '-'
