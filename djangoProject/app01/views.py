import json

import json


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import app01.models

from django.http import HttpResponse
from django.core import serializers
# Create your views here.
from app01 import models


# python manage.py runserver 192.168.123.8:8000

def index(request):
    return HttpResponse("Welcome!!")


# 水资源
def shuiziyuan(request):
    year = models.water_resource.objects.values().filter(水资源总量_亿立方米_field__isnull=False).first().get('年份')
    szy = models.water_resource.objects.filter(年份=year)
    data = serializers.serialize("json", szy, ensure_ascii=False)
    return HttpResponse(data, content_type='application/json; charset=utf-8')

    # all_water = models.water_resource.objects.filter(年份 = '2020' ) #最近年份
    #
    # all_water_data = [{'省份','水资源总量(亿立方米)','地表水资源量(亿立方米)','地下水资源量(亿立方米)','地表水与地下水资源重复量(亿立方米)','人均水资源量(立方米 / 人)'}]

    # list_dict = all_water.values()
    # print(all_water)
    # for obj in all_water:
    #     print(obj.id,obj.省份 ,obj.人均水资源量_立方米_人_field,obj.地下水资源量_亿立方米_field)
        # print(obj.value)

    # print(list_dict)    #111
    # ret_list = list(list_dict)
    # return HttpResponse(ret_list, safe=False)

    # data = serializers.serialize("json", all_water,ensure_ascii=False)
    # return HttpResponse(data, content_type='application/json; charset=utf-8')

    # return HttpResponse("hunan ziyuan data")
#


# # 供用水情况
# def gongyongshui(request):
#     year = models.water_supply.objects.values().filter(供水总量_亿立方米_field__isnull=False).first().get('年份')
#     # a = models.water_supply.objects.first()
#     # print(year)
#     gysqk = models.water_supply.objects.filter(年份=year)
#     data = serializers.serialize("json", gysqk, ensure_ascii=False)
#     return HttpResponse(data, content_type='application/json; charset=utf-8')
#
# # 运输线路长度
# def yunshuluxian(request):
#     year = models.transportation_route.objects.values().filter(内河航道里程_万公里_field__isnull = False).first().get('年份')
#     ysxlcd = models.transportation_route.objects.filter(年份=year)
#     data = serializers.serialize("json", ysxlcd, ensure_ascii=False)
#     return HttpResponse(data, content_type='application/json; charset=utf-8')
#
#
# # 货运量
# def huoyun(request):
#     year = models.freight_transport.objects.values().filter(货运量_万吨_field__isnull=False).first().get('年份')
#     hyl = models.freight_transport.objects.filter(年份=year)
#     data = serializers.serialize("json", hyl, ensure_ascii=False)
#     return HttpResponse(data, content_type='application/json; charset=utf-8')
#
# # 客运量
# def keyun(request):
#     year = models.passenger_volume.objects.values().filter(客运量_万人_field__isnull=False).first().get('年份')
#     kyl = models.passenger_volume.objects.filter(年份=year)
#     data = serializers.serialize("json", kyl, ensure_ascii=False)
#     return HttpResponse(data, content_type='application/json; charset=utf-8')
#
# # 森林资源
# def senlinziyuan(request):
#     year = models.forest_resources.objects.values().filter(林业用地面积_万公顷_field__isnull=False).first().get('年份')
#     slzy = models.forest_resources.objects.filter(年份=year)
#     data = serializers.serialize("json", slzy, ensure_ascii=False)
#     return HttpResponse(data, content_type='application/json; charset=utf-8')
#
# # 造林面积
#
# def zaolinmianji(request):
#     year = models.afforestation_area.objects.values().filter(造林总面积_千公顷_field__isnull=False).first().get('年份')
#     zlmj = models.afforestation_area.objects.filter(年份=year)
#     data = serializers.serialize("json", zlmj, ensure_ascii=False)
#     return HttpResponse(data, content_type='application/json; charset=utf-8')
#
# # 有色金属非金属
# def yousefeijinshu(request):
#     year = models.non_ferrous_metals.objects.values().filter(铜矿储量_万吨_field__isnull=False).first().get('年份')
#     ysjs = models.non_ferrous_metals.objects.filter(年份=year)
#     data = serializers.serialize("json", ysjs, ensure_ascii=False)
#     return HttpResponse(data, content_type='application/json; charset=utf-8')
#
#
#
# # 黑色金属能源
# def heisenengyuan(request):
#     year = models.Main_energy_ferrous_metal.objects.values().filter(石油储量_万吨_field__isnull=False).first().get('年份')
#     hsjs = models.Main_energy_ferrous_metal.objects.filter(年份=year)
#     data = serializers.serialize("json", hsjs, ensure_ascii=False)
#     return HttpResponse(data, content_type='application/json; charset=utf-8')
#



