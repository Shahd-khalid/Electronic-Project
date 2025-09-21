from django.shortcuts import render, get_object_or_404, redirect
from .models import Shop
from .forms import ShopForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# الصفحة الرئيسية (Home)
def home(request):
    shops = Shop.objects.all()
    return render(request, 'shops/home.html', {'shops': shops})

# قائمة المحلات
def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shops/shop_detail.html', {'shops': shops})

# تفاصيل المحل + المنتجات
def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'shops/shop_detail.html', {'shop': shop})

# إضافة محل (أدمن المنصة فقط)

def shop_create(request):
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)

            # ربط المالك
            owner_username = request.POST.get('owner_username')
            if owner_username:
                try:
                    owner_user = User.objects.get(username=owner_username)
                except User.DoesNotExist:
                    owner_user = User.objects.create_user(username=owner_username, password='defaultpass')
                shop.owner = owner_user

            # ربط المندوب
            delivery_username = request.POST.get('delivery_username')
            if delivery_username:
                try:
                    delivery_user = User.objects.get(username=delivery_username)
                except User.DoesNotExist:
                    delivery_user = User.objects.create_user(username=delivery_username, password='defaultpass')
                shop.delivery_person = delivery_user

            shop.save()
            return redirect('shop_list')
    else:
        form = ShopForm()
    return render(request, 'shops/shop_form.html', {'form': form})


# تعديل محل (أدمن المنصة فقط)
def shop_update(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop_detail', pk=shop.pk)
    else:
        form = ShopForm(instance=shop)
    return render(request, 'shops/shop_form.html', {'form': form})

# حذف محل (أدمن المنصة فقط)
def shop_delete(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == 'POST':
        shop.delete()
        return redirect('shop_list')
    return render(request, 'shops/shop_confirm_delete.html', {'shop': shop})


#@login_required
#def owner_dashboard(request):
   # shop = request.user.shop  # جلب المتجر المرتبط بالمستخدم
   # products = shop.products.all()  # جميع المنتجات الخاصة بالمتجر
   # return render(request, 'shops/owner_dashboard.html', {'shop': shop, 'products': products})