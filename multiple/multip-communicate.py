# encoding=utf-8
import queue
from threading import Thread
from time import time, sleep


def get_detail_html(url_list, id):
    while True:
        try:
            url = url_list.get()
            sleep(0.1)  # 延时2s，模拟网络请求
            print("thread {id}: get {url} detail finished".format(id=id, url=url))
        except queue.Empty:
            print('the queue is closed')
            return


def get_detail_url(queue):
    # 模拟抓取10000个网页
    for index in range(100):
        sleep(0.1)  # 延时1s，模拟比爬取文章详情要快
        queue.put("http://projectedu.com/{id}".format(id=index))
        print("get detail url {id} end".format(id=index))


if __name__ == '__main__':
    # 构造多个线程之间通信所用的队列
    q = queue.Queue(maxsize=1000)

    # 构造两类线程
    # 第一类线程用于获取url
    url_thread = Thread(target=get_detail_url, args=(q,))
    # 第一类线程用于获取url的具体html
    html_thread = []
    for i in range(5):
        html_thread.append(Thread(target=get_detail_html, args=(q, i)))

    # 记录现在开始时间
    start_time = time()

    # 启动线程
    url_thread.start()
    for thread in html_thread:
        thread.start()

    # 等待所有线程结束
    url_thread.join()
    for thread in html_thread:
        thread.join()

    print("used time: {} s".format(time()-start_time))

