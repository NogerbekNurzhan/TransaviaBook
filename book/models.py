from django.db import models


class Book(models.Model):
    text = models.TextField(
        help_text='Text',
        blank=True,
        null=True,
    )

    def __str__(self):
            return "%s: %s" % (self.id, self.text[:100])

    class Meta:
        db_table = 'book'
        verbose_name = 'book'
        verbose_name_plural = 'books'
        ordering = ['id']
