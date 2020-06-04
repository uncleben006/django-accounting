from django.shortcuts import render, HttpResponse, redirect
from .models import Record, Category
from .forms import RecordForm

# Create your views here.
def hello(request):
    return render(request,'app/hello.html',{})

def index(request):

    # 若要使用 ModelForm，直接 import 並且實例化
    # initial 可以讓屬性帶入預設值
    record_form = RecordForm(initial={'balance_type':'支出','category':'1'})

    records = Record.objects.filter()
    income_list = [record.cash for record in records if record.balance_type == '收入']
    outcome_list = [record.cash for record in records if record.balance_type == '支出']
    income = sum(income_list) if len(income_list) != 0 else 0
    outcome = sum(outcome_list) if len(outcome_list) != 0 else 0
    net = income - outcome

    # locals() 會直接 load 進這個 method 裡宣告的所有變數
    return render(request,'app/index.html',locals())

def settings(request):
    categories = Category.objects.filter()
    return render(request,'app/settings.html',locals())

def addRecord(request):
    if request.method == 'POST':
        # ModelForm 我們可以直接賦予它 dict，相當於賦予它一個值
        form = RecordForm(request.POST)
        # 這裡可以做一些客製的驗證
        if form.is_valid():
            form.save()
    return redirect('/')

def deleteRecord(request):
    if request.method == 'POST':
        id = request.POST['delete_val']
        Record.objects.filter(id=id).delete()

    return redirect('/')
