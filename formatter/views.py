from io import BytesIO

import pandas as pd

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

            output = BytesIO()

            with pd.ExcelWriter(
                output,
                engine="openpyxl"
            ) as writer:

                output_df.to_excel(
                    writer,
                    index=False
                )

            output.seek(0)

            response = HttpResponse(
                output.read(),
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

            response[
                "Content-Disposition"
            ] = (
                'attachment; filename="employees.xlsx"'
            )

            return response

    else:
        form = UploadFileForm()

    return render(
        request,
        "formatter/upload.html",
        {"form": form}
    )