import glob
import sqlite3
import sys
import os

from sqlalchemy import create_engine
import pandas as pd

from utils import *

files_exp = glob.glob(r"F:\adidas\sensor data\Experience all video sensor data\low session 1 - PRE\psd+shimmer\*.db")
# files_pc = glob.glob(r"F:\adidas\sensor data\Product*sensor data*\**\*_*.db")

# out_db = sqlite3.connect('test_combine.db')

for file in files_exp:
    # db = sqlite3.connect(file)

    try:
        db = create_engine('sqlite:///' + file)
        print("Reading ", file)
        df = pd.read_sql_table('clean', db)
        df.to_csv(os.path.splitext(file)[0] + '_clean.csv', header=True, index=False)
    except Exception as e:
        print(f"Error processing {file}:::{e}", file=sys.stderr)
