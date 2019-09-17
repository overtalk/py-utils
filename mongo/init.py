# encoding=utf-8

import pymongo


class Config:
    host = ''
    port = ''
    db = ''

    def __init__(self, db, host='127.0.0.1', port=27017):
        self.db = db
        self.port = port
        self.host = host


class MongoDB:
    config = Config
    db = pymongo.MongoReplicaSetClient

    def __init__(self, c):
        self.config = c
        self.db = pymongo.MongoClient(host=c.host, port=c.port)[c.db]

    def insert(self, table, *items):
        self.db[table].insert_many(items)

    def find_one(self, table, **conditions):
        result = self.db[table].find_one(conditions)
        print(result)

    def find(self, table, **conditions):
        results = self.db[table].find(conditions)
        for result in results:
            print(result)

    def update(self, table, conditions, update):
        results = self.db[table].update_one(conditions, update)
        print(results)

    def del_one(self, table, conditions):
        results = self.db[table].delete_one(conditions)
        print(results)


def main():
    config = Config(db='test')
    mongo = MongoDB(c=config)
    # 插入数据
    student1 = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male'
    }

    student2 = {
        'id': '20170202',
        'name': 'Mike',
        'age': 21,
        'gender': 'male'
    }

    table = 'bbb'
    items = [student1, student2]
    mongo.insert(table, *items)

    # 查询数据
    conditions = {"age": 20}
    mongo.find_one(table, **conditions)
    mongo.find(table, **conditions)

    # 修改数据
    condition = {'name': 'Mike'}
    student = {'$set': {"age": 100}}
    mongo.update(table, condition, student)

    # 删除数据
    condition = {'name': 'Mike'}
    mongo.del_one(table, condition)


if __name__ == '__main__':
    main()
