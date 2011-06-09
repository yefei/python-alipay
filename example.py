# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect

import alipay


# django例子： alipay 回调接口
def alipay_notify(request):
    if request.method == 'POST':
        verify_result = notify_verify(request.POST) # 解码并验证数据是否有效
        if verify_result:
            tn = request.POST.get('out_trade_no')
            if request.POST.get('trade_status') in ('TRADE_FINISHED','TRADE_SUCCESS'):
                remark = u'使用支付宝 %s 充值，交易号: %s ' % (request.POST.get('buyer_email'), tn)
                print remark
            return HttpResponse('success') #有效数据需要返回 'success' 给 alipay
    return HttpResponse('fail') # 无效数据返回 'fail' 




if __name__ == "__main__":
    moneys = 100
    payurl = alipay.create_direct_pay_by_user('12345', u'充值测试', u'充值 %d 元' % moneys, moneys)
    # return HttpResponseRedirect(payurl)
    print payurl # 直接跳转到此 url 用户即可充值  用户充值成功后 alipay 将回调 alipay_notify





