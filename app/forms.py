from django.forms import ModelForm, TextInput
from datetime import date
from .models import Record

# 宣告一個 class 繼承 ModelForm
class RecordForm(ModelForm):
    # ModelForm 裡面有一個 sub class 用來定義這個 ModelForm 的屬性
    class Meta:
        model = Record
        fields = ['date','description','category','cash','balance_type']
        # 這個屬性允許針對特定的欄位做客製化的處理，傳 dict，key=欄位，value=要客製化的內容
        widgets = {
            # 代表 date 欄位要用 text input，裡面的 attrbute 再用一個 dict 做定義
            'date': TextInput(
                attrs={
                    # 欄位 id 為 datepicker1
                    'id': 'datepicker1',
                    # 預設會顯示今天
                    'value': date.today().strftime('%Y-%m-%d')
                }
            )
        }