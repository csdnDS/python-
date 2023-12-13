import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


class BarChartGenerator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path, encoding='gbk')

    def generate_bar_chart(self):
        # 提取省份信息的列
        province_column = '用户归属地'
        provinces = self.df[province_column]

        # 统计各个省份的出现次数
        province_counts = provinces.value_counts()

        # 设置中文字体
        font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
        sns.set(font=font.get_name())

        # 使用Seaborn绘制条形图
        plt.figure(figsize=(12, 6))
        sns.barplot(x=province_counts.index, y=province_counts.values, color='skyblue')

        plt.title('样本中各省份的评论数量')
        plt.xlabel('省份')
        plt.ylabel('评论数')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('barChart.png')


