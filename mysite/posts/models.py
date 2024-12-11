from django.db import models

class Posts(models.Model):
    title = models.CharField(verbose_name="제목", max_length=100)
    content = models.TextField(verbose_name="내용")
    password = models.CharField(verbose_name="비밀번호", max_length=100)
    username = models.CharField(verbose_name="글쓴이", max_length=10)
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)
    
    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title