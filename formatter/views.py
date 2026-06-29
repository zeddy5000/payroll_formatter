from io import BytesIO
from io import StringIO
from uuid import uuid4

import pandas as pd

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

from .forms import UploadFileForm
from .services import process_file


def upload_view(request):

    if request.method == "POST":

        form = UploadFileForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            file = request.FILES["file"]

            output_df = process_file(file)

            file_id = str(uuid4())

            cache.set(
                file_id,
                output_df.to_json(
                    orient="records"
                ),
                timeout=3600
            )

            preview = output_df.head(
                50
            ).to_html(
                classes="table table-bordered",
                index=False
            )

            return render(
                request,
                "formatter/preview.html",
                {
                    "preview": preview,
                    "file_id": file_id,
                },
            )

    else:

        form = UploadFileForm()

    return render(
        request,
        "formatter/upload.html",
        {
            "form": form,
        },
    )


def download_csv(request, file_id):

    json_data = cache.get(file_id)

    if not json_data:
        return HttpResponse(
            "Session expired.",
            status=404
        )

    df = pd.read_json(
        StringIO(json_data),
        orient="records"
    )

    response = HttpResponse(
        content_type="text/csv"
    )

    response[
        "Content-Disposition"
    ] = (
        'attachment; filename="payroll.csv"'
    )

    df.to_csv(
        response,
        index=False
    )

    return response


def download_xlsx(request, file_id):

    json_data = cache.get(file_id)

    if not json_data:
        return HttpResponse(
            "Session expired.",
            status=404
        )

    df = pd.read_json(
        StringIO(json_data),
        orient="records"
    )

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False
        )

    output.seek(0)

    response = HttpResponse(
        output.read(),
        content_type=(
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ),
    )

    response[
        "Content-Disposition"
    ] = (
        'attachment; filename="payroll.xlsx"'
    )

    return response


def download_xls(request, file_id):

    return download_xlsx(
        request,
        file_id
    )