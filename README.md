# 浪漫的表白墙网页

## 介绍
浪漫的表白墙网页

## 演示图片
![浪漫表白墙](https://gitee.com/huang-hai-deng/images/raw/master/10.png)

## 软件架构
```
confession_wall/
    app_biaobai/
        main/
            __init__.py    蓝图文件
            view.py
        static/            静态文件
            css/
            images/
            js
        templates/        模板文件
            index.html
        __init__           工厂函数
config.py
wsgi.py                    主程序
```


#### 安装教程

1.解压文件后，在命令行进入文件根目录:
```
cd confession_wall
```

2.使用python的pip3包管理器安装需要的库:
```
pip3 install -r requirements.txt
```

3.启动
```
flask run
```

4.如果你们想在局域网都可以访问，那就:
```
flask run -h 0.0.0.0 -p 5000
```
局域网访问要你的计算机IP地址，这个你可以百度windows怎么查看ip地址。

代码任意修改，欢迎贡献！

# 微信打赏二维码
![weixin_sm](https://gitee.com/huang-hai-deng/images/raw/master/weixin_sm.jpg)
