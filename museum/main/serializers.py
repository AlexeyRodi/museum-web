import base64
import uuid

from django.core.files.base import ContentFile
from rest_framework import serializers

from .models import Exhibition, MuseumRoom, Exhibit


class ExhibitionsSerializer(serializers.ModelSerializer):
    image_upload = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Exhibition
        fields = ['exhibition_id', 'name', 'start_date', 'end_date', 'responsible_person', 'image', 'image_upload']

    def validate_image_upload(self, value):
        if value:
            if isinstance(value, ContentFile):
                return value
            try:
                print("Received image_upload:", value)

                if value.startswith('data:image'):
                    format, imgstr = value.split(';base64,')
                else:
                    imgstr = value
                imgdata = base64.b64decode(imgstr)
                filename = f"exhibit_{uuid.uuid4()}.png"
                return ContentFile(imgdata, name=filename)
            except Exception as e:
                print(f"Error decoding image: {str(e)}")
                raise serializers.ValidationError(f"Ошибка обработки изображения: {str(e)}")
        return value

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

    def update(self, instance, validated_data):
        image_upload = validated_data.pop('image_upload', None)

        try:
            for attr, value in validated_data.items():
                setattr(instance, attr, value)

            if image_upload:
                instance.image = self.validate_image_upload(image_upload)
            instance.save()
            return instance
        except Exception as e:
            print(f"Error updating exhibit: {e}")
            raise serializers.ValidationError(f"Ошибка обновления экспоната: {str(e)}")


class MuseumRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuseumRoom
        fields = ['room_id', 'room_number', 'description', 'museum']


class ExhibitSerializer(serializers.ModelSerializer):
    image_upload = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Exhibit
        fields = ['exhibit_id', 'name', 'description', 'creation_year', 'creator', 'room', 'image', 'image_upload']

    def validate_image_upload(self, value):
        if value:
            if isinstance(value, ContentFile):
                return value
            try:
                print("Received image_upload:", value)

                if value.startswith('data:image'):
                    format, imgstr = value.split(';base64,')
                else:
                    imgstr = value
                imgdata = base64.b64decode(imgstr)
                filename = f"exhibit_{uuid.uuid4()}.png"
                return ContentFile(imgdata, name=filename)
            except Exception as e:
                print(f"Error decoding image: {str(e)}")
                raise serializers.ValidationError(f"Ошибка обработки изображения: {str(e)}")
        return value

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

    def update(self, instance, validated_data):
        image_upload = validated_data.pop('image_upload', None)

        try:
            for attr, value in validated_data.items():
                setattr(instance, attr, value)

            if image_upload:
                instance.image = self.validate_image_upload(image_upload)
            instance.save()
            return instance
        except Exception as e:
            print(f"Error updating exhibit: {e}")
            raise serializers.ValidationError(f"Ошибка обновления экспоната: {str(e)}")
