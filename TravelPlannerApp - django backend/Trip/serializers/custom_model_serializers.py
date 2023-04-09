from rest_framework import serializers


class CustomModelSerializer(serializers.ModelSerializer):

    class Meta:
        pass

    def __init__(self, *args, **kwargs):
        super(CustomModelSerializer, self).__init__(*args, **kwargs)

        if "depth" in self.context:
            self.Meta.depth = self.context["depth"]

        if "fields" in self.context:
            self.Meta.fields = self.context["fields"]

        if "exclude" in self.context:
            self.Meta.exclude = self.context["exclude"]