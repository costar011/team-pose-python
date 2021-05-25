from django.db import models


class ContactFileModel(models.Model):
    file = models.FileField(null=True, default=True)
    contact = models.ForeignKey(
        "ContactsModel", related_name="contacts", on_delete=models.CASCADE
    )


class ContactsModel(models.Model):

    name = models.CharField(max_length=80)
    loc = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    contents = models.TextField()

    created = models.DateField(auto_now_add=True)

    # str : to Stirng
    def __str__(self):
        return f"{self.name} - {self.created}"

    class Meta:
        verbose_name_plural = "CONTACTS"