def ooap_lscl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(粮食产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '粮食产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_xlcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(夏收粮食产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '夏收粮食产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_qlcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(秋粮产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '秋粮产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_dgcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(稻谷产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '稻谷产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_xmcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(小麦产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '小麦产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_ymcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(玉米产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '玉米产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_gzcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(谷子产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '谷子产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_glcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(高粱产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '高粱产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_qtgwcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(其他谷物产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '其他谷物产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_ldcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(绿豆产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '绿豆产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_hxdcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(红小豆产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '红小豆产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_ddcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(大豆产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '大豆产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_mlscl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(马铃薯产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '马铃薯产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_mhcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(棉花产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '棉花产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_hscl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(花生产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '花生产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_yczcl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(油菜籽产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '油菜籽产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap_sccl(request):
    model = models.Output_of_agricultural_products.objects
    year = model.values().filter(蔬菜产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份', '年份', '蔬菜产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')






def ca_nzwzmj2020(request):
    model = models.Crop_area.objects
    # year = model.values().filter(粮食单位面积产量_公斤_公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份='2020').values('省份','年份','农作物总播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_nzwzmj2019(request):
    model = models.Crop_area.objects
    # year = model.values().filter(粮食单位面积产量_公斤_公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份='2019').values('省份','年份','农作物总播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_nzwzmj2018(request):
    model = models.Crop_area.objects
    # year = model.values().filter(粮食单位面积产量_公斤_公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份='2018').values('省份','年份','农作物总播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_nzwzmj2017(request):
    model = models.Crop_area.objects
    # year = model.values().filter(粮食单位面积产量_公斤_公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份='2017').values('省份','年份','农作物总播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_nzwzmj2016(request):
    model = models.Crop_area.objects
    # year = model.values().filter(粮食单位面积产量_公斤_公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份='2016').values('省份','年份','农作物总播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_lsmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(粮食作物播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','粮食作物播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_xlmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(夏收粮食播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','夏收粮食播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_qlmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(秋收粮食播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','秋收粮食播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_dgmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(稻谷播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','稻谷播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_xmmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(小麦播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','小麦播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_ymmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(玉米播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','玉米播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_gzmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(谷子播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','谷子播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_glmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(高粱播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','高粱播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_qtgwmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(其他谷物播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','其他谷物播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_ldmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(绿豆播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','绿豆播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_hxdmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(红小豆播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','红小豆播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_ddmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(大豆播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','大豆播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_mlsmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(马铃薯播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','马铃薯播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')


def ca_mhmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(棉花播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','棉花播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_hsmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(花生播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','花生播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_yczmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(油菜籽播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','油菜籽播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ca_scmj(request):
    model = models.Crop_area.objects
    year = model.values().filter(蔬菜播种面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','蔬菜播种面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')





def oofp_mccl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(木材产量_万立方米_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','木材产量_万立方米_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oofp_xjcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(橡胶产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','橡胶产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oofp_szcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(松脂产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','松脂产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oofp_sqcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(生漆产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','生漆产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oofp_ytzcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(油桐籽产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','油桐籽产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oofp_cyzcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(油茶籽产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','油茶籽产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oofp_wjzcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(乌桕籽产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','乌桕籽产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oofp_wbzcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(五倍籽产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','五倍籽产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oofp_zpcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(棕片产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','棕片产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oofp_zspcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(竹笋片产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','竹笋片产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oofp_zjcl(request):
    model = models.Output_of_forest_products.objects
    year = model.values().filter(紫胶产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','紫胶产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')




def ec_yxggl2016(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(有效灌溉面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=2016).values('省份','年份','有效灌溉面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')
def ec_yxggl2017(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(有效灌溉面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=2017).values('省份','年份','有效灌溉面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')
def ec_yxggl2018(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(有效灌溉面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=2018).values('省份','年份','有效灌溉面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')
def ec_yxggl2019(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(有效灌溉面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=2019).values('省份','年份','有效灌溉面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')
def ec_yxggl2020(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(有效灌溉面积_千公顷_field__isnull=False).first().get('年份')
    data = model.filter(年份=2020).values('省份','年份','有效灌溉面积_千公顷_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ec_nyhfsyzcl2016(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农用化肥施用折纯量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=2016).values('省份','年份','农用化肥施用折纯量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')
def ec_nyhfsyzcl2017(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农用化肥施用折纯量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=2017).values('省份','年份','农用化肥施用折纯量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')
def ec_nyhfsyzcl2018(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农用化肥施用折纯量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=2018).values('省份','年份','农用化肥施用折纯量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')
def ec_nyhfsyzcl2019(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农用化肥施用折纯量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=2019).values('省份','年份','农用化肥施用折纯量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')
def ec_nyhfsyzcl2020(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农用化肥施用折纯量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=2020).values('省份','年份','农用化肥施用折纯量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ec_ncydl2016(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农村用电量_亿千瓦小时_field__isnull=False).first().get('年份')
    data = model.filter(年份=2016).values('省份','年份','农村用电量_亿千瓦小时_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')
def ec_ncydl2017(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农村用电量_亿千瓦小时_field__isnull=False).first().get('年份')
    data = model.filter(年份=2017).values('省份','年份','农村用电量_亿千瓦小时_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')
def ec_ncydl2018(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农村用电量_亿千瓦小时_field__isnull=False).first().get('年份')
    data = model.filter(年份=2018).values('省份','年份','农村用电量_亿千瓦小时_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')
def ec_ncydl2019(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农村用电量_亿千瓦小时_field__isnull=False).first().get('年份')
    data = model.filter(年份=2019).values('省份','年份','农村用电量_亿千瓦小时_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')
def ec_ncydl2020(request):
    model = models.Electricity_consumption.objects
    year = model.values().filter(农村用电量_亿千瓦小时_field__isnull=False).first().get('年份')
    data = model.filter(年份=2020).values('省份','年份','农村用电量_亿千瓦小时_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')





def ooap1_scpzcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(水产品总产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','水产品总产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap1_blcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(捕捞产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','捕捞产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap1_yzcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(养殖产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','养殖产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap1_ylcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(鱼类产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','鱼类产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap1_xxlcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(虾蟹类产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','虾蟹类产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap1_blcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(贝类产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','贝类产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap1_zlcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(藻类产量_吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','藻类产量_吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap1_hscpcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(海水产品产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','海水产品产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def ooap1_dscpcl(request):
    model = models.Output_of_aquatic_products.objects
    year = model.values().filter(淡水产品产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','淡水产品产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')




def lo_zclsl(request):
    model = models.Livestock_output.objects
    year = model.values().filter(猪出栏数量_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','猪出栏数量_万头_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def lo_nclsl(request):
    model = models.Livestock_output.objects
    year = model.values().filter(牛出栏数量_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','牛出栏数量_万头_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def lo_yclsl(request):
    model = models.Livestock_output.objects
    year = model.values().filter(羊出栏数量_万只_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','羊出栏数量_万只_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def lo_jqcll(request):
    model = models.Livestock_output.objects
    year = model.values().filter(家禽出栏量_万只_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','家禽出栏量_万只_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')



def lr_dscndts(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(大牲畜年底头数_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','大牲畜年底头数_万头_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def lr_nqmsl(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(牛期末数量_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','牛期末数量_万头_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def lr_mqmsl(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(马期末数量_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','马期末数量_万头_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def lr_lqmsl(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(驴期末数量_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','驴期末数量_万头_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def lr_luoqmsl(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(骡期末数量_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','骡期末数量_万头_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def lr_zndts(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(猪年底头数_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','猪年底头数_万头_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def lr_yndzs(request):
    model = models.Livestock_raising.objects
    year = model.values().filter(羊年底只数_万头_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','羊年底只数_万头_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')






def oolp_rlcl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(肉类产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','肉类产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oolp_zrcl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(猪肉产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','猪肉产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oolp_nrcl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(牛肉产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','牛肉产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oolp_yrcl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(羊肉产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','羊肉产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oolp_nncl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(牛奶产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','牛奶产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oolp_qdcl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(禽蛋产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','禽蛋产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def oolp_fmcl(request):
    model = models.Output_of_livestock_products.objects
    year = model.values().filter(蜂蜜产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','蜂蜜产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')



def tafy_sgcl(request):
    model = models.Tea_and_fruit_yield.objects
    year = model.values().filter(水果产量_万吨_field__isnull=False).first().get('年份')
    data = model.filter(年份=year).values('省份','年份','水果产量_万吨_field')
    return HttpResponse(data, content_type='application/json; charset=utf-8')
