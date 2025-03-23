# 导入系统模块
import sys
# 导入PyQt5的QApplication和QWidget类
#from PyQt5.QtWidgets import QApplication, QWidget
#使用别名（alias）导入整个PyQt5.QtWidgets模块
#通过别名和点操作符（.）来访问模块中的类或函数。例如：qw.QApplication和qw.QWidget。
import PyQt5.QtWidgets as qw

# 导入自定义的serial_ui模块
import serial_ui

# 主程序入口
if __name__ == "__main__":
    # 创建QApplication实例，sys.argv传递命令行参数
    app = QApplication(sys.argv)
    # 创建主窗口QWidget实例
    w = QWidget()
    # 创建serial_ui模块中的Ui_serial实例
    ui = serial_ui.Ui_serial()
    # 调用setupUi方法初始化UI
    ui.setupUi(w)
    # 显示主窗口
    w.show()
    # 进入主事件循环，程序退出时返回退出状态码
    sys.exit(app.exec())
