from Close import get_all_high,get_all_low,get_all_volume,get_all_close,get_all_open
from conn_postgre import create_table,change_column_type_to_timestamp,insert_data
import time 

df = get_all_volume()
create_table("volume",df.columns)
change_column_type_to_timestamp("volume")
insert_data("volume",df)
time.sleep(30)

df = get_all_close()
create_table("close",df.columns)
change_column_type_to_timestamp("close")
insert_data("close",df)
time.sleep(30)

df = get_all_open()
create_table("open",df.columns)
change_column_type_to_timestamp("open")
insert_data("open",df)
time.sleep(30)

df = get_all_low()
create_table("low",df.columns)
change_column_type_to_timestamp("low")
insert_data("low",df)
time.sleep(30)

df = get_all_high()
create_table("high",df.columns)
change_column_type_to_timestamp("high")
insert_data("high",df)