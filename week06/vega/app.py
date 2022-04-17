from colorama import Fore, Style
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewService
import os
import sys
import time
__user_service=UserService()
__news_service=NewService()

while True:
    os.system("cls")
    print(Fore.LIGHTBLUE_EX, "\n\t===============")
    print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t===============")
    print(Fore.LIGHTGREEN_EX, "\n\t1.登录系统")
    print(Fore.LIGHTGREEN_EX, "\n\t2.退出系统")
    # 重置字体
    print(Style.RESET_ALL)
    opt = input("\n\t输出操作编号:")
    if opt == "1":
        username = input("\n\t用户名:")
        password = input("\n\t密码:")
        # password = getpass("\n\t密码")
        result = __user_service.login(username, password)
        # 登录成功
        if result == True:
            role = __user_service.search_user_role(username)
            os.system("cls")
            while True:
                if role == "新闻编辑":
                    print("test")
                elif  role == "管理员":
                    print(Fore.LIGHTGREEN_EX, "\n\t1.新闻管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.用户管理")
                    print(Fore.LIGHTRED_EX, "\n\tback.退出登录")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输出操作编号:")
                    if opt == "1":
                        page = 1
                        page_count = __news_service.unreview_count() # 未审批新闻所占页数
                        all_count = __news_service.all_count() # 全部新闻的页数
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.审批新闻")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号:")
                            if opt == "back":
                                break
                            # 删除新闻
                            elif opt == "2":
                                # 展示所有新闻
                                result = __news_service.all_news(page)
                                print("编号\t标题\t\t类型\t作者\t状态")
                                for index in range(len(result)):
                                    print(Fore.LIGHTGREEN_EX, "%s\t%s\t%s\t%s\t%s" %
                                          (index + 1, result[index][0], result[index][1], result[index][2], result[index][3]))
                                print()
                                print(Fore.LIGHTRED_EX, f"页码:{page}/{all_count}", end="\t")
                                print(Fore.LIGHTRED_EX, "pre \t next   删除:d")
                                # 开始删除新闻
                                while True:
                                    os.system("cls")
                                    print(Fore.LIGHTGREEN_EX, "\n\tpre:上一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\tnext:下一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\td:删除")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    opt = input("\n\t输入操作指令:")
                                    if opt == "back":
                                        break
                                    elif opt == "pre" and page > 1:
                                        page -= 1
                                        # 展示
                                        # 展示所有新闻
                                        result = __news_service.all_news(page)
                                        print("编号\t标题\t\t类型\t作者\t状态")
                                        for index in range(len(result)):
                                            print(Fore.LIGHTGREEN_EX, "%s\t%s\t%s\t%s\t%s" %
                                                  (index + 1, result[index][0], result[index][1], result[index][2],
                                                   result[index][3]))
                                        print()
                                        print(Fore.LIGHTRED_EX, f"页码:{page}/{all_count}", end="\t")
                                        print(Fore.LIGHTRED_EX, "pre \t next   删除:d")
                                    elif opt == "next" and page < all_count:
                                        page += 1
                                        # 展示所有新闻
                                        result = __news_service.all_news(page)
                                        print("编号\t标题\t\t类型\t作者\t状态")
                                        for index in range(len(result)):
                                            print(Fore.LIGHTGREEN_EX, "%s\t%s\t%s\t%s\t%s" %
                                                  (index + 1, result[index][0], result[index][1], result[index][2],
                                                   result[index][3]))
                                        print()
                                        print(Fore.LIGHTRED_EX, f"页码:{page}/{all_count}", end="\t")
                                        print(Fore.LIGHTRED_EX, "pre \t next   删除:d")

                                    elif opt == "d":
                                        num = int(input("\n\t输入删除索引:"))
                                        print(num, type(num))
                                        result = __news_service.all_news(page)
                                        __news_service.delete_by_id(result[num - 1][4])
                                        print("删除成功（1秒后显示）")
                                        time.sleep(1)
                                        # 展示所有新闻
                                        result = __news_service.all_news(page)
                                        print("编号\t标题\t\t类型\t作者\t状态")
                                        for index in range(len(result)):
                                            print(Fore.LIGHTGREEN_EX, "%s\t%s\t%s\t%s\t%s" %
                                                  (index + 1, result[index][0], result[index][1], result[index][2],
                                                   result[index][3]))
                                        print()
                                        print(Fore.LIGHTRED_EX, f"页码:{page}/{all_count}", end="\t")
                                        print(Fore.LIGHTRED_EX, "pre \t next   删除:d")

                            # 审批新闻
                            elif opt == "1":
                                result = __news_service.search_unreview_list(page)
                                # print(result)
                                print("编号\t标题\t\t类型\t作者")
                                for index in range(len(result)):
                                    print(Fore.LIGHTGREEN_EX, "%s\t%s\t%s\t%s" %
                                          (index+1, result[index][1], result[index][2], result[index][3]))
                                print()
                                print(Fore.LIGHTRED_EX, f"页码:{page}/{page_count}", end="\t")
                                print(Fore.LIGHTRED_EX, "pre \t next")
                                # 开始审批
                                while True:
                                    os.system("cls")
                                    print(Fore.LIGHTGREEN_EX, "\n\tpre:上一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\tnext:下一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\tstart:开始审批")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    opt = input("\n\t输入操作指令:")
                                    if opt == "back":
                                        break
                                    elif opt == "pre" and page > 1:
                                        page -= 1
                                        # 展示
                                        os.system("cls")
                                        result = __news_service.search_unreview_list(page)
                                        print("编号\t标题\t\t类型\t作者")
                                        for index in range(len(result)):
                                            print(Fore.LIGHTGREEN_EX, "%s\t%s\t%s\t%s" %
                                                  (index+1, result[index][1], result[index][2], result[index][3]))
                                        print()
                                        print(Fore.LIGHTRED_EX, f"页码:{page}/{page_count}", end="\t")
                                        print(Fore.LIGHTRED_EX, "pre \t next")
                                    elif opt == "next" and page < page_count:
                                        page += 1
                                        result = __news_service.search_unreview_list(page)
                                        os.system("cls")
                                        print("编号\t标题\t\t类型\t作者")
                                        for index in range(len(result)):
                                            print(Fore.LIGHTGREEN_EX, "%s\t%s\t%s\t%s" %
                                                  (index+1, result[index][1], result[index][2], result[index][3]))
                                        print()
                                        print(Fore.LIGHTRED_EX, f"页码:{page}/{page_count}", end="\t")
                                        print(Fore.LIGHTRED_EX, "pre \t next")

                                    elif opt == "start":
                                        num = int(input("\n\t输入审批号码:"))
                                        result = __news_service.search_unreview_list(page)
                                        __news_service.review_news(result[num-1][0])
                                        print("审批成功（1秒后显示）")
                                        time.sleep(1)
                                        # 展示
                                        result = __news_service.search_unreview_list(page)
                                        os.system("cls")
                                        print("编号\t标题\t\t类型\t作者")
                                        for index in range(len(result)):
                                            print(Fore.LIGHTGREEN_EX, "%s\t%s\t%s\t%s" %
                                                  (index + 1, result[index][1], result[index][2], result[index][3]))
                                        print()
                                        print(Fore.LIGHTRED_EX, f"页码:{page}/{page_count}", end="\t")
                                        print(Fore.LIGHTRED_EX, "pre \t next")

                    elif opt == "back":
                        break
                    elif opt == "exit":
                        sys.exit(0)

        else:
            print("\n\t登录失败(3秒自动返回)")
            time.sleep(3)
    elif opt == "2":
        sys.exit(0)
