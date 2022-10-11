from django.db.models import Model, CharField, DateField


class StudentGroup(Model):
    """ Учебная группа """

    name = CharField('название', max_length=50)

    class Meta:
        verbose_name = 'учебная группа'
        verbose_name_plural = 'учебные группы'


class Semester(Model):
    """ Семестр """

    start = DateField('дата начала')
    finish = DateField('дата окончания')

    class Meta:
        verbose_name = 'семестр'
        verbose_name_plural = 'семестры'

    # def __str__(self):
    #     return f"{self.}"
