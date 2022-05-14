from django.db import models
import uuid as uuid_lib
from django.contrib.auth.models import User

# from django.contrib.auth import get_user_model

import threading

_thread_locals = threading.local()


# Create your models here.
def get_current_user():
    return getattr(_thread_locals, "user", None)


class BaseModel(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid_lib.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        User, null=True, editable=False, related_name="%(class)s_created", on_delete=models.CASCADE,
    )
    modified_by = models.ForeignKey(
        User, null=True, editable=False, related_name="%(class)s_modified", on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        user = get_current_user()

        if user and user.is_authenticated:
            self.modified_by = user
            if "update_fields" in kwargs and "modified_by" not in kwargs["update_fields"]:
                kwargs["update_fields"].append("modified_by")

            if not self.pk:
                self.created_by = user
                if "update_fields" in kwargs and "created_by" not in kwargs["update_fields"]:
                    kwargs["update_fields"].append("created_by")
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Collection(BaseModel):
    name = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=150, null=False)
    creator_network = models.ForeignKey(
        User, null=True, editable=False, related_name="collections", on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"id: {self.uuid} | file_type: {self.name}"


class NFT(BaseModel):
    asset_id = models.UUIDField(unique=True, default=uuid_lib.uuid4, editable=False)
    name = models.CharField(max_length=150, null=False)
    picture = models.FileField(upload_to="picutures", max_length=275)  # file Path
    external_link = models.URLField(max_length=200, null=False)
    description = models.CharField(max_length=150, null=False)
    collection = models.ForeignKey(Collection, null=True, related_name="collection_nfts", on_delete=models.CASCADE)
    supply = models.IntegerField(default=0)
    royalties = models.FloatField(null=True, default=None)
    buyer = models.ForeignKey(
        User, null=True, editable=False, related_name="nfts", on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"id: {self.asset_id} | file_type: {self.name}"