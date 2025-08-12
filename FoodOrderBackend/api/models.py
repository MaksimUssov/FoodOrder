from django.db import models


# Create your models here.
class Worker(models.Model):
    name = models.CharField('ФИ', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Section(models.Model):
    title = models.CharField('Название', blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

class Dish(models.Model):
    title = models.CharField('Название', blank=False)
    composition = models.TextField('Состав')
    cost = models.IntegerField('Цена', blank=False)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.title} - {self.section}'

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

class Order(models.Model):
    date = models.DateField()
    worker_id = models.ForeignKey(Worker, on_delete=models.PROTECT)
    def __str__(self):
        return f'{str(self.date)} - {self.worker_id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class DishesOfOrder(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    dish_id = models.ForeignKey(Dish, on_delete=models.PROTECT)
    dish_title = models.CharField('Название блюда')
    worker_id = models.ForeignKey(Worker, on_delete=models.PROTECT)
    def __str__(self):
        return f'{self.order_id.id} | {self.dish_id} | {self.order_id}'

    class Meta:
        verbose_name = 'Блюдо заказа'
        verbose_name_plural = 'Блюда заказов'
