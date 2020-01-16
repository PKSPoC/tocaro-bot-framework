from django.db import models


class User(models.Model):
    objects = None
    STATUS_DRAFT = "draft"
    name = models.CharField(max_length=32)
    email = models.EmailField()

    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)

    __str__ = __repr__


class Quote(models.Model):
    objects = None
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
        (STATUS_DRAFT, "下書き"),
        (STATUS_PUBLIC, "公開中"),
    )
    quote = models.TextField()
    author = models.ForeignKey(User, related_name="quotes", on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "{}: {} by{}".format(self.pk, self.quote, self.author.name)

    __str__ = __repr__


class Command(models.Model):
    command = models.TextField()

    def __repr__(self):
        return "{}: {}".format(self.pk, self.command)

    __str__ = __repr__

