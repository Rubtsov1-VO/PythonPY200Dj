from django.urls import path
from landing.forms import TemplateForm
from .views import TemplView

urlpatterns = [
    path('', TemplView.as_view(), name='landing'),
    # TODO добавьте здесь маршрут для вашего обработчика отображения страницы приложения landing
]