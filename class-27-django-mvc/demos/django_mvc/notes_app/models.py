from django.db import models


class Note(models.Model):
    """
    """
    title = models.CharField(max_length=48)
    detail = models.CharField(max_length=4096)

    STATES = [
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
    ]
    status = models.CharField(max_length=48, default='incomplete', choices=STATES)

    # def __repr__(self):
    #     return ''

    def __str__(self):
        return f'{self.title} ({self.status})'
