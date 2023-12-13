import requests
import random
import time
import re
import json
import csv
from datetime import datetime


class WeiboCommentsCrawler:
    def __init__(self, start_url, target_comments=200, max_retry=3):
        self.start_url = start_url
        self.target_comments = target_comments
        self.max_retry = max_retry
        self.count = 0
        self.current_url = start_url
        self.next_url_template = start_url
        # 设置请求头
        self.headers = {
            'cookie': '_T_WM=62489705963; WEIBOCN_FROM=1110006030; SCF=AskHINEWHjMJ4xmrCDJjHMZhormG-aTrzJdTciJXGWRslPbnC-9Him08ic7kvK42V2ZpM_OedJ6Ru2pwrFTbsok.; SUB=_2A25IdTzbDeRhGeBO41EX8i3MwzWIHXVrCzATrDV6PUNbktANLUfxkW1NRb9llyQZwPw1kQsLtTA5_64nmp1_xt6S; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhkmY.4IuTZno2X1z4AZV4q5JpX5KMhUgL.Foq71heceoe71h.2dJLoI7L0UgUyPNiyIgRt; SSOLoginState=1701923979; ALF=1704515979; MLOGIN=1; XSRF-TOKEN=88d1b7; mweibo_short_token=69914700a8; M_WEIBOCN_PARAMS=oid%3D4976073798583078%26luicode%3D20000061%26lfid%3D4976073798583078%26uicode%3D20000061%26fid%3D4976073798583078',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        }

        # CSV文件的标题行
        self.file_header = ["id", "评论时间", "用户ID", "昵称", "评论内容", "用户归属地", "点赞数量"]

    def get_data(self, url):
        retry_count = 0
        while retry_count < self.max_retry:
            try:
                response = requests.get(url=url, headers=self.headers, timeout=5)
                data = json.loads(response.text)

                if response.status_code == 200 and data['ok'] == 1:
                    max_id = data.get("data").get("max_id")
                    comments = data.get('data').get('data')

                    for item in comments:
                        self.count += 1
                        create_time = self.time_change(item['created_at'])
                        text = ''.join(re.findall('[\u4e00-\u9fa5]', item['text']))
                        user_id = item.get('user')['id']
                        screen_name = item.get('user')['screen_name']
                        ip_from = item['source']
                        like_count = item['like_count']
                        self.csv_operator([self.count, create_time, user_id, screen_name, text, ip_from, like_count])
                        print([self.count, create_time, user_id, screen_name, text, ip_from, like_count])
                        print("第{}条数据获取成功".format(self.count))

                        if self.count >= self.target_comments:
                            print(f"已成功获取 {self.target_comments} 条评论，开始生成图表...")
                            return

                    continue_url = self.next_url_template.format(str(max_id))
                    time.sleep(random.random() * 5)

                else:
                    print(f"未成功获取数据，响应码：{response.status_code}，重试中...")
                    retry_count += 1
                    time.sleep(random.random() * 5)

            except Exception as e:
                print(f"发生异常：{e}")
                retry_count += 1
                time.sleep(random.random() * 5)

        print(f"连续{self.max_retry}次未响应，程序退出。")

    def csv_operator(self, row_data):
        with open("weibocomments.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(row_data)

    def time_change(self, time_data):
        original_string = time_data
        parsed_datetime = datetime.strptime(original_string, "%a %b %d %H:%M:%S %z %Y")
        formatted_string = parsed_datetime.strftime("%Y.%m.%d %H:%M:%S")
        return formatted_string

    def crawl_weibo_comments(self):
        self.current_url = self.start_url
        self.csv_operator(self.file_header)
        self.get_data(self.current_url)
