from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class VideoPost(models.Model):
    LIST_CATEGORIES = [
        ("Science & Technology","Science & Technology"),
        ("Fashion","Fashion"),
        ("Food","Food"),
        ("Education","Education"),
        ("Blogs","Blogs")
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("Название видео", max_length=100)
    desc = models.TextField("Подробное описание к видео")
    video_file = models.FileField("Загружаемый видео-файл формата MP4", upload_to='videos/')
    thumbnail = models.ImageField("Титульная картинка формата JPG", upload_to='videos/thumbnail/', default='none')
    category = models.CharField("Категория видео", max_length=120,  choices=LIST_CATEGORIES, default="Blogs")
    pub_date = models.DateField("Дата публикации", auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)
    video_views = models.ManyToManyField(User, related_name='video_views', blank=True)

    def __str__(self):
        return f"{self.user} {self.title} {self.desc} {self.category}"

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    profile_pic = models.ImageField(upload_to='pic/', default='pic/default.jpg')
    subscribers = models.ManyToManyField(User, related_name='subscribers')

    def __str__(self):
        return f"{self.user} {self.about} {self.subscribers} {self.profile_pic}"

class Comment(models.Model):
    post = models.ForeignKey(VideoPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    date_create = models.DateField(("Date"), default=date.today)

    def __str__(self):
        return f"{self.user.id} {self.user.username} {self.post} {self.comment} {self.date_create}"
