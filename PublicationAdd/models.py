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


class my_datetime(datetime.datetime):
    def __ge__(self, other):
        IsMoreOrEqual = self.year > other.year or \
            self.year == other.year and self.month > other.month or\
                self.year == other.year and self.month == other.month and self.day > other.day or\
                    self.year == other.year and self.month == other.month and self.day == other.day and self.hour > other.hour or\
                        self.year == other.year and self.month == other.month and self.day == other.day and self.hour == other.hour and self.minute >= other.minute
        return IsMoreOrEqual


class Publication(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True, default=None)
    Text = models.TextField()
    Image = models.FileField(upload_to='publication_images')
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE, default=None)
    tags = models.ManyToManyField(Tag, default=None)
    IsVisible = models.BooleanField(default=True)
    DateOfPublic = models.DateTimeField(default=datetime.datetime.now(tz=None))
    Likes = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def can_post(self):
        dt = self.DateOfPublic
        public_datetime = my_datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        return my_datetime.now(tz=None) >= public_datetime  # получаем текущую дату и
        # сравниваем с датой из БД

    def __str__(self):
        return f"Статья: {self.id}"
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
