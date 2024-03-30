import xlsxwriter
import csv

from django.http import HttpResponse

from rest_framework import generics, views, status
from rest_framework.response import Response

from .serializers import GuestSerializer
from .models import Guest



class GuestView(generics.ListCreateAPIView):

    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = GuestSerializer(queryset, many=True)

        return Response(serializer.data)
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class ExportToExcel(views.APIView):

    def get(self, request):
        queryset = Guest.objects.all().values()

        # Create a new Excel workbook and add a worksheet
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
        workbook = xlsxwriter.Workbook(response)
        worksheet = workbook.add_worksheet()

        # Write header row
        header_row = ['name', 'email', 'phone']  # Replace with actual field names
        for col_num, field_name in enumerate(header_row):
            worksheet.write(0, col_num, field_name)

        # Write data rows
        for row_num, row_data in enumerate(queryset, start=1):
            for col_num, field_name in enumerate(header_row):
                worksheet.write(row_num, col_num, row_data.get(field_name, ''))

        workbook.close()
        return response
    

class ExportToCSV(views.APIView):
    def get(self, request):
        queryset = Guest.objects.all().values()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        writer = csv.writer(response)
        # Write header row
        writer.writerow(['Имя', 'Почта', 'Телефон'])  # Replace 'Field1', 'Field2', ... with actual field names

        for item in queryset:
            writer.writerow([item['name'], item['email'], item['phone']])  # Replace 'field1', 'field2', ... with actual field names

        return response