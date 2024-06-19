from django.db import models

from apps.core.models import BaseModel


class PlantedTree(BaseModel):
    age = models.IntegerField(
        blank=True, null=True
    )
    # tree = models.ForeignKey(Tree, on_delete=models.PROTECT)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    # latitude = models.DecimalField(max_digits=9, decimal_places=6)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # date_planted = models.DateTimeField(auto_now_add=True)


class Tree(BaseModel):
    name = models.CharField(
        max_length=2048
    )
    scientific_name = models.CharField(
        max_length=2048,
        blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Árvore'
        verbose_name_plural = 'Árvores'
        ordering = ['-created_at']
        db_table = 'tree'
