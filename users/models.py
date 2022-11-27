from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, user_id, password, nick_name, email, student_num, date_joined):
        if not email:
            raise ValueError('이메일은 필수입니다.')

        user = self.model(
            user_id = user_id,
            password = password,
            nick_name = nick_name,
            email = email,
            student_num = student_num,
            date_joined = date_joined,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, nick_name=None, email=None, student_num=None, date_joined=None):
        user = self.create_user(user_id, password, nick_name, email, student_num, date_joined)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_id = models.CharField(max_length=18 , verbose_name='아이디', unique=True)
    password = models.CharField(max_length=30, verbose_name='비밀번호')
    nick_name = models.CharField(max_length=10, verbose_name='닉네임', null=True)
    email = models.EmailField(verbose_name='이메일', max_length=128, unique=True, null=True)
    student_num = models.IntegerField(verbose_name='학번', null=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일자', null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

