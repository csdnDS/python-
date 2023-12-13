# 该项目的使用说明

## 包含的库

PySide6：用于调用Qt写的界面代码，该项目的界面组件是用Qt Designer实现的，然后运用pyside6-uic工具将.ui的界面文件转化为.py的python文件。

> `pyside6-uic mainwindow.ui > ui_mainwindow.py`

matploylib：使用该库生成图表。

pandas：使用该库实现文件数据的读取。

注：在运行代码之前要确保安装这些库。

## 运行方法

在window.py文件中点击运行按钮，在弹出的对话框中填入从网页上获取的微博url，点击界面中的生成按钮开始爬取数据生成图表。

## 运行界面展示
![image](https://github.com/csdnDS/python-/assets/98262598/9914f4f5-8e26-45b6-a0b3-b86feda9583d)
![image](https://github.com/csdnDS/python-/assets/98262598/77cca7d4-b307-4043-9a4e-bc787ee71b47)









