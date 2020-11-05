from django import forms
from .models import Icon


class IconForm(forms.ModelForm):
    class Meta:
        model = Icon
        # fields = '__all__'
        fields = ('icon_name', 'address', 'lat','lon','memo')
        labels = {
            'icon_name': 'アイコン名称',
            'address': '所在地',
            'lat':'緯度',
            'lon':'経度',
            'memo': 'メモ',
        }
        help_texts = {
            'icon_name': 'アイコン名を入力',
            'address': '住所を入力',
            'lat': '緯度',
            'lon': '経度',
            'memo': 'メモ',
        }


