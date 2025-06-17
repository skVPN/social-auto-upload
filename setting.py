from alex_utils.apollo import APOLLO
from alex_utils.mysqldb import MysqlDB
import json

db_info = json.loads(APOLLO.get_value("mysql_config"))
COOKIE_DB=MysqlDB(**db_info)
BROWSER_URL=APOLLO.get_value("browser_url",default_val="http://172.16.94.44:54345")

