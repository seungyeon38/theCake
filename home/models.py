from django.db import models
from django.core.validators import FileExtensionValidator

class Orderer(models.Model):
    userID = models.CharField(max_length=20, verbose_name='주문자 아이디',blank=False, primary_key=True,default="")
    email = models.EmailField(max_length=128, verbose_name='주문자 이메일',blank=False,null=True)
    name = models.CharField(max_length=30,verbose_name='주문자 이름',null=True,blank=False)
    phoneNum = models.CharField(max_length=30, verbose_name='주문자 전화번호',null=True,blank=False,unique=True)
    password = models.CharField(max_length=200, verbose_name='주문자 비밀번호',null=True,blank=False)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.userID

    class Meta:
        db_table = 'Orderer'
        verbose_name = '주문자'
        verbose_name_plural = '주문자'

class checkOrderer(models.Model):
    userid = models.CharField(max_length=20, verbose_name='주문자 아이디',blank=False, primary_key=True)

    def __str__(self):
        return self.userid

    class Meta:
        db_table = 'checkOrderer'
        verbose_name = '주문자 가입용'
        verbose_name_plural = '주문자 가입용'

class Baker(models.Model):
    userID = models.CharField(max_length=20, verbose_name='사업자 아이디', blank=False, primary_key=True,default="")
    businessID = models.CharField(max_length=10, verbose_name='사업자 등록번호', blank=False, null=True)
    email = models.EmailField(max_length=128, verbose_name='사업자 이메일', null=True, blank=False)  # unique=True,
    name = models.CharField(max_length=30, verbose_name='사업자 이름', null=True, blank=False)
    phoneNum = models.CharField(max_length=30, verbose_name='사업자 전화번호', null=True, blank=False)  # unique=True,
    password = models.CharField(max_length=200, verbose_name='사업자 비밀번호', null=True, blank=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.userID

    class Meta:
        db_table = 'Baker'
        verbose_name = '사업자'
        verbose_name_plural = '사업자'

class checkBaker(models.Model):
    userid = models.CharField(max_length=20, verbose_name='사업자 아이디', blank=False, primary_key=True,default="")
    businessCRN = models.CharField(max_length=10,verbose_name='사업자 등록번호',blank=False,null=True)

    def __str__(self):
        return self.userid

    class Meta:
        db_table = 'checkBaker'
        verbose_name = '사업자 가입용'
        verbose_name_plural = '사업자 가입용'

class Store(models.Model):
    TIME_CHOICES = [
        ('0', '9:00'), ('1', '9:30'), ('2', '10:00'), ('3', '10:30'), ('4', '11:00'),
        ('5', '11:30'),
        ('6', '12:00'), ('7', '12:30'), ('8', '13:00'), ('9', '13:30'), ('10', '14:00'),
        ('11', '14:30'),
        ('12', '15:00'), ('13', '15:30'), ('14', '16:00'), ('15', '16:30'), ('16', '17:00'),
        ('17', '17:30'),
        ('18', '18:00'), ('19', '18:30'), ('20', '19:00'), ('21', '19:30'), ('22', '20:00'),
        ('23', '20:30'),
        ('24', '21:00'), ('25', '21:30'), ('26', '22:00'), ('27', '22:30'),
    ]
    BANK_CHOICES = [
        ('1', '국민은행'), ('2', '기업은행'), ('3', '우리은행'), ('4', '농협은행'), ('5', '지역농축협'), ('6', '신한은행'),
        ('7', '씨티은행'), ('8', '카카오뱅크'), ('9', '케이뱅크'), ('10', '하나은행'), ('11', 'SC제일은행'),
        ('12', '경남은행'), ('13', '광주은행'), ('14', '대구은행'), ('15', '부산은행'), ('16', '산림조합은행'),
        ('17', '산업은행'), ('18', '저축은행'), ('19', '새마을금고'), ('20', '수협은행'), ('21', '신협은행'),
        ('22', '우체국은행'), ('23', '전북은행'), ('24', '제주은행'), ('25', '도이치은행'), ('26', '중국공상은행'),
        ('27', '중국건설은행'), ('28', '중국은행'), ('29', 'BOA'), ('30', 'HSBC'), ('31', 'JP모간'), ('32', 'BNP파리바')
    ]
    businessID = models.CharField(max_length=10, verbose_name='사업자 등록번호', blank=False, primary_key=True)
    manager = models.ForeignKey(Baker, on_delete=models.CASCADE,null=True)
    storeName = models.CharField(max_length=30, verbose_name='가게 이름', null=True, blank=True)
    location = models.CharField(max_length=200, verbose_name='가게 위치', null=True, blank=True) #나중에 blank False로 수정하기
    postcode = models.CharField(max_length=10, verbose_name='우편번호', null=True, blank=True)
    address1 = models.CharField(max_length=100, verbose_name='가게 주소', null=True, blank=True)
    address2 = models.CharField(max_length=100, verbose_name='가게 상세주소', null=True, blank=True)
    address3 = models.CharField(max_length=100, verbose_name='위치 추가정보', null=True, blank=True)
    daum_sido = models.CharField(max_length=20, verbose_name='주문자와 비교할 시/도', null=True, blank=True)
    daum_sigungu = models.CharField(max_length=20, verbose_name='주문자와 비교할 시/군/구', null=True, blank=True)
    daum_dong = models.CharField(max_length=20, verbose_name='주문자와 비교할 읍/면/동', null=True, blank=True)
    storeContact = models.CharField(max_length=30, verbose_name='가게 연락처', null=True, blank=True) #,unique=True
    pickUpOpen = models.CharField(max_length=15, verbose_name='픽업 오픈 시간',null=True, blank=True, choices=TIME_CHOICES)
    pickUpClose = models.CharField(max_length=15, verbose_name='픽업 마감 시간',null=True, blank=True, choices=TIME_CHOICES)
    aboutStore = models.TextField(verbose_name='가게 소개글', null=True, blank=True)
    storeImg = models.ImageField(verbose_name='가게 대표이미지', null=True, blank=True, default="logo_baker.png")
    aboutCake = models.TextField(verbose_name='케이크 소개글', null=True, blank=True)
    totalorder = models.IntegerField(verbose_name="전체 주문 수",null=True,default=0,blank=True)
    totalrate = models.FloatField(verbose_name="평점 평균",blank=True,default=0,null=True)
    bankname = models.CharField(max_length=15, verbose_name='은행',null=True, blank=True, choices=BANK_CHOICES)
    banknumber = models.CharField(max_length=20, verbose_name='계좌번호', null=True, blank=True)

    def __str__(self):
        return self.businessID

    class Meta:
        db_table = 'Store'
        verbose_name = '가게'
        verbose_name_plural = '가게'

class OpenDays(models.Model):
    businessID = models.CharField(max_length=10, verbose_name="사업자 등록번호", blank=False, primary_key=True, default="")
    monday = models.IntegerField(verbose_name="월요일 주문가능 수량",null=True,default=0,blank=True)
    tuesday = models.IntegerField(verbose_name="화요일 주문가능 수량",null=True,default=0,blank=True)
    wednesday = models.IntegerField(verbose_name="수요일 주문가능 수량",null=True,default=0,blank=True)
    thursday = models.IntegerField(verbose_name="목요일 주문가능 수량",null=True,default=0,blank=True)
    friday = models.IntegerField(verbose_name="금요일 주문가능 수량",null=True,default=0,blank=True)
    saturday = models.IntegerField(verbose_name="토요일 주문가능 수량",null=True,default=0,blank=True)
    sunday = models.IntegerField(verbose_name="일요일 주문가능 수량",null=True,default=0,blank=True)

    class Meta:
        db_table = 'openDays'
        verbose_name = '주문가능 수량'
        verbose_name_plural = '주문가능 수량'

class DailyAmount(models.Model):
    businessID = models.CharField(max_length=10, verbose_name="사업자 등록번호", blank=False, primary_key=True, default="")
    day1 = models.IntegerField(verbose_name="1일 수량",null=False,default=0,blank=False)
    day2 = models.IntegerField(verbose_name="2일 수량",null=False,default=0,blank=False)
    day3 = models.IntegerField(verbose_name="3일 수량",null=False,default=0,blank=False)
    day4 = models.IntegerField(verbose_name="4일 수량",null=False,default=0,blank=False)
    day5 = models.IntegerField(verbose_name="5일 수량",null=False,default=0,blank=False)
    day6 = models.IntegerField(verbose_name="6일 수량",null=False,default=0,blank=False)
    day7 = models.IntegerField(verbose_name="7일 수량",null=False,default=0,blank=False)
    day8 = models.IntegerField(verbose_name="8일 수량",null=False,default=0,blank=False)
    day9 = models.IntegerField(verbose_name="9일 수량",null=False,default=0,blank=False)
    day10 = models.IntegerField(verbose_name="10일 수량",null=False,default=0,blank=False)
    day11 = models.IntegerField(verbose_name="11일 수량",null=False,default=0,blank=False)
    day12 = models.IntegerField(verbose_name="12일 수량",null=False,default=0,blank=False)
    day13 = models.IntegerField(verbose_name="13일 수량",null=False,default=0,blank=False)
    day14 = models.IntegerField(verbose_name="14일 수량",null=False,default=0,blank=False)
    day15 = models.IntegerField(verbose_name="15일 수량",null=False,default=0,blank=False)
    day16 = models.IntegerField(verbose_name="16일 수량",null=False,default=0,blank=False)
    day17 = models.IntegerField(verbose_name="17일 수량",null=False,default=0,blank=False)
    day18 = models.IntegerField(verbose_name="18일 수량",null=False,default=0,blank=False)
    day19 = models.IntegerField(verbose_name="19일 수량",null=False,default=0,blank=False)
    day20 = models.IntegerField(verbose_name="20일 수량",null=False,default=0,blank=False)
    day21 = models.IntegerField(verbose_name="21일 수량",null=False,default=0,blank=False)
    day22 = models.IntegerField(verbose_name="22일 수량",null=False,default=0,blank=False)
    day23 = models.IntegerField(verbose_name="23일 수량",null=False,default=0,blank=False)
    day24 = models.IntegerField(verbose_name="24일 수량",null=False,default=0,blank=False)
    day25 = models.IntegerField(verbose_name="25일 수량",null=False,default=0,blank=False)
    day26 = models.IntegerField(verbose_name="26일 수량",null=False,default=0,blank=False)
    day27 = models.IntegerField(verbose_name="27일 수량",null=False,default=0,blank=False)
    day28 = models.IntegerField(verbose_name="28일 수량",null=False,default=0,blank=False)
    day29 = models.IntegerField(verbose_name="29일 수량",null=False,default=0,blank=False)
    day30 = models.IntegerField(verbose_name="30일 수량",null=False,default=0,blank=False)
    day31 = models.IntegerField(verbose_name="31일 수량",null=False,default=0,blank=False)
    day32 = models.IntegerField(verbose_name="32일 수량", null=False, default=0, blank=False)
    day33 = models.IntegerField(verbose_name="33일 수량", null=False, default=0, blank=False)
    day34 = models.IntegerField(verbose_name="34일 수량", null=False, default=0, blank=False)
    day35 = models.IntegerField(verbose_name="35일 수량", null=False, default=0, blank=False)
    day36 = models.IntegerField(verbose_name="36일 수량", null=False, default=0, blank=False)
    day37 = models.IntegerField(verbose_name="37일 수량", null=False, default=0, blank=False)
    day38 = models.IntegerField(verbose_name="38일 수량", null=False, default=0, blank=False)
    day39 = models.IntegerField(verbose_name="39일 수량", null=False, default=0, blank=False)
    day40 = models.IntegerField(verbose_name="40일 수량", null=False, default=0, blank=False)
    day41 = models.IntegerField(verbose_name="41일 수량", null=False, default=0, blank=False)
    day42 = models.IntegerField(verbose_name="42일 수량", null=False, default=0, blank=False)
    day43 = models.IntegerField(verbose_name="43일 수량", null=False, default=0, blank=False)
    day44 = models.IntegerField(verbose_name="44일 수량", null=False, default=0, blank=False)
    day45 = models.IntegerField(verbose_name="45일 수량", null=False, default=0, blank=False)
    day46 = models.IntegerField(verbose_name="46일 수량", null=False, default=0, blank=False)
    day47 = models.IntegerField(verbose_name="47일 수량", null=False, default=0, blank=False)
    day48 = models.IntegerField(verbose_name="48일 수량", null=False, default=0, blank=False)
    day49 = models.IntegerField(verbose_name="49일 수량", null=False, default=0, blank=False)
    day50 = models.IntegerField(verbose_name="50일 수량", null=False, default=0, blank=False)
    day51 = models.IntegerField(verbose_name="51일 수량", null=False, default=0, blank=False)
    day52 = models.IntegerField(verbose_name="52일 수량", null=False, default=0, blank=False)
    day53 = models.IntegerField(verbose_name="53일 수량", null=False, default=0, blank=False)
    day54 = models.IntegerField(verbose_name="54일 수량", null=False, default=0, blank=False)
    day55 = models.IntegerField(verbose_name="55일 수량", null=False, default=0, blank=False)
    day56 = models.IntegerField(verbose_name="56일 수량", null=False, default=0, blank=False)
    day57 = models.IntegerField(verbose_name="57일 수량", null=False, default=0, blank=False)
    day58 = models.IntegerField(verbose_name="58일 수량", null=False, default=0, blank=False)
    day59 = models.IntegerField(verbose_name="59일 수량", null=False, default=0, blank=False)
    day60 = models.IntegerField(verbose_name="60일 수량", null=False, default=0, blank=False)
    day61 = models.IntegerField(verbose_name="61일 수량", null=False, default=0, blank=False)
    day62 = models.IntegerField(verbose_name="62일 수량", null=False, default=0, blank=False)

    class Meta:
        db_table = 'dailyAmount'
        verbose_name = '일자별 주문가능수량'
        verbose_name_plural = '일자별 주문가능 수량'


class Order(models.Model):
    MONTHS ={
        ('Jan', '1월'), ('Feb', '2월'), ('Mar', '3월'), ('Apr', '4월'), ('May', '5월'), ('Jun', '6월'),
        ('Jul', '7월'), ('Aug', '8월'), ('Sep', '9월'), ('Oct', '10월'), ('Nov', '11월'), ('Dec', '12월'),
    }
    orderNum = models.CharField(max_length=50,verbose_name='주문 번호',primary_key=True,blank=False)
    orderer = models.CharField(max_length=20,verbose_name="주문자",null=True,blank=False)
    pickupDate = models.CharField(max_length=30,verbose_name='희망 수령일',null=True,blank=False)
    pickupTime = models.CharField(max_length=20,verbose_name='희망 픽업 시간',null=True,blank=False)
    businessID = models.CharField(max_length=50, verbose_name='사업자 등록번호',null=True,blank=False)
    storeName = models.CharField(max_length=30, verbose_name='가게 이름', null=True, blank=True)
    location = models.CharField(max_length=200, verbose_name='가게 위치', null=True, blank=True)  # 나중에 blank False로 수정하기
    storeContact = models.CharField(max_length=30, verbose_name='가게 연락처', null=True, blank=True) #,unique=True
    cakeName = models.CharField(max_length=200, verbose_name='케이크 이름',null=True,blank=False)
    cakeImg = models.ImageField(verbose_name='케이크 이미지', null=True, blank=True)
    cakeText = models.TextField(verbose_name='케이크 문구',null=True,blank=True)
    message = models.TextField(verbose_name='요청 사항',null=True,blank=True)
    price = models.IntegerField(verbose_name='가격',null=True,blank=False)
    status = models.IntegerField(verbose_name='주문 진행 상황',default=0,blank=False)
    fromManager = models.TextField(verbose_name='사장님 메세지', null=True, blank=True)
    def __str__(self):
         return self.orderNum

    class Meta:
        db_table = 'Order'
        verbose_name = '주문서'
        verbose_name_plural = '주문서'


class Review(models.Model):
    orderNum = models.CharField(max_length=20, verbose_name='주문 번호',primary_key=True)
    cakeName = models.CharField(max_length=200, verbose_name='케이크 이름',null=False,blank=False,default="")
    orderer = models.CharField(max_length=20,verbose_name="주문자",null=True,blank=False)
    secureID = models.CharField(max_length=20,verbose_name="주문자 ID 변환",null=True,blank=False)
    storeInfo = models.CharField(max_length=50, verbose_name='사업자 등록번호',null=True,blank=False)
    taste = models.IntegerField(verbose_name='맛 평점',null=True,blank=False)
    service = models.IntegerField(verbose_name='서비스 평점',null=True,blank=False)
    design = models.IntegerField(verbose_name='디자인 평점',null=True,blank=False)
    textReview = models.TextField(verbose_name='한 줄 후기',null=True,blank=True)

    class Meta:
        db_table = 'Review'
        verbose_name = '리뷰'
        verbose_name_plural = '리뷰'

class Option(models.Model):
    businessID = models.CharField(max_length=50, verbose_name='사업자 등록번호', null=True, blank=False)
    optionName = models.CharField(max_length=30, verbose_name='옵션명', null=True, blank=False)
    isNecessary = models.BooleanField(default=False, verbose_name='필수 여부', null=True, blank=False)
    withColorOrImage = models.CharField(max_length=100,default="선택 없음", verbose_name='색상판/이미지 유무', null=False, blank=False, choices=[('색상판', '색상판'), ('이미지', '이미지'),('선택 없음', '선택 없음')])
    isUsed = models.BooleanField(default=False)

    class Meta:
        db_table = 'Options'
        verbose_name = '등록된 옵션'
        verbose_name_plural = '등록된 옵션'

    def __str__(self):
        return self.optionName

    def get_details(self):
        return ', '.join(self.details.all().values_list('detailName', flat=True))


class DetailedOption(models.Model):
    businessID = models.CharField(max_length=50, verbose_name='사업자 등록번호', null=True, blank=False,default="")
    option = models.ForeignKey(Option,related_name='details', on_delete=models.CASCADE, null=True)
    detailName = models.CharField(max_length=50,verbose_name='옵션 세부항목명',null=True,blank=False,default="")
    pricing = models.IntegerField(verbose_name='추가 금액',null=True,blank=False,default="")


    class Meta:
        db_table = 'DetailedOptions'
        verbose_name = '세부 옵션'
        verbose_name_plural = '세부 옵션'

    def __str__(self):
        return self.detailName

class Cake(models.Model): #원래 Store상속받음
    cakeid = models.CharField(max_length=200,verbose_name="케이크 PK",primary_key=True,blank=False,default="")
    crn = models.CharField(max_length=50, verbose_name='사업자 등록번호',null=True,blank=False)
    cakeName = models.CharField(max_length=200, verbose_name='케이크 이름',null=False,blank=False,default="")
    cakeImg = models.ImageField(verbose_name='케이크 이미지',null=True,blank=True, default="logo_baker.png")
    cakePrice = models.IntegerField(verbose_name='1호 기준 가격',null=True,blank=False)

    class Meta:
        db_table = 'Cake'
        verbose_name = '케이크'
        verbose_name_plural = '케이크'

class CakeOption(models.Model):
    businessID = models.CharField(max_length=50, verbose_name='사업자 등록번호', null=True, blank=False,default="")
    optionID = models.IntegerField(verbose_name='옵션 ID',null=True,blank=False,default="")
    cakeID = models.CharField(max_length=100,verbose_name='케이크 ID',null=True,blank=False,default="")
    isSelected = models.BooleanField(default=False,verbose_name='선택 여부',null=True,blank=False)

    class Meta:
        db_table = 'Cake Option'
        verbose_name = '케이크 옵션'
        verbose_name_plural = '케이크 옵션'


class OrderOption(models.Model):
    businessID = models.CharField(max_length=50, verbose_name='사업자 등록번호', null=True, blank=False,default="")
    orderer = models.CharField(max_length=20,verbose_name="주문자",null=True,blank=False)
    optionID = models.IntegerField(verbose_name='옵션 ID',null=True,blank=False,default="")
    orderID = models.CharField(max_length=50,verbose_name='주문 번호',null=True,blank=False,default="")
    color = models.CharField(max_length=30, verbose_name='컬러 코드', null=True, blank=True, unique=False)
    image = models.ImageField(verbose_name='이미지 이름', null=True, blank=True)

    class Meta:
        db_table = 'Order Option'
        verbose_name = '주문서 옵션'
        verbose_name_plural = '주문서 옵션'
