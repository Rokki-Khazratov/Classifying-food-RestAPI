from rest_framework import serializers
from fastai.vision.all import *
from PIL import Image
import io

from .models import ImageModel


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ['id', 'name', 'image','probability']

    def predict_image(self, image_data):
        try:

            learner = load_learner('materials/food_class.pkl')


            image = Image.open(io.BytesIO(image_data.read()))


            if image.mode != 'RGB':
                image = image.convert('RGB')


            prediction, pred_id, probability = learner.predict(image)

            result = {'prediction': prediction, 'pred_id': pred_id, 'probability': probability}

            return result
        except Exception as e:

            print("Error during image prediction:", e)
            return None

    def create(self, validated_data):
        image_data = validated_data.pop('image')

        prediction_result = self.predict_image(image_data)

        x = prediction_result['pred_id']
        y = prediction_result['probability']
        z = f"{y[x].item() * 100:.2f}%"

        if prediction_result is not None:

            instance = ImageModel.objects.create(
                name=prediction_result['prediction'],
                probability=z,
                image=image_data
            )
            return instance
        else:

            raise serializers.ValidationError("Image processing failed")
