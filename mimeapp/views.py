from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
data="""<table>
  <tr>
    <th>Weekly</th>
    <th>Drawings</th>
  </tr>
  <tr>
    <td>march</td>
    <td>$100</td>
  </tr>
</table>"""
class HtmlView(View):
    def get(self,request):
        return HttpResponse(data,content_type="text/html")
class XmlView(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/xml")
class ExcelView(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/vnd.ms-excel")