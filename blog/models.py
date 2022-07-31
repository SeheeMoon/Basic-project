from django.db import models
class Post(models.Model): # models 모듈의 Model 클래스를 확장해서 만듦
    title = models.CharField(max_length=30) # CharField 클래스는 문자(char)를 담는 필드
    content = models.TextField() # TextField는 문자열의 길이 제한이 없음

    created_at = models.DateTimeField(auto_now_add=True) #DateTimeField는 월, 일, 시, 분, 초까지 기록할 수 있게 해주는 필드, auto_now_add=True는 처음 레코드가 생성될 때 현재시각이 자동으로 저장되게 함
    updated_at = models.DateTimeField(auto_now=True) #auto_now=True는 다시 저장할 때 마다 그 시각이 저장되도록 함
    # author: 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title}' #pk는 각 레코드에 대한 고유값 ex)처음 포스트는 자동으로 pk값 1 부여, 두번째 포스트는 2