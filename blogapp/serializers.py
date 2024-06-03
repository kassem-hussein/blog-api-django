from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  Post,Comment
class CommentSerializer(serializers.ModelSerializer):
      owner = serializers.SerializerMethodField(read_only=True)
      class Meta:
            model=Comment
            fields=['id','owner','content']
      def get_owner(self,obj):
            return obj.owner.username
class CommentCreateSerializer(serializers.ModelSerializer):
      class Meta:
            model=Comment
            fields=['owner','content','post_id']    
class PostSerializer(serializers.ModelSerializer):
      owner = serializers.SerializerMethodField(read_only=True)
      comments = CommentSerializer(many=True, read_only=True)
      class Meta:
            model =Post
            fields=['id','title','content','post_date','owner','comments']
      def get_owner(self,obj):
            return obj.owner.username
class PostCreateSerializer(serializers.ModelSerializer):
      class Meta:
            model =Post
            fields=['title','content','owner']
     

   
      
