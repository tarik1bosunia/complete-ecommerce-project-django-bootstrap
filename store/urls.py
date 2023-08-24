from django.urls import path
from store.views import store_page_view

app_name = 'store'

urlpatterns = [
    path("", store_page_view, name="store_page")
]
