import json
import pdb

from django.conf import settings
from django.core.serializers import serialize
from django.db import models


def upload_update_image(instance, filename):
    return f"updates/{instance.user}/{filename}"


class UpdateQuerySet(models.QuerySet):
    # def serialize(self, ):
    #     qs = self
    #     return serialize('json', qs, fields=('user', 'content', 'image'))

    def serialize(self, ):
        list_values = list(self.values("user", "content","image"))
        #qs = self
        #final_array = []
        #for obj in qs:
        #final_array.append(obj.serialize())
        return json.dumps(list_values) #serialize('json', qs, fields=('user', 'content', 'image'))


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image,
                              blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        json_data = serialize("json", [self], fields=(
            'user', 'content', 'image'))
        struct = json.loads(json_data)
        #print(struct, "struct")
        data = json.dumps(struct[0]['fields'])
        print(data)
        return data
