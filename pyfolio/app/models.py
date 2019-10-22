from django.db import models


class Status(models.Model):
    class Meta:
        verbose_name_plural = "Status"

    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(blank=False)
    created = models.DateField(null=False, blank=False)
    changed = models.DateField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
