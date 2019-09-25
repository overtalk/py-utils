#!/usr/bin/env bash

#建立虚拟环境
pipenv install
#进入虚拟环境
pipenv shell
#安装模块
pip install 小工具.py里面用到的模块
#打包的模块也要安装
pip install pyinstaller
#开始打包
pyinstaller -F ./main.py