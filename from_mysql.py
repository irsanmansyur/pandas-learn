from sqlalchemy import create_engine

import pymysql

import pandas as pd

 

sqlEngine       = create_engine('mysql+pymysql://root:@127.0.0.1', pool_recycle=3307)

dbConnection    = sqlEngine.connect()

frame           = pd.read_sql("select * from tikets", dbConnection);

 

pd.set_option('display.expand_frame_repr', False)

print(frame)

 

dbConnection.close()