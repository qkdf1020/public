from settings import DB_SETTINGS

from db.connector import DBConnector
from db.queries_rdb import queries_rdb
from db.queries_ddb import queries_ddb

from pipeline import extract, transform, load

from ast import literal_eval



def etl_job_1(_batch_month) :
    print('<< Start etl_job_1 >>')

    _source_db_conn = DBConnector(**DB_SETTINGS['source_db_localhost_rdb'])
    _target_db_conn = DBConnector(**DB_SETTINGS['target_db_localhost_rdb'])

    _source_table_list = ['actor', 'film']
    _target_table_list = ['actor_back_v1', 'film_back_v1']

    for _idx, _tb in enumerate(_source_table_list) :

        print(f"#####-----  Start Extract : table_name == '{_tb}'  -----#####")
        _read_query = queries_rdb['read'][_tb]
        data = extract.rdb_cursor_extractor(_source_db_conn, _read_query)
        print(f"#####-----  End Extract : row_cnt == '{len(data)}'  -----#####")

        _tb_back = _target_table_list[_idx]
        print(f"#####-----  Start Load : table_name == '{_tb_back}'  -----#####")
        _create_query = queries_rdb['create'][_tb_back]
        load.rdb_cursor_loader(_target_db_conn, _create_query, data)
        print(f"#####-----  End Load  -----#####")

    print('<< End etl_job_1 >>')

def etl_job_2(_batch_month) :
    print('<< Start etl_job_2 >>')

    _source_db_conn = DBConnector(**DB_SETTINGS['source_db_localhost_rdb'])
    _target_db_conn = DBConnector(**DB_SETTINGS['target_db_localhost_rdb'])

    _source_table_list = ['actor', 'film', 'film_actor']
    _target_table_list = ['actor_back_v1', 'film_back_v1', 'film_actor_back_v1']

    for _idx, _tb in enumerate(_source_table_list) :

        print(f"#####-----  Start Extract : table_name == '{_tb}'  -----#####")
        _read_query = queries_rdb['read'][_tb]
        pdf = extract.rdb_pandas_extractor(_source_db_conn, _read_query)
        print(f"#####-----  End Extract : row_cnt == '{len(pdf)}'  -----#####")

        _tb_back = _target_table_list[_idx]
        print( f"#####-----  Start Load : table_name == '{_tb_back}'  -----#####")
        load.rdb_pandas_loader(_target_db_conn, _tb_back, pdf)
        print(f"#####-----  End Load  -----#####")

    print('<< End etl_job_2 >>')

def etl_job_3(_batch_month) :
    print('<< Start etl_job_3 >>')

    _source_db_conn = DBConnector(**DB_SETTINGS['source_db_localhost_rdb'])
    _target_db_conn = DBConnector(**DB_SETTINGS['target_db_localhost_rdb'])

    _source_table_list = ['actor_yyyymm', 'film_yyyymm']
    _target_table_list = ['actor_back_v2', 'film_back_v2']

    for _idx, _tb in enumerate(_source_table_list) :

        print(f"#####-----  Start Extract : table_name == '{_tb}'  -----#####")
        _read_query = queries_rdb['read'][_tb].format(*[_batch_month])
        data = extract.rdb_cursor_extractor(_source_db_conn, _read_query)
        print(f"#####-----  End Extract : row_cnt == '{len(data)}'  -----#####")

        _tb_back = _target_table_list[_idx]
        print(f"#####-----  Start Load : table_name == '{_tb_back}'  -----#####")
        _create_query = queries_rdb['create'][_tb_back]
        load.rdb_cursor_loader(_target_db_conn, _create_query, data)
        print(f"#####-----  End Load  -----#####")

    print('<< End etl_job_3 >>')

def etl_job_4(_batch_month) :
    print('<< Start etl_job_4 >>')

    _source_db_conn = DBConnector(**DB_SETTINGS['source_db_localhost_rdb'])
    _target_db_conn = DBConnector(**DB_SETTINGS['target_db_localhost_rdb'])

    _source_table_list = ['actor', 'film', 'film_actor']
    _target_table_list = []

    _pdfs = []
    for _idx, _tb in enumerate(_source_table_list) :
        
        print(f"#####-----  Start Extract : table_name == '{_tb}'  -----#####")
        _read_query = queries_rdb['read'][_tb]
        pdf = extract.rdb_pandas_extractor(_source_db_conn, _read_query)
        _pdfs.append(pdf)
        print(f"#####-----  End Extract : row_cnt == '{len(pdf)}'  -----#####")
        
    print(f"#####-----  Start Transform  -----#####")
    _transform_df = transform.transform_etl_job_4(_pdfs)
    print(f"#####-----  End Transform  -----#####")

    _tb_name = 'join_table_actor_and_film'
    print(f"#####-----  Start Load : table_name == '{_tb_name}'  -----#####")
    load.rdb_pandas_loader(_target_db_conn, tb_name, _transform_df)
    print(f"#####-----  End Load  -----#####")

    print('<< End etl_job_4 >>')

def etl_job_5(_batch_month) :
    print('<< Start etl_job_5 >>')

    _source_db_conn = DBConnector(**DB_SETTINGS['source_db_localhost_ddb'])
    _target_db_conn = DBConnector(**DB_SETTINGS['target_db_localhost_ddb'])
    
    _source_collection_list = ['book_code']
    _target_collection_list = ['book_code_back_v2']
    
    for _idx, _coll in enumerate(_source_collection_list) :
        
        print(f"#####-----  Start Extract : collection_name == '{_coll}'  -----#####")
        _read_query = literal_eval(queries_ddb['read'][_coll].strip())
        data = extract.ddb_cursor_extractor(_source_db_conn, _coll, _read_query)
        print(f"#####-----  End Extract : row_cnt == '{len(data)}'  -----#####")
        
        _coll_back = _target_collection_list[_idx]
        print(f"#####-----  Start load : collection_name == '{_coll_back}'  -----#####")
        load.ddb_cursor_loader(_target_db_conn, _coll_back, data)
    print(f"#####-----  End Load  -----#####")
        
    print('<< End etl_job_5 >>')
    
def etl_job_6(_batch_month) :
    print('<< Start etl_job_6 >>')

    _source_db_conn = DBConnector(**DB_SETTINGS['source_db_localhost_ddb'])
    _target_db_conn = DBConnector(**DB_SETTINGS['target_db_localhost_rdb'])

    _source_collection_list = ['book_code']
    _target_table_list = ['book_code_basic_back']

    for _idx, _coll in enumerate(_source_collection_list) :

        print(f"#####-----  Start Extract : collection_name == '{_coll}'  -----#####")
        _read_query = literal_eval(queries_ddb['read'][_coll].strip())
        data = extract.ddb_cursor_extractor(_source_db_conn, _coll, _read_query)
        print(f"#####-----  End Extract : row_cnt == '{len(data)}'  -----#####")
        
        _transform_df = transform.transform_etl_job_6(data)
        
        _tb_name = _target_table_list[_idx]
        print( f"#####-----  Start Load : table_name == '{_tb_name}'  -----#####")
        load.rdb_pandas_loader(_target_db_conn, _tb_name, _transform_df)
        print(f"#####-----  End Load  -----#####")

    print('<< End etl_job_6 >>')

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