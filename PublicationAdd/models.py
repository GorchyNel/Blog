from django.db import models
import datetime


class Tag(models.Model):
    Name = models.CharField(max_length=30, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f"Тег: {self.Name}"
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Rubric(models.Model):
    Name = models.CharField(max_length=30, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f"Рубрика: {self.Name}"
    
    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'


class my_date(datetime.date):
    def __ge__(self, other):
        IsMoreOrEqual = not (self.year < other.year or \
            self.year == other.year and self.month < other.month or\
                self.year == other.year and self.month == other.month and self.day < other.day)
        return IsMoreOrEqual


class Publication(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True, default=None)
    Text = models.TextField()
    Image = models.FileField(upload_to='publication_images')
    rubr = models.ForeignKey(Rubric, on_delete=models.CASCADE, default=None)
    tags = models.ManyToManyField(Tag)
    IsVisible = models.BooleanField(default=True)
    DelayedPosting = models.DateField(default=datetime.date.today())
    Likes = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def can_post(self):
        return my_date.today() >= my_date(self.DelayedPosting)  # получаем текущую дату и
        # сравниваем с датой из БД

    def __str__(self):
        return f"Статья: {self.Name}"
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
