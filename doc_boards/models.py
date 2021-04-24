from django.db import models
from django.contrib.auth.models import User


class FileModel(models.Model):
    caption = models.CharField(max_length=100)
    file = models.FileField()
    board = models.ForeignKey(
        "DocBoardsModel",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = "Files"


class DocBoardsModel(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    likeCount = models.IntegerField(default=0)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def displayUser(self):
        return self.author.username

    displayUser.short_description = "author"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "DOC_BOARDS"