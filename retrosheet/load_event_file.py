#import psycopg2
#conn = psycopg2.connect("host=localhost dbname=lahman2017 user=lahman")

import subprocess
path = '/Users/youngty/Projects/baseball_data/retrosheet/2017/2017ANA.csv'
with open(path, "a") as file:
    file.flush()
    subprocess.call(['cwevent','-y', '2017', 'a' , '2017ANA.EVA'],cwd='2017', stdout=file)
#df = pandas.read_csv('/Projects/baseball_data/retrosheet/2017/2017ANA.csv')
