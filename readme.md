程序在main.py里

如要运行，安装Anaconda环境（python3.6），需要一些库

--安装命令：

打开Terminal或者cmd输入以下代码：

    OpenCV-PY: pip install opencv-python

    numPy: pip install numpy

--运行方式：
Terminal 或者 Cmd下输入以下代码

    python main.py
    
cell.py 里是比较简单的调色代码 可以忽略

主要使用的python库 Numpy, cv2. 可以在CSDN上查阅相关资料便于写论文。

主要使用的函数：  
    
    cv2.addWeighted(cell_img, 0.7, color_img, 0.6, -100)
    
    这个函数用于混色色库和纹理图案
    
    cv2.imread()图片读取
    cv2.resize()重新定义图片大小（此方式使用平均采样（缩小）和线性插值（扩大））
    cv2.show()显示图片