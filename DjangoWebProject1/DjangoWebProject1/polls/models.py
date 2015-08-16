from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField
    user_name = models.CharField(max_length=15)
    SEX_CHOICES = (
        ('M', 'Man'),
        ('W', 'Women'),
    )
    user_sex = models.CharField(max_length=2, choices=SEX_CHOICES)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
       return self.question_text
    class Meta:
       db_table = 'user_question'



class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
