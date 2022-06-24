import pymysql
from sqlalchemy import create_engine


def db_connection(*, mysql_server='gator3251.hostgator.com', database='silviog_skin_case_study', user='silviog_skin_1', password='3valuati0n_1'):
    connection_str = f'mysql+pymysql://{user}:{password}@{mysql_server}:3306/{database}'
    connection = create_engine(connection_str)
    return connection
