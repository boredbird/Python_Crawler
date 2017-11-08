# coding=utf-8
import unittest
import requests

base_url = "http://sls.bqjr.cn:10004/ccs-web/App/rpc/customerFreezeServer/singleFreeze"
content_load = {'1|3|20|15|55|"210811198609092522""1509379200000""POS贷或交叉现金贷合同当前逾期大于10天"'}
r = requests.post(base_url, data=content_load)
result = r.json()
#
# assertEqual(result['status'], 10021)
# assertEqual(result['message'], 'parameter error')
