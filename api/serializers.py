from rest_framework import serializers
from fastai.vision.all import *
from PIL import Image
import io

from .models import ImageModel

# class ImageModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ImageModel
#         fields = ['id', 'name', 'image']

#     def predict_image(self, image_data):
        
#         try:
#             # Load the model
#             learner = load_learner('materials/food_class.pkl')

#             # Convert image data to PIL.Image
#             image = Image.open(io.BytesIO(image_data.read()))

#             # Ensure the image has three channels (RGB)
#             if image.mode != 'RGB':
#                 image = image.convert('RGB')

#             # Make a prediction
#             prediction, id, probablity = learner.predict(image)

#             result = [prediction,id,probablity]
#             # print(result)

#             return result
#         except Exception as e:
#             # Handle exceptions during prediction
#             print("Error during image prediction:", e)
#             return None

#     def create(self, validated_data):
#         # Extract image data
#         image_data = validated_data.pop('image')

#         # Predict the image class
#         prediction = self.predict_image(image_data)

#         if prediction is not None:
#             instance = ImageModel.objects.create(
#                 name=prediction,
#                 image=image_data
#             )
#             return instance
#         else:
#             # Handle the case where prediction fails
#             raise serializers.ValidationError("Image processing failed")





class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ['id', 'name', 'image','probability']

    def predict_image(self, image_data):
        try:
            # Load the model
            learner = load_learner('materials/food_class.pkl')

            # Convert image data to PIL.Image
            image = Image.open(io.BytesIO(image_data.read()))

            # Ensure the image has three channels (RGB)
            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Make a prediction
            prediction, pred_id, probability = learner.predict(image)

            result = {'prediction': prediction, 'pred_id': pred_id, 'probability': probability}

            return result
        except Exception as e:
            # Handle exceptions during prediction
            print("Error during image prediction:", e)
            return None

    def create(self, validated_data):
        # Extract image data
        image_data = validated_data.pop('image')

        # Predict the image class
        prediction_result = self.predict_image(image_data)

        x = prediction_result['pred_id']
        z = prediction_result['probability']
        y = f"{z[x].item() * 100:.2f}%"

        if prediction_result is not None:
            # Create a new model instance
            instance = ImageModel.objects.create(
                name=prediction_result['prediction'],
                probability=y,
                image=image_data
            )
            return instance
        else:
            # Handle the case where prediction fails
            raise serializers.ValidationError("Image processing failed")
