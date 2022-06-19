from rest_framework import serializers


class NameSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    first = serializers.CharField(max_length=200)
    last = serializers.CharField(max_length=200)


class CoordinatesSerializer(serializers.Serializer):
    latitude = serializers.CharField(max_length=200)
    longitude = serializers.CharField(max_length=200)


class TimezoneSerializer(serializers.Serializer):
    offset = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)


class LocationSerializer(serializers.Serializer):
    street = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=200)
    state = serializers.CharField(max_length=200)
    postcode = serializers.IntegerField()
    coordinates = CoordinatesSerializer()
    timezone = TimezoneSerializer()


class DobAndRegisteredSerializer(serializers.Serializer):
    date = serializers.CharField(max_length=200)


class PictureSerializer(serializers.Serializer):
    large = serializers.CharField(max_length=200)
    medium = serializers.CharField(max_length=200)
    thumbnail = serializers.CharField(max_length=200)


class ProfileSerializer(serializers.Serializer):
    gender = serializers.CharField(max_length=200)
    name = NameSerializer()
    location = LocationSerializer()
    email = serializers.CharField(max_length=200)
    dob = DobAndRegisteredSerializer()
    registered = DobAndRegisteredSerializer()
    phone = serializers.CharField(max_length=200)
    cell = serializers.CharField(max_length=200)
    picture = PictureSerializer()

    def to_e164_format(self, str_phone):
        phone = "".join(x for x in str_phone if x.isdigit() or x == "+")
        return f"+55{phone}"

    def to_representation(self, instance):

        return {
            "gender": "m" if instance["gender"] == "male" else "f",
            "name": instance["name"],
            "location": instance["location"],
            "email": instance["email"],
            "birthday": instance["dob"].pop("date"),
            "registered": instance["registered"].pop("date"),
            "telephoneNumbers": [self.to_e164_format(instance["phone"])],
            "mobileNumbers": [self.to_e164_format(instance["cell"])],
            "picture": instance["picture"],
            "nationality": "BR",
        }
