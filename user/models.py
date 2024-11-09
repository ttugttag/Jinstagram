from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    """
        유저 프로파일 사진
        유저 닉네임     -> 화면에 표기되는 이름
        유저 이름       -> 실제 사용자 이름
        유저 이메일주소 -> 회원가입할때 사용하는 아이디
        유저 비밀번호 -> 디폴트 쓰자
    """
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True, unique=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    profile_image = models.CharField(max_length=256, default='default_profile.jpg', blank=True, null=True)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['nickname']

    # def __str__(self):
    #     return self.user_id
    #
    # @property
    # def is_staff(self):
    #     return self.is_admin

    class Meta:             # table이름을 설정
        # db_table = 'users'
        db_table = 'User'
