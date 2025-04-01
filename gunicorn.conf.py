import multiprocessing as mp
from configs import settings


workers = mp.cpu_count() * 2 + 1
bind = f'{settings.HOST}:{settings.PORT}'
accesslog = '-'
errorlog = '-'
