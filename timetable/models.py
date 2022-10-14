from django.db.models import CharField, DateField, Model


class StudyGroup(Model):

    name = CharField("название", max_length=50)

    class Meta:
        verbose_name = "учебная группа"
        verbose_name_plural = "учебные группы"

    def __str__(self):
        return f"{self.name}"


class Semester(Model):

    start = DateField("дата начала")
    finish = DateField("дата окончания")

    class Meta:
        verbose_name = "семестр"
        verbose_name_plural = "семестры"

    # def __str__(self):
    #     return f"{self.}"
