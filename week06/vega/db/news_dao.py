# coding:utf-8
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



# if __name__ == "__main__":
#     service = NewsDao()
#     result = service.search_unreview_list(1)
#     print(result)

