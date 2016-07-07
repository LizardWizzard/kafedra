from django.db import models

STEPS = (
    (1, 'Бакалавриат'),
    (2, 'Магистратура'),
    (3, 'Аспирантура')
)

class Step(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Этап обучения')
    description = models.TextField()

class Kurs(models.Model):
    number = models.IntegerField(unique=True, verbose_name='Курс')
    # description = models.TextField()
    step = models.ForeignKey(Step, null=False, blank=False)
    # document_folder

class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название предмета')

    description = models.TextField(verbose_name= 'Описание предмета')

class Document(models.Model):
    subject = models.CharField(max_length=50, verbose_name='Предмет')


    name = models.CharField(max_length=50, unique=True, verbose_name='Документ')
    description = models.TextField()
    file = models.FileField(upload_to='docs')




