#-*- coding:utf8 -*-
from base.readConfig import ReadConfig
from init.init import init
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.remote.command import Command
import argparse
import pytest
import sys
import jpype

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-k','--keyword',help='只执行匹配关键字的用例，会匹配文件名、类名、方法名',type=str)
    parser.add_argument('-d','--dir',help='指定要测试的目录',type=str)
    args=parser.parse_args()

    print '开始初始化......'

    print '初始化基础数据......'
    init()
    print '初始化基础数据完成......'
    print '初始化完成......'

    print '开始测试......'
    # 执行pytest前的参数准备
    pytest_execute_params=['-c', 'config/pytest.conf', '-v', '--alluredir', 'output/','-n',ReadConfig().config.test_workers,'--dist','loadfile']
    # 判断目录参数
    dir = 'cases'
    if args.dir:
        dir=args.dir
    # 判断关键字参数
    if args.keyword:
        pytest_execute_params.append('-k')
        pytest_execute_params.append(args.keyword)
    pytest_execute_params.append(dir)

    exit_code=pytest.main(pytest_execute_params)
    
    print '清除未被关闭的浏览器......'
    try:
        conn=RemoteConnection(ReadConfig().config.selenium_hub,True)
        sessions=conn.execute(Command.GET_ALL_SESSIONS,None)
        sessions=sessions['value']
        for session in sessions:
            session_id=session['id']
            conn.execute(Command.QUIT,{'sessionId':session_id})
    except Exception,e:
        print '清除未关闭浏览器异常:\r\n'+e.message
    print '清除未被关闭的浏览器完成......'

    print '结束测试......'
    sys.exit(exit_code)
