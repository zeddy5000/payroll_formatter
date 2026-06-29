from django.urls import path

from .views import (
    upload_view,
    download_csv,
    download_xlsx,
    download_xls,
)

urlpatterns = [
    path(
        "",
        upload_view,
        name="upload"
    ),

    path(
        "download/csv/<str:file_id>/",
        download_csv,
        name="download_csv"
    ),

    path(
        "download/xlsx/<str:file_id>/",
        download_xlsx,
        name="download_xlsx"
    ),

    path(
        "download/xls/<str:file_id>/",
        download_xls,
        name="download_xls"
    ),
]