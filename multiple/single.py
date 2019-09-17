from time import sleep,ctime


def music(name):
    for i in range(2):
        print("I am listening to %s . %s" % (name, ctime()))
        sleep(1)


def movie(name):
    for i in range(2):
        print("I am at the %s! %s" % (name, ctime()))
        sleep(1)


if __name__ == '__main__':
    music('掐')
    movie('m')
    print("all over %s" % ctime())
