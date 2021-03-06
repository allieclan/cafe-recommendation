from django.db import models

# Create your models here.


class Gate(models.Model):
    문이름 = models.CharField(max_length=5)

    def __str__(self):
        return self.문이름


class Category(models.Model):
    카테고리 = models.CharField(max_length=10)

    def __str__(self):
        return self.카테고리


class Cafe(models.Model):
    문 = models.ForeignKey(Gate, on_delete=models.PROTECT)
    카테고리 = models.ForeignKey(Category, on_delete=models.PROTECT)
    카페명 = models.CharField(max_length=20)
    전화번호 = models.CharField(max_length=20)
    주소 = models.CharField(max_length=30)
    영업시간 = models.CharField(max_length=20)
    x좌표 = models.FloatField(max_length=50, blank=False)
    y좌표 = models.FloatField(max_length=50, blank=False)

    def __str__(self):
        return "[" + self.문.문이름 + "] " + self.카페명

    class Meta:
        ordering = ['문', '카페명']


class Menu(models.Model):
    카페 = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    이름 = models.CharField(max_length=20)
    가격 = models.CharField(max_length=10)

    def __str__(self):
        return "[" + self.카페.카페명 + "] " + self.이름

    class Meta:
        ordering = ['카페', '이름']
