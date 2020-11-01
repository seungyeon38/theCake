from django import forms
from home.models import Store, Baker, Cake, DetailedOption

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['storeImg', 'storeName', 'storeContact', 'aboutStore', 'pickUpOpen', 'pickUpClose', 'sido', 'sigugun', 'dong', 'postcode', 'address1','address2', 'address3']
        widgets = {
            # label은 HTML에서 label태그를 의미
            # widget은 input이라고 생각
            # 예를 들어, TextInput은 <input type="text">를 의미
            # textarea 태그를 원하면 widget = forms.Textarea라고 설정하면 됨.
            # attrs={}안에 지정하고자 하는 class나 placeholder등을 부가적으로 설정(이 또한 HTML 엘리먼트의 속성)

            'storeName': forms.TextInput(
                #label='가게 이름',
                attrs={'class': 'form-control'}
            ),
            'storeContact': forms.TextInput(
                #label='가게 연락처',
                attrs={
                    'class': 'form-control',
                    'placeholder': '예) 02-1234-5678'
                }
            ),
            'pickUpOpen': forms.Select(
                #label='픽업 오픈 시간',
                attrs={'class': 'form-control'}
            ),
            'pickUpClose': forms.Select(
                #label='픽업 마감 시간',
                attrs={'class': 'form-control'}
            ),
            'aboutStore': forms.Textarea(
                #label='가게 소개글',
                attrs={'class': 'form-control'}
            ),
            'postcode': forms.TextInput(
                attrs={'id':'sample6_postcode',
                       'placeholder':"우편번호"}
            ),
            'address1': forms.TextInput(
                attrs={'id': 'sample6_address',
                       'placeholder':"주소"}
            ),
            'address2': forms.TextInput(
                attrs={'id': 'sample6_detailAddress',
                       'placeholder':"상세주소"}
            ),
            'address3': forms.TextInput(
                attrs={'id': 'sample6_extraAddress',
                       'placeholder':"참고항목"}
            ),
            'sido': forms.Select(
                attrs={'class': 'sido'}
            ),
            'sigugun': forms.Select(
                attrs={'class': 'sigugun'}
            ),
            'dong': forms.Select(
                attrs={'class': 'dong'}
            )
        }

class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ['cakeName', 'cakeImg', 'cakePrice', 'mini']
        widgets = {
            'cakeName': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '케이크 이름'
                }
            ),
            'cakePrice': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '케이크 가격(1호 기준)'
                }
            ),
            'mini': forms.RadioSelect()
        }

class DetailedOptionForm(forms.ModelForm):
    class Meta:
        model = DetailedOption
        fields = ['detailName', 'pricing', 'withColor', 'withImage']
        widgets = {
            'detailName' : forms.TextInput(
                attrs={'class': 'form-control', 'aria-label': 'cakeName'}
                # 여기를 이용해서 꾸며야 합니다.
            ),
            'pricing' : forms.TextInput(
                attrs={}
            ),
            'withColor' : forms.TextInput(
                attrs={}
            ),
            'withImage' : forms.TextInput(
                attrs={}
            )
        }