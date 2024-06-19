import uuid

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models

from apps.trees.models import PlantedTree


class Profile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    groups = models.ManyToManyField(
        Group,
        related_name='profile_groups',
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=_('groups'),
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='profile_permissions',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )

    def plant_tree(self, plant, latitude, longitude):
        PlantedTree.objects.create(user=self, plant=plant, latitude=latitude, longitude=longitude)

    def plant_trees(self, plants_with_coords):
        for plant, (latitude, longitude) in plants_with_coords:
            self.plant_tree(plant, latitude, longitude)
