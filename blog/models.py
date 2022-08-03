from django.db import models
from django.contrib.auth.models import User
import os
class Post(models.Model): # models 모듈의 Model 클래스를 확장해서 만듦
    title = models.CharField(max_length=30) # CharField 클래스는 문자(char)를 담는 필드
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField() # TextField는 문자열의 길이 제한이 없음

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #이미지를 지정할 폴더의 경로 규칙 지정, 뒤 옵션은 해당 필드는 필수 항목은 아니라는 뜻
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #DateTimeField는 월, 일, 시, 분, 초까지 기록할 수 있게 해주는 필드, auto_now_add=True는 처음 레코드가 생성될 때 현재시각이 자동으로 저장되게 함
    updated_at = models.DateTimeField(auto_now=True) #auto_now=True는 다시 저장할 때 마다 그 시각이 저장되도록 함
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}' #pk는 각 레코드에 대한 고유값 ex)처음 포스트는 자동으로 pk값 1 부여, 두번째 포스트는 2

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]