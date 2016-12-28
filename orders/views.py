from django.shortcuts import render, get_object_or_404, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import OrderCreated
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.http import HttpResponse


def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            # if cart.cupon:
            #     order.cupon = cart.cupon
            #     order.discount = cart.cupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()

            # Асинхронная отправка сообщения
            OrderCreated.delay(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))

    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})
