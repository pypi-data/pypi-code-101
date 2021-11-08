"""
依赖django的功能函数
"""

from . import pure

import math
import pandas as pd

from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.request import Request
from functools import wraps
from django.db import connection
from django.db.models import Q
from django.db.models import QuerySet


def APIResponse(ret, status=200, msg=None):
    if isinstance(ret, Response):
        ret = ret.data
    ret = pure.add_status_and_msg(ret, status=status, msg=msg)
    ret = Response(ret)
    return ret


class Pagination(PageNumberPagination):
    """
    * 默认分页器参数设置

    - page_size: 每页16个
    - page_size_query_param: 前端控制每页数量时使用的参数名, 'page_size'
    - page_query_param: 页码控制参数名"p"
    - max_page_size: 最大100页
    """
    page_size = 100
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 1000


class BaseList(ListModelMixin, RetrieveModelMixin, GenericAPIView):
    """
    * API: BaseModel的ListView和RetrieveView接口

    - 测试接口:
        - List:
            GET /api/index/BaseList/?order_type=-id&page_size=4&p=1
        - Retrieve:
            GET /api/index/BaseList/5/
    """

    pagination_class = Pagination
    filter_fields = []

    def get(self, request: Request, *args, **kwargs):
        """
        - 如果request携带pk参数, 则进行Retrieve操作, 否则进行List操作.

        - BaseList的默认get请求参数(仅在List操作时生效)
            - page_size: 分页器每页数量, 前端用来控制数据每页展示的数量, 在Pagination类中设置.
            - p: 第p页.
            - order_type: 排序字段, 如"id"和"-id".
        """
        if kwargs.get('pk'):
            ret, status, msg = self.get_retrieve_ret(request, *args, **kwargs)
        else:
            ret, status, msg = self.get_list_ret(request, *args, **kwargs)
        return APIResponse(ret, status=status, msg=msg)

    def get_retrieve_ret(self, request: Request, *args, **kwargs):
        """
        Retrieve操作

        - pk必须在`url.py::urlpatterns`中设置, 如: path('BaseList/<str:pk>/', views.BaseList.as_view())
        """
        status = 200
        msg = 'ok'

        try:
            ret = self.retrieve(request)
        except Exception as e:
            # 没找到的情况, 404 Not Found
            ret = None
            status = 404
            msg = str(e)
        return ret, status, msg

    def get_list_ret(self, request: Request, *args, **kwargs):
        """
        List操作
        """
        status = 200
        msg = 'ok'

        self._get_list_queryset()

        # --- 解析请求参数
        query_dc = request.query_params

        order_type = query_dc.get('order_type')
        if order_type:
            try:
                self.queryset = self.queryset.order_by(order_type)
            except ValueError as e:
                ret = None
                status = 404
                msg = f'参数order_type指定的排序字段[{order_type}]取值错误!'
                return ret, status, msg

        # --- 获取返回数据
        try:
            ret = self.list(request)
        except Exception as e:
            # 页码无效的情况, 404 Not Found
            ret = None
            status = 404
            msg = str(e)
        return ret, status, msg

    def _get_list_queryset(self):
        """
        得到queryset, 仅对list方法生效
        """
        query_dc = self.request.query_params
        self.queryset = super().get_queryset()
        if not isinstance(self.queryset, QuerySet):
            self.queryset = self.queryset.objects.all()

        if self.queryset.count():
            """
            过滤字段filter_fields
            """
            meta = self.queryset[0]._meta
            field_names = [field.name for field in meta.fields]
            for fn in field_names:
                if fn in self.filter_fields:
                    if fn in query_dc:
                        value = query_dc.get(fn)
                        exec(f"self.queryset = self.queryset.filter(Q({fn}='{value}'))")

        return self.queryset

    def list(self, request: Request, *args, **kwargs):
        resp = super(BaseList, self).list(request, *args, **kwargs)
        ret = self._conv_data_format(resp)
        return ret

    def _conv_data_format(self, data: (dict, Response)):
        if isinstance(data, Response):
            data = data.data

        # 分页信息
        count = data.get('count')
        page_size = self.request.query_params.get('page_size', self.pagination_class.page_size)
        p = self.request.query_params.get('p', 1)
        total = math.ceil(count / int(page_size))
        page_dc = {
            'count': count,
            'total': total,
            'page_size': page_size,
            'p': p,
        }

        results = data.get('results')

        ret = {
            'page_dc': page_dc,
            'results': results,
        }
        return ret


