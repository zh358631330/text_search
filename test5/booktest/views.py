
# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from models import *
import os
from django.conf import settings
from models import PicTest, Areas
from django.core.paginator import Paginator
from django.core.mail import send_mail
import time
# Create your views here.

def index(request):
    return render(request,'booktest/index.html')


def jingtai(request):
    return render(request,'booktest/jingtai.html')

def area1(request):
    return render(request,'booktest/area1.html')

def sheng(request):
    list  = Areas.objects.filter(pid__isnull=True)
    # [ [] [] []]
    shenglist = []
    for sheng in list:
        shenglist.append([sheng.aid,sheng.atitle])
    context = {'sheng':shenglist}
    return JsonResponse(context)

def shi(request):
    id = request.GET.get('pid')
    list = Areas.objects.filter(pid=id)
    resault = []
    #{'id':'i.id','title':'zhengzhou'}
    for i in list:
        resault.append({'id':i.aid,'title':i.atitle})
        #resault.append([i.aid,i.atitle])
    context={'resault':resault}
    return JsonResponse(context)

def pic_upload(request):
    return render(request,'booktest/pic_upload.html')
def pic_handle(request):
    f1 = request.FILES.get('pic1')
    print(1)
    print(f1)
    path = os.path.join(settings.MEDIA_ROOT, 'booktest', f1.name)
    print path
    with open(path,'w') as pic:
        for p in f1.chunks():
            pic.write(p)
    pic1 = PicTest()
    pic1.pic='booktest/%s'%f1.name
    pic1.save()
    return HttpResponse('ok')

def pic_show(request):
    pic=PicTest.objects.get(pk=2)
    context = {'pic':pic}
    return render(request,'booktest/pic_show.html',context)

def page_test(request,pIndex):
    #查询所有的地区信息
    list1 = Areas.objects.filter(aid__isnull=False)
    #将地区信息按一页10条进行分页
    p = Paginator(list1, 10)
    #如果当前没有传递页码信息，则认为是第一页，这样写是为了请求第一页时可以不写页码
    if pIndex == '':
        pIndex = '1'
    #通过url匹配的参数都是字符串类型，转换成int类型
    pIndex = int(pIndex)
    #获取第pIndex页的数据
    list2 = p.page(pIndex)
    #获取所有的页码信息
    plist = p.page_range
    #将当前页码、当前页的数据、页码信息传递到模板中
    return render(request, 'booktest/page_test.html', {'list': list2, 'plist': plist, 'pIndex': pIndex})

def rich(request):
    return render(request,'booktest/rich.html')

def rich_handle(request):
    goods = GoodsInfo()
    goods.gcontent=request.POST.get('rich')
    goods.save()
    return HttpResponse('ok')

def rich_show(request):
    goods = GoodsInfo.objects.get(pk=1)
    context={'goods':goods}
    return render(request,'booktest/rich_show.html',context)

def query(request):
    return render(request,'booktest/query.html')

def mail_test(request):
    send_mail('注册激活','',
              settings.EMAIL_FROM,
              ['zh358631330@163.com'],
              html_message='<a href="#">点击激活</a>')
    return HttpResponse('邮箱确认信息已发送,请确认')
import task
def sayhello(request):
    # print 'hello'
    # time.sleep(4)
    # print 'world'
    task.task1.delay()
    return HttpResponse('ok')









