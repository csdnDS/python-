# coding: utf-8

import jieba
import pandas as pd
import stylecloud


class wordCloudGenerator:
    def __init__(self, file_path, stopwords_path='stopwords.txt', font_path='simhei.ttf',
                 icon_name='fas fa-cloud', size=768, max_font_size=145, background_color='white'):
        self.file_path = file_path
        self.stopwords_path = stopwords_path
        self.font_path = font_path
        self.icon_name = icon_name
        self.size = size
        self.max_font_size = max_font_size
        self.background_color = background_color

    def get_cut_words(self, content):
        stop_words = []
        with open(self.stopwords_path, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                stop_words.append(line.strip())
        word_num = jieba.lcut(content, cut_all=False)
        word_num_selected = [i for i in word_num if i not in stop_words and len(i) >= 1]
        return word_num_selected

    def generate_word_cloud_chart(self, output_name='wordcloud.png'):
        df = pd.read_csv(self.file_path, usecols=['评论内容'], encoding='gbk', converters={'评论内容': str})

        # 将所有评论合并成一个字符串
        all_comments = ''.join(df['评论内容'])

        # 获取分词结果
        text = self.get_cut_words(all_comments)

        # 生成词云图
        stylecloud.gen_stylecloud(
            text=' '.join(text),
            collocations=False,
            font_path=self.font_path,
            icon_name=self.icon_name,
            size=self.size,
            output_name=output_name,
            max_font_size=self.max_font_size,
            background_color=self.background_color
        )
