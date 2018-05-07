#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import hashlib

import json

work_path = '/Users/zhenhua.wang/PycharmProjects/test/'

dict_category_id = {"movie":"1","music":"3","tv_show":"2","short_video":"4"}
list_video_type = ['movie', 'music', 'tv_show', 'short_video']
json_index_type = {"index":{"_index":"mx_cms_v1","_type":"Genre"}}


def generate_md5(some_str):

    if isinstance(some_str, basestring):
        some_str = some_str
        str_md5 = hashlib.md5(some_str).hexdigest()
        return str_md5
    else:
        return ''

def getJsonFile(vide_type):
    json_doc = {}
    dict_genrename_id = {}
    category_id = dict_category_id[vide_type]
    file_json = open(work_path + vide_type + '_genres.json', 'w')
    file_csv = open(work_path + vide_type + '_genres.csv')
    for f in file_csv:
        #每行去掉结尾的'\r\n'，然后加上'，'号使格式统一
        list_f = (f.strip('\r\n') + ',').split(',')
        if list_f[1] == '':
            level = 1
            genre_name = list_f[0]
            genre_id = generate_md5(genre_name + category_id)
            #把一级标签的id存到字典里，后面二级标签读取到father字段里
            dict_genrename_id[genre_name] = genre_id
            json_index_type["index"]["_id"] = genre_id
            json_doc["level"] = level
            json_doc["genre_name"] = genre_name
            json_doc["father"] = ""
            json_doc["category_id"] = category_id

            file_json.write(json.dumps(json_index_type) + "\n")
            file_json.write(json.dumps(json_doc) + '\n')
        else:
            level = 2
            genre_name = list_f[1]
            #因为不同一级标签下会有同名的二级标签，所以二级标签的id应该加上一级标签前缀，生成不同的id，如id相同导入时可能会更改第一个二级标签father值
            genre_id = generate_md5(list_f[0] + genre_name + category_id)
            dict_genrename_id[genre_name] = genre_id
            json_index_type["index"]["_id"] = genre_id
            json_doc["level"] = level
            json_doc["genre_name"] = genre_name
            json_doc["father"] = dict_genrename_id[list_f[0]]
            json_doc["category_id"] = category_id

            file_json.write(json.dumps(json_index_type) + "\n")
            file_json.write(json.dumps(json_doc) + "\n")

    file_json.close()
    file_csv.close()


if __name__ == '__main__':

    getJsonFile('movie')
    #getJsonFile('music')
    #getJsonFile('tv_show')
    #getJsonFile('short_video')






