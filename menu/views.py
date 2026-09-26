from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import MenuItem
from .serializers import MenuItemPublicSerializer, MenuItemAdminSerializer


# ---------- TV uchun ochiq API ----------
class TVMenuAPIView(APIView):
    """Smart TV shu manzildan taomlarni oladi — faqat is_active=True bo'lganlari"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        items = MenuItem.objects.filter(is_active=True)
        serializer = MenuItemPublicSerializer(items, many=True, context={'request': request})
        return Response(serializer.data)


def tv_display_view(request):
    return render(request, 'menu/tv_display.html')


# ---------- Mobil panel uchun API (toggle) ----------
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemAdminSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        item = self.get_object()
        item.is_active = not item.is_active
        item.save()
        return Response({'id': item.id, 'is_active': item.is_active})


# ---------- Login / logout ----------
def mobile_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mobile_panel')
        return render(request, 'menu/mobile_login.html', {'error': 'Login yoki parol xato'})
    return render(request, 'menu/mobile_login.html')


def mobile_logout_view(request):
    logout(request)
    return redirect('mobile_login')


# ---------- Mobil panel sahifalari ----------
@login_required(login_url='mobile_login')
def mobile_panel_view(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/mobile_panel.html', {'items': items})


@login_required(login_url='mobile_login')
def add_item_view(request):
    if request.method == 'POST':
        MenuItem.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price') or 0,
            image=request.FILES.get('image'),
            order=request.POST.get('order') or 0,
        )
        return redirect('mobile_panel')
    return render(request, 'menu/item_form.html', {'item': None})


@login_required(login_url='mobile_login')
def edit_item_view(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.price = request.POST.get('price') or 0
        item.order = request.POST.get('order') or 0
        if request.FILES.get('image'):
            item.image = request.FILES.get('image')
        item.save()
        return redirect('mobile_panel')
    return render(request, 'menu/item_form.html', {'item': item})


@login_required(login_url='mobile_login')
def delete_item_view(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        item.delete()
    return redirect('mobile_panel')
