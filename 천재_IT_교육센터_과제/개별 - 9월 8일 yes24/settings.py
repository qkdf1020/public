# 해당 파일은 python 3.8.17에서 작성 되었습니다.

DB_SETTINGS = {
    'source_db_localhost_rdb' : {
        'host' : "127.0.0.1",
        'port' : "5432",
        'user' : "postgres",
        'pw' : "0akqjqtk0",
        'db' : "dvdrental",
        'location' : "localhost_source",
        'engine' : "postgre"
    },
    'source_db_localhost_ddb' : {
        'host' : "127.0.0.1",
        'port' : 27017,
        'user' : "root",
        'pw' : "qwe123",
        'db' : "yes24",
        'location' : "localhost_source",
        'engine' : "mongodb"
    },    
    'target_db_localhost_rdb' : {
        'host' : "127.0.0.1",
        'port' : "5432",
        'user' : "postgres",
        'pw' : "0akqjqtk0",
        'db' : "role",
        'location' : "localhost_target",
        'engine' : "postgre"
    },
    'target_db_localhost_ddb' : {
        'host' : "127.0.0.1",
        'port' : 27017,
        'user' : "root",
        'pw' : "qwe123",
        'db' : "sample",
        'location' : "localhost_target",
        'engine' : "mongodb"
    },
    'sample_db_localhost_rdb' : {
        'host' : "127.0.0.1",
        'port' : "5432",
        'user' : "postgres",
        'pw' : "0akqjqtk0",
        'db' : "product_analytics",
        'location' : "localhost_target",
        'engine' : "postgre"
    }
}