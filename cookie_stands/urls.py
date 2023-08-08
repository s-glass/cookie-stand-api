from django.urls import path
from .views import CookieStandList, CookieStandDetail, CookieStandCreateView, CookieStandUpdateView, CookieStandDeleteView

urlpatterns = [
    path("", CookieStandList.as_view(), name="cookiestand_list"),
    path("<int:pk>", CookieStandDetail.as_view(), name="cookiestand_detail"),
    path("create/", CookieStandCreateView.as_view(), name="cookiestand_create"),
    path("<int:pk>/update/", CookieStandUpdateView.as_view(), name="cookiestand_update"),
    path("<int:pk>/delete/", CookieStandDeleteView.as_view(), name="cookiestand_delete"),
]



