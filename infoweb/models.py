from django.db import models


class Headline(models.Model):
    title = models.TextField()


class NewsHeadlines(models.Model):
    title = models.CharField(max_length=256)
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'news_headlines'

    def __str__(self):
        print(self.title)
        return self.title
