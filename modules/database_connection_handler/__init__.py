import pyodbc
import time
import requests
import json


def param_request_execution(sql, connection, request_payload):
    cnxn = pyodbc.connect(f'''
    DRIVER={{MySQL ODBC 8.0 ANSI Driver}};
    SERVER={connection['database_address']};
    DATABASE={connection['database_name']};
    UID={connection['database_user']};
    PWD={connection['database_pass']};
    OPTION=3;
    Trusted_Connection=yes; 
    ''')
    cursor = cnxn.cursor()
    cursor.execute(sql, request_payload)
    cursor.commit()
    try:
        sql_result = cursor.fetchall()
        cnxn.close()
        return sql_result
    except Exception as error:
        sql_result = error
        cnxn.close()
        return sql_result

def param_request_execution_auto_commit(sql, connection, request_payload):
    cnxn = pyodbc.connect(f'''
    DRIVER={{MySQL ODBC 8.0 ANSI Driver}};
    SERVER={connection['database_address']};
    DATABASE={connection['database_name']};
    UID={connection['database_user']};
    PWD={connection['database_pass']};
    OPTION=3;
    Trusted_Connection=yes; 
    ''')
    cursor = cnxn.cursor()
    cursor.execute(sql, request_payload)
    cursor.commit()
    try:
        sql_result = cursor.fetchall()
        cnxn.close()
        return sql_result
    except Exception as error:
        sql_result = error
        cnxn.close()
        return sql_result


def execute_sql(sql, connection):
    cnxn = pyodbc.connect(f'''
    DRIVER={{MySQL ODBC 8.0 ANSI Driver}};
    SERVER={connection['database_address']};
    DATABASE={connection['database_name']};
    UID={connection['database_user']};
    PWD={connection['database_pass']};
    OPTION=3;
    ansi=True;
    Trusted_Connection=yes; 
    ''')
    cnxn.setencoding("utf-8")
    cursor = cnxn.cursor()
    cursor.execute(sql)
    cursor.commit()
    try:
        sql_result = cursor.fetchall()
        cnxn.close()
        return sql_result
    except Exception as error:
        sql_result = error
        cnxn.close()
        return sql_result


def create_connection(database_address, database_name, database_user, database_pass):
    connection = dict()
    connection['database_pass'] = database_pass
    connection['database_user'] = database_user
    connection['database_address'] = database_address
    connection['database_name'] = database_name
    return connection
