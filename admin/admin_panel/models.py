from django.db import models


_null_blank = {'null': True, 'blank': True}


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField()

    enter_at_chat_time = models.DateTimeField(**_null_blank)
    spamed = models.BooleanField(**_null_blank)

    class Meta:
        db_table = 'bot_user'


class Text(models.Model):
    id = models.CharField(primary_key=True)
    text = models.TextField()

    class Meta:
        db_table = 'bot_text'