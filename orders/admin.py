from django.contrib import admin
from .models import Order, OrderItem
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils.html import format_html
import datetime


def OrderDetail(obj):
    return format_html('<a href="{}">Посмотреть</a>'.format(
        reverse('orders:AdminOrderDetail', args=[obj.id])
    ))
OrderDetail.short_description = 'Инфо'



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'address','paid', 'created',
                    OrderDetail]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
