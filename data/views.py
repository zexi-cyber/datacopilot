from django.shortcuts import render, HttpResponse
from data import models
from django.db.models import Avg,Max,Min,Count,Sum,F ,Q #   引入函数
# Create your views here.

from django.db import connection
from . import api
def add_query(request):
    # 您的 SQL 查询字符串
    sql_query = api.get_sql()

    # 获取数据库连接
    with connection.cursor() as cursor:
        # 执行 SQL 查询
        cursor.execute(sql_query)

        # 获取查询结果
        result = cursor.fetchall()

    # 打印结果
    for row in result:
        print(row[0])  # 假设查询结果的第一列是 price

    return HttpResponse(result)

