from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("""<html>
    <title>Сайт Станислава Яловкина</title>
    <h1>Станислав Яловкин</h1>
    </html>""")
