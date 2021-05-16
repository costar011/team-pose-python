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

    CHOICE_HTML = "html"
    CHOICE_CSS = "css"
    CHOICE_JS = "javascript"
    CHOICE_ES6 = "eS6"
    CHOICE_NODE = "node.js"
    CHOICE_JAVA = "java"
    CHOICE_PYTHON = "python"
    CHOICE_SQL = "sql"
    CHOICE_REACT = "react"
    CHOICE_RN = "react-native"
    CHOICE_FIREBASE = "firebase"
    CHOICE_GRAPHQL = "graphql"

    CHOICE_TYPE = (
        (CHOICE_HTML, "HTML"),
        (CHOICE_CSS, "CSS"),
        (CHOICE_JS, "JAVASCRIPT"),
        (CHOICE_ES6, "ES6"),
        (CHOICE_NODE, "NODE"),
        (CHOICE_JAVA, "JAVA"),
        (CHOICE_PYTHON, "PYTHON"),
        (CHOICE_SQL, "SQL"),
        (CHOICE_REACT, "REACT"),
        (CHOICE_RN, "REACT-NATIVE"),
        (CHOICE_FIREBASE, "FIREBASE"),
        (CHOICE_GRAPHQL, "GRAPHQL"),
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name="doc_board", on_delete=models.CASCADE)
    board_type = models.CharField(choices=CHOICE_TYPE, max_length=40)

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
