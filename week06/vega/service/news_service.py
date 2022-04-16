# coding:utf-8
from vega.db.news_dao import NewsDao

class NewService:
    __news_service = NewsDao()

    # 查询待审批的新闻列表
    def search_unreview_list(self, page):
        result = self.__news_service.search_unreview_list(1)
        return result
