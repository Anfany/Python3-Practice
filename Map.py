# -*- coding：utf-8 -*-
# &Author  AnFany

import urllib.request as ur # WEB服务接口地址
import urllib.parse # URL中的中文转码
import json  # 读取内容

#  百度地图开发者中心注册后获得个人密钥

privatekey = '个人密钥'

#  根据中文地址获得相应的经纬度
def latlon(address, ak):
    base = 'http://api.map.baidu.com/geocoder/v2/?'
    add = urllib.parse.quote(address)  # 网址中出现中文，需要转码
    start = 'address=%s' % add
    end = 'output=json&'
    miyao = 'ak=%s' % ak
    url = base + start + '&' + end + miyao + '&callback=showLocation// '
    req = ur.urlopen(url)
    du = req.read()
    hjson = json.loads(du.decode('utf-8')) # jason形式需要转码
    return hjson['result']['location']  # 根据jason格式

#  根据经纬度获得驾车距离
def distance(add1, add2, ak):
    base = 'http://api.map.baidu.com/direction/v2/driving?'
    start = 'origin=%s,%s' % (add1[0], add1[1])
    end = 'destination=%s,%s' % (add2[0], add2[1])
    miyao = '&ak=%s' % ak
    url = base + start + '&' + end + miyao
    req = ur.urlopen(url)
    du = req.read()
    hjson = json.loads(du.decode('utf-8')) 
    return hjson['result']['routes'][0]['distance']  # 根据jason格式

#  最终的函数
def drive(address1, address2, ak=privatekey):
    jingwei1 = latlon(address1, ak)
    add1 = ['%.6f' % jingwei1['lat'], '%.6f' % jingwei1['lng']]  # 接口要求最多6位

    jingwei2 = latlon(address2, ak)
    add2 = ['%.6f' % jingwei2['lat'], '%.6f' % jingwei2['lng']]  # 接口要求最多6位

    juli = distance(add1, add2, ak)  # 获得驾车距离

    return '从\n%s\n到\n%s\n \n驾车距离约为 %.3f公里' % (address1, address2, juli / 1000)

#  最终的程序
if __name__ == "__main__":
    print(drive('入门', '放弃'))













