from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class UserModel(AbstractUser):

    class Meta:
        db_table = "Users" # 여기는 테이블 이름이에요! 꼭 기억 해 주세요!
        
    address = models.TextField()
    phone = models.TextField()
