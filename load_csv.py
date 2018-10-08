#import psycopg2
#conn = psycopg2.connect("host=localhost dbname=lahman2017 user=lahman")

import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("lahman/baseballdatabank-master/core/AllstarFull.csv")
print(df)

engine = create_engine('postgresql://lahman:lahman@localhost/lahman2017')

df.to_sql("AllstarFull",engine,if_exists='replace')
