from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)

    @property
    def parents(self):
        parents = []
        category = self
        while category.parent:
            parents.append(category.parent)
            category = category.parent

        return parents

    @property
    def siblings(self):
        siblings = self.__class__.objects.none()
        if self.parent_id:
            siblings = self.__class__.objects.filter(parent_id=self.parent_id).exclude(id=self.id)
        return siblings
