from db.config import load_config
from db.connect import connect
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2://postgres:Password$1234@localhost/proy_bi_mundo_ss2')

    df =  pd.read_excel('data\Unesco Core Data Portal Sources of Funding for 13 May 2024 - 12_20 am.xlsx')
    df.to_sql('my_table', con=engine, index=False)
    # df['Year'].astype('int64')
    # df.groupby(['Contributor', 'year'])['Contribution (USD)'] \
    # .sum().reset_index()
    
    # df_pu.loc[df_pu['Project ID'] == '201GLO1005'].groupby(['Project ID'])[['Project Budget (USD)', 'Cumulative Incurred Expenditures (USD)']].sum()


    # df.groupby(['year','quarter'])['Planned Expenditure (USD)'].sum().reset_index()

    # df.loc[df['sum'] == df['sum'].min()]

    # result = df.groupby(['Project ID', 'Project Title'])[['Project Budget (USD)', 'Cumulative Incurred Expenditures (USD)']].sum().reset_index()
    # result.loc[result['Project ID'] == '201URT1000']

    # df.loc[df['Sector'] == 'Education']['Planned Expenditure (USD)'].sum()

    # query 'SELECT  year, quarter, COUNT(quarter), SUM("Contribution (USD)") FROM sources_funding_unesco GROUP BY quarter, year ORDER BY quarter ASC'
    # query 'SELECT  year, quarter, COUNT(quarter), SUM("Contribution (USD)") FROM sources_funding_unesco GROUP BY quarter, year ORDER BY sum ASC'

    # query = 'select * from sources_funding_unesco'
    # df = pd.read_sql(sql=query, con=engine)

    # df = pd.read_sql('select * from sources_funding_unesco', engine)

    # df_cleaned.loc[df_cleaned['Cause'] == '1020']
    # df_cleaned.groupby(['Sex'])['Deaths1'].sum().reset_index()

def get_connection():
    engine = create_engine('postgresql+psycopg2://postgres:Password$1234@localhost/proy_bi_mundo_ss2')
    return engine
