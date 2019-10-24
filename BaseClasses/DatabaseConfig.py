# python3
# -*- coding:utf8 -*-
import json
import pymysql


class DatabaseConfig(object):
    def __init__(self, config_filename):
        config_json = json.load(open(config_filename, 'r'))
        config_json = config_json["MysqlDatabase"]
        self.__host = config_json['host']
        self.__port = config_json['port']
        self.__schema = config_json['schema']
        self.__user = config_json['user']
        self.__password = config_json['password']
        self.__table_pois = config_json['table_pois']
        self.__table_checkin = config_json['table_checkin']
        self.__table_geo = config_json['table_geo']
        self.__table_all = config_json['table_all']
        # connection
        self.db_conn = None

    def get_db_connection(self) -> pymysql.cursors.DictCursor:
        if self.db_conn is None:
            self.db_conn = pymysql.connect(host=self.__host, port=int(self.__port), user=self.__user,
                                           password=self.__password, database=self.__schema, charset='utf8')
        return self.db_conn.cursor(pymysql.cursors.DictCursor)
