import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns


class polylineChartGenerator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path, encoding='gbk', parse_dates=['评论时间'])
        # Set the Seaborn dark style
        sns.set(style="dark")
        # 指定中文字体
        self.font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)

    def generate_poly_line_chart(self):
        # 提取评论时间列的年月日小时部分
        self.df['评论时间'] = pd.to_datetime(self.df['评论时间'])
        self.df['日期'] = self.df['评论时间'].dt.strftime('%Y-%m-%d %H:00:00')

        # 对相同日期的评论数进行统计
        date_comment_count = self.df.groupby('日期').size()

        # 生成折线图
        plt.figure(figsize=(10, 6))  # 创建画布并指定尺寸

        plt.grid(axis='both', linestyle='-', alpha=0.7, color="grey")  # 设置网格线,alpha用于设置线的透明度

        date_comment_count.plot(kind='line', marker='o', markersize=8, color='orange', linestyle='-', linewidth=2)

        plt.title('评论数随日期变化趋势', fontproperties=self.font, fontsize=16)  # 使用中文字体，增加标题字体大小
        plt.xlabel('日期', fontproperties=self.font, fontsize=12)  # 使用中文字体，增加横轴标签字体大小
        plt.ylabel('评论数', fontproperties=self.font, fontsize=12)  # 使用中文字体，增加纵轴标签字体大小

        # 手动设置刻度，显示每个小时
        plt.xticks(range(len(date_comment_count.index)), date_comment_count.index, rotation=30, ha='right',
                   fontproperties=self.font, fontsize=10)  # 调整刻度字体大小

        # 增加图例
        plt.legend(['评论数'], loc='upper right', prop=self.font)

        # 增加网格线
        plt.grid(True, linestyle='--', alpha=0.5)

        plt.tight_layout()
        plt.show()
        # 保存图片
        plt.savefig("polyLine.png")


if __name__ == "__main__":
    chart = polylineChartGenerator("weibocomments.csv")
    chart.generate_poly_line_chart()
