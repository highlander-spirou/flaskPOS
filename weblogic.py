import numpy as np
import pandas as pd
# from flask_sqlalchemy import SQLAlchemy
from app import db


df = pd.read_sql_query('select * from Input', db.engine)
print(df)