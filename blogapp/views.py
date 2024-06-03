from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view,renderer_classes,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .serializers  import PostSerializer,PostCreateSerializer,CommentSerializer,CommentCreateSerializer
# from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from .models      import Post ,Comment
from rest_framework.response import Response
# Create your views here.
@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def Posts(request,*args,**keywords):
      if request.method =='GET':
            postsInstance =Post.objects.all()
            serializer    =PostSerializer(postsInstance,many=True).data
            return Response(serializer)
      else:
            if  not request.user:
                  return Response({'message':'you are not authenticated'},status=401) 
            serializer =PostCreateSerializer(data={'owner':request.user.id,'title':request.data['title'],'content':request.data['content']})
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data,status=201)
            else:
                  return Response(serializer.errors,status=400)
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def PostDetails(request,pk):
      postInstance =Post.objects.get(pk=pk)
      if request.method =='GET':
            serializer_data =PostSerializer(postInstance).data
            return Response(serializer_data,status=200)
      elif request.method =='PUT':
            if request.user.id == postInstance.owner.id:
                  serializer =PostSerializer(postInstance,data=request.data)
                  if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data,status=206)
                  return Response(serializer.errors,status=400)
            else:
                  return Response({'message':'you are not authenticated'},status=401)

      else:
            if request.user.id == postInstance.owner.id:
                  postInstance.delete();
                  return Response({'message':'Delete Record successfully'},status=204)
            return Response({'message':'you are not authenticated'},status=401)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication,SessionAuthentication])
def PostComments(request,pk):
      if request.method =='GET':
            instance =Comment.objects.filter(post_id=pk)
            serializer =CommentSerializer(instance=instance,many=True)
            return Response(serializer.data,status=200)
      
      else:
            data ={
                  'owner':request.user.id,
                  'content':request.data['content'],
                  'post_id':pk
            }
            serializer =CommentCreateSerializer(data=data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data,status=201)
            return Response(serializer.errors,status=400)
@api_view(['GET','PATCH','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
@authentication_classes([TokenAuthentication,SessionAuthentication])
def CommentDetails(request,post_id,pk):
      try:
            global instance
            instance = Comment.objects.get(pk=pk,post_id=post_id)
      except:
            return Response({'message':'comment not found for this post'},status=404)
      if request.method == 'GET':
                  serializer =CommentSerializer(instance=instance)
                  return Response(serializer.data,200)
      elif instance.owner.id ==request.user.id:
            if request.method =='PATCH':
                  serializer =CommentCreateSerializer(instance,request.data, partial=True)
                  if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data,status=206)
                  return Response(serializer.errors,status=400)
            elif request.method =='DELETE':
                  instance.delete()
                  return Response({'message':'Delete Record successfully'},status=204)
      return Response({'message':'you are not autherized'},status=403)
      