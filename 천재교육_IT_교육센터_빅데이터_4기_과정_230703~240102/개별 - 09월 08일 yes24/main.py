# python 3.8.17에서 작성 되었습니다.

import sys
import click
from datetime import datetime, timedelta

import settings
from pipeline import controller



@click.command()
@click.option('-m', '--custom-batch-month', type = click.STRING, default = '', help = '배치작업연월')
@click.option('-j', '--job-name', type = click.STRING, default = '',  help = '배치작업시 수행되는 작업의 명칭')
def start_batch(custom_batch_month, job_name) :
    print('<<<<< START BATCH >>>>>')
    print(f"\tInput Value : custom_batch_month == '{custom_batch_month}' ")
    print(f"\tInput Value : job_name == '{job_name}' ")
    
    batch_month = _get_batch_month(custom_batch_month)
    print(f"\tValue : batch_month == '{batch_month}' ")
    
    if not batch_month :
        print(f'<<<<< KILL BATCH : batch_month == {batch_month} >>>>>')
        sys.exit(1)
    
    elif job_name == '' :
        print(f'<<<<< KILL BATCH : job_name == {job_name} >>>>>')
        sys.exit(1)
        
    try : 
        controller.__getattribute__(job_name)(batch_month)
        
    except Exception as e :
        print(f'<<<<< KILL BATCH : Exception == {e} >>>>>')
        sys.exit(1)
        
    print('<<<<< END BATCH >>>>>')
    sys.exit(0)

def _get_batch_month(_custom_batch_month) :
    
    print(_custom_batch_month)
    if _custom_batch_month != '' :
        return _check_valid_month(_custom_batch_month)
    
    first_day = datetime.today().replace(day = 1)
    logical_day = first_day - timedelta(days = 1)
    batch_month = logical_day.strftime('%Y%m')
    
    return batch_month

def _check_valid_month(_str_yyyymm) :
    try :
        datetime.strptime(_str_yyyymm, '%Y%m')
        return _str_yyyymm
    
    except Exception as e :
        print(e)
        return None
    
if __name__ == '__main__' :
    start_batch()