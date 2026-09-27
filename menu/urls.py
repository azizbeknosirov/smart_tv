from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r'items', views.MenuItemViewSet, basename='menuitem')

urlpatterns = [
    # Smart TV
    path('', views.tv_display_view, name='tv_display_home'),
    path('tv/', views.tv_display_view, name='tv_display'),
    path('api/tv-menu/', views.TVMenuAPIView.as_view(), name='tv_menu_api'),
    path('api/tv-settings/', views.TVSettingsAPIView.as_view(), name='tv_settings_api'),

    # API (Flutter ilovasi va mobil panel foydalanadi)
    path('api/auth/login/', obtain_auth_token, name='api_login'),
    path('api/', include(router.urls)),

    # Telefon boshqaruv paneli
    path('panel/', views.mobile_panel_view, name='mobile_panel'),
    path('panel/login/', views.mobile_login_view, name='mobile_login'),
    path('panel/logout/', views.mobile_logout_view, name='mobile_logout'),
    path('panel/add/', views.add_item_view, name='item_add'),
    path('panel/edit/<int:pk>/', views.edit_item_view, name='item_edit'),
    path('panel/delete/<int:pk>/', views.delete_item_view, name='item_delete'),

    # Mobil ilova uchun TV sozlamalari
    path('api/settings/background/', views.settings_background_view, name='settings_background'),
]
