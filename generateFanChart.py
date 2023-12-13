import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns


class fanChartGenerator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path, encoding='gbk')  # 确保不会因为读取的信息格式问题报错
        sns.set(style="dark")  # Set the Seaborn dark style

    def generate_fan_chart(self):
        # 提取省份信息的列
        province_column = '用户归属地'
        provinces = self.df[province_column]

        # 统计各个省份的出现次数
        province_counts = provinces.value_counts()

        # 取前五个省份
        top_five_provinces = province_counts.head(5)

        plt.figure(figsize=(8, 8))  # 设置图表的大小

        # 指定中文字体
        font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)

        # 用前五省份的数据生成扇形图
        top_five_provinces.plot(
            kind='pie',  # 指定图表类型为扇形图
            autopct='%1.1f%%',  # 显示百分比，并保留一位小数
            startangle=90,  # 设置起始角度为90度（从12点钟方向开始）
            counterclock=False,  # 设置为顺时针方向绘制扇形
            wedgeprops=dict(width=1),  # 设置扇形之间的间距（宽度）
            labels=None,  # 不显示默认的标签，由图例代替
        )

        plt.title('前五省份评论数占比', fontproperties=font)  # 使用中文字体
        # 添加图例，显示前五省份的名称
        plt.legend(
            labels=top_five_provinces.index,  # 图例显示的标签为前五省份的名称
            loc='upper right',  # 将图例放置在图表的右上角
            bbox_to_anchor=(1, 1),  # 调整图例位置，以避免覆盖图表内容
            prop=font  # 指定图例中文本的字体属性
        )

        plt.tight_layout()
        plt.savefig("fanChart.png")


