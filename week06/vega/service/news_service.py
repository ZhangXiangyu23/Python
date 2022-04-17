# coding:utf-8
from vega.db.news_dao import NewsDao

class NewService:
    __news_service = NewsDao()

    # 查询待审批的新闻列表
    def search_unreview_list(self, page):
        result = self.__news_service.search_unreview_list(page)
        return result


    # 查询待审批新闻的总条数
    def unreview_count(self):
        count = self.__news_service.unreview_count()
        return count

    # 对未审批新闻进行审批
    def review_news(self, id):
        self.__news_service.review_news(id)


    # 展示所有新闻
    def all_news(self, page):
        result = self.__news_service.all_news(page)
        return result

    # 所有新闻的页数
    def all_count(self):
        all_count = self.__news_service.all_count()
        return  all_count

    # 删除新闻
    def delete_by_id(self, id):
        self.__news_service.delete_by_id(id)