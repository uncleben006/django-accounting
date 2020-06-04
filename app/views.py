from django.shortcuts import render, HttpResponse
from .models import Record

# Create your views here.
def hello(request):
    return render(request,'app/hello.html',{})

def index(request):
    records = Record.objects.filter()
    income_list = [record.cash for record in records if record.balance_type == '收入']
    outcome_list = [record.cash for record in records if record.balance_type == '支出']
    income = sum(income_list) if len(income_list) != 0 else 0
    outcome = sum(outcome_list) if len(outcome_list) != 0 else 0
    net = income - outcome

    # locals() 會直接 load 進這個 method 裡宣告的所有變數
    return render(request,'app/index.html',locals())
