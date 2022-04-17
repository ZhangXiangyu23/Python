# coding:utf-8
import math

from vega.db.mysql_db import pool

class NewsDao:
    # 查询未审批的新闻，然后进行分页
    def search_unreview_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select n.id, n.title, t.type, u.username " \
                  "from t_news n join t_type t on n.type_id=t.id " \
                  "join t_user u on n.editor_id=u.id " \
                  "where n.state=%s " \
                  "order by n.create_time DESC " \
                  "limit %s, %s"
            # 每一页显示10条数据
            cursor.execute(sql, ("待审批", (page-1)*10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" is dir():
                con.close()


    # 查询总页数
    def unreview_count(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select count(*) from t_news where state='待审批'"
            cursor.execute(sql)
            # fetchone取到的结果是一条记录（元组类型）
            # fetchall取到的结果是多条记录（每一条记录是一个元组，外面是列表套着）
            count = cursor.fetchone()[0]
            page_count = math.ceil(count/10)
            return page_count
        except Exception as e:
            print(e)
        finally:
            if "con" is dir():
                con.close()


    # 对未审批新闻进行审批
    def review_news(self, id):
        try:
            con = pool.get_connection()
            # 开启事务
            con.start_transaction()
            cursor = con.cursor()
            sql = "update  t_news set state = '已审批' where id = %s"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if 'con' is dir():
                con.rollback()
            print(e)
        finally:
            if "con" is dir():
                con.close()

    # 展示全部新闻
    def all_news(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select n.title, t.type, u.username, n.state" \
                  " from t_news n join t_type t on n.type_id = t.id" \
                  " join t_user u on n.editor_id = u.id" \
                  " order by n.create_time DESC " \
                  " limit %s, %s"
            # 每一页显示10条数据
            cursor.execute(sql, ((page-1)*10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" is dir():
                con.close()

    # 所有新闻的数量
    def all_count(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select count(*) from t_news"
            cursor.execute(sql)
            # fetchone取到的结果是一条记录（元组类型）
            # fetchall取到的结果是多条记录（每一条记录是一个元组，外面是列表套着）
            count = cursor.fetchone()[0]
            page_count = math.ceil(count/10)
            return page_count
        except Exception as e:
            print(e)
        finally:
            if "con" is dir():
                con.close()

    # 删除新闻
    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            # 开启事务
            con.start_transaction()
            cursor = con.cursor()
            sql = "delete from t_news where id = %s"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" is dir():
                con.close()






if __name__ == "__main__":
#     service = NewsDao()
#     # result = service.search_unreview_list(1)
#     # print(result)
#     count = service.page_count()
#     print(count)
    service = NewsDao()
    # service.review_news(2)
    # result = service.search_unreview_list(2)
    # print(result)
    # result = service.all_news(2)
    # print(result)

    service.delete_by_id(13)


