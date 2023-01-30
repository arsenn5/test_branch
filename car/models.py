from django.db import models


class Brand(models.Model):
    brand = models.CharField(max_length=50,
                             verbose_name="Назаваниие бренда")

    def __str__(self):
        return self.brand


class NameModel(models.Model):
    name = models.CharField(verbose_name="Названиие машины",
                            max_length=50,

                            )
    image = models.ImageField(default="",
                              )
    price = models.IntegerField(verbose_name="Цена",
                                )
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              )

    def __str__(self):
        return self.name