def paginate_qsls_to_dcls(qsls, serializer, page: int, per_page=16):
    """
    * 手动分页函数

    - 指定模型的queryset_ls和serializer, 然后按给定的page和per_page参数获取分页后的数据
    """

    p = Paginator(qsls, per_page)
    page_obj = p.get_page(page)
    page_dc = {
        'num_pages': p.num_pages,
        'count_objects': p.count,
        'current_page_number': page_obj.number,
    }

    # --- 处理单个Model和多个Model的情况
    if serializer.__class__.__name__ == 'function':
        dc_ls = serializer(page_obj)
    else:
        dc_ls = serializer(page_obj, many=True).data
    return dc_ls, page_dc


def conv_qsls_to_dcls(qsls: list, names: list=None, new_names=None):
    """
    将一个queryset_list转换为dict_list
    """
    if not qsls:
        return []

    if names is None:
        names = list(qsls[0].keys())

    if not new_names:
        new_names = names

    dc_ls = []
    for qs in qsls:
        if names and new_names:
            # 优化版
            values = []
            for name in names:
                values.append(qs.get(name))

            dc = dict(zip(new_names, values))
        else:
            # 手动一算
            if names.__len__() == 2:
                name, value = qs.get(names[0]), qs.get(names[1])
                dc = {
                    new_names[0]: name,
                    new_names[1]: value,
                }
            elif names.__len__() == 3:
                name, code, value = qs.get(names[0]), qs.get(names[1]), qs.get(names[2])
                dc = {
                    new_names[0]: name,
                    new_names[1]: code,
                    new_names[2]: value,
                }
            else:
                print('长度不对!')
                dc = {}
        dc_ls.append(dc)
    return dc_ls


def order_qs_ls_by_id(qs_ls, sort_by='id'):
    df = pd.DataFrame(qs_ls).sort_values(by=sort_by)

    cols = df.columns
    dc_ls = []
    for i, row in df.iterrows():
        dc = {
            cols[0]: row.get(cols[0]),
            cols[1]: row.get(cols[1]),
        }
        dc_ls.append(dc)
    return dc_ls


def api_decorator(func):
    """
    * API装饰器

    - 如果运行出错, 将格式化输出错误的信息, 并返回给前端, 而不会报错.
    """
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print('--- API Error! ---')
            print(e)
            return APIResponse(str(e), status=404, msg='Error!')
    return wrapped_function


def get_model_max_id_in_db(model=None, meta=None):
    """
    仅适用于postgresql, mysql直接忽略就行.
    """
    if not meta:
        meta = model._meta

    cursor = connection.cursor()
    # db_prefix = meta.__str__().split('.')[0]

    # --- 先尝试创建id_seq
    id_seq = f"{meta.app_label}_{meta.db_table}_id_seq"

    try:
        sql = f"""CREATE SEQUENCE IF NOT EXISTS {id_seq}"""
        cursor.execute(sql)
    except Exception as e:
        print(e)
        print('不是PostgreSQL无法运行CREATE SEQUENCE语句! 请确认数据库类型!')

    # --- 找出最大的id
    sql = f"""select setval('{id_seq}', (select max(id) from "{meta.db_table}")+1);"""
    # sql = '(select max(id) from  "{meta.db_table}")'
    print('sql---', sql)
    cursor.execute(sql)
    row = cursor.fetchall()
    curr_id = row[0][0]
    ret = 0 if curr_id is None else curr_id
    return ret

