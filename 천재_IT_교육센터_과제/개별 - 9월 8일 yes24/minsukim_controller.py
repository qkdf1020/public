from settings import DB_SETTINGS

from db.connector import DBConnector
from db.queries_rdb import queries_rdb
from db.queries_ddb import queries_ddb

from pipeline import extract, transform, load

from ast import literal_eval



def minsukim(_batch_month) :
    print('<< Start minsukim >>')

    _source_db_conn = DBConnector(**DB_SETTINGS['source_db_localhost_ddb'])
    _target_db_conn = DBConnector(**DB_SETTINGS['sample_db_localhost_rdb'])

    _source_collection_list = ['math_book']

    for _idx, _coll in enumerate(_source_collection_list) :

        print(f"#####-----  Start Extract : collection_name == '{_coll}'  -----#####")
        _read_query = literal_eval(queries_ddb['read'][_coll].strip())
        data = extract.ddb_cursor_extractor(_source_db_conn, _coll, _read_query)
        print(f"#####-----  End Extract : row_cnt == '{len(data)}'  -----#####")
        
        _transform_df_1 = transform.transform_minsukim_1(data)
        _transform_df_2 = transform.transform_minsukim_2(data)
        
        _target_table_list_1 = ['{}_math_book_analytics_minsukim'.format(transform.transform_minsukim_3(data))]
        _target_table_list_2 = ['online_data']
        
        _tb_name_1 = _target_table_list_1[_idx]
        _tb_name_2 = _target_table_list_2[_idx]
        
        print( f"#####-----  Start Load : table_name == '{_tb_name_1}'  -----#####")
        load.rdb_pandas_loader(_target_db_conn, _tb_name_1, _transform_df_2)
        print(f"#####-----  End Load {transform.transform_minsukim_2(data).shape}  -----#####")
        
        print( f"#####-----  Start Load : table_name == '{_tb_name_2}'  -----#####")
        load.rdb_pandas_loader(_target_db_conn, _tb_name_2, _transform_df_1)
        print(f"#####-----  End Load {transform.transform_minsukim_1(data).shape}  -----#####")

    print('<< End minsukim >>')