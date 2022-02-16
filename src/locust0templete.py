# -*- coding:utf-8 -*-

"""
# Author ：li zi hao
"""
import os

from locust import TaskSet, HttpLocust, between, task


class TestSuites(TaskSet):

    def on_start(self):
        """
        初始化方法，相当于setup或__init__函数
        :return:
        """
        print('开始执行！！！')

    def test_get_baidu(self):
        res = self.client
        if res.success():
            print('登录成功')

    def on_stop(self):
        """
        测试执行结束后，执行的方法，相当于teardown
        :return:
        """
        print('结束执行！！！')


class RunCase(HttpLocust):
    """
    压测类
    """
    task_set = TestSuites   # 指定测试套件    task_set固定
    wait_time = between(1, 3)   # 定义执行过程中随即等待时间区间


if __name__ == '__main__':
    os.system('locust -f locust0templete.py')
