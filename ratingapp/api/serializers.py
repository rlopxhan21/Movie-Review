from rest_framework import serializers

from ratingapp.models import Video, StreamingPlatform, Rating


class RatingSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Rating
        exclude = ['assocvideo']     


class VideoSerializer(serializers.ModelSerializer):
    # ratingfield = RatingSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='streamingplatform.name')
    class Meta:
        model = Video
        fields = '__all__'
        
class StreamignPlatformSerializer(serializers.ModelSerializer):
    watchlist = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = StreamingPlatform
        fields = '__all__'


        
        
        