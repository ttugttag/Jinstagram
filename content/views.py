from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed, Reply, Like, Bookmark, Follow
from user.models import User
from rest_framework.response import Response
import os
from Jinstagram.settings import MEDIA_ROOT
from uuid import uuid4

# Create your views here.
class Main(APIView):
    def get(self, request):
        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")

        feed_object_list = Feed.objects.all().order_by('-id')  # select  * from content_feed;
        feed_list = []

        for feed in feed_object_list:
            user = User.objects.filter(email=feed.email).first()
            reply_object_list = Reply.objects.filter(feed_id=feed.id)
            reply_list = []
            for reply in reply_object_list:
                user = User.objects.filter(email=reply.email).first()
                reply_list.append(dict(reply_content=reply.reply_content,
                                       nickname=user.nickname))
            like_count=Like.objects.filter(feed_id=feed.id, is_like=True).count()
            marked_count=Bookmark.objects.filter(feed_id=feed.id, is_marked=True).count()
            is_liked=Like.objects.filter(feed_id=feed.id, email=email, is_like=True).exists()
            is_marked=Bookmark.objects.filter(feed_id=feed.id, email=email, is_marked=True).exists()
            feed_list.append(dict(id=feed.id,
                                  image=feed.image,
                                  content=feed.content,
                                  like_count=like_count,
                                  marked_count=marked_count,
                                  profile_image=user.profile_image,
                                  nickname=user.nickname,
                                  reply_list=reply_list,
                                  is_liked=is_liked,
                                  is_marked=is_marked
                                  ))

        user = User.objects.filter(email=email).first()
        all_user_object_list = User.objects.exclude(email=email).order_by('id')
        all_user=[]
        for all_user_list in all_user_object_list:
            follow_count = Follow.objects.filter(follow_id=all_user_list.id, is_follow=True).count()
            is_follow = Follow.objects.filter(follow_id=all_user_list.id, email=email, is_follow=True).exists()
            all_user.append(dict(id=all_user_list.id,
                                 name=all_user_list.name,
                                 nickname=all_user_list.nickname,
                                 profile_image = all_user_list.profile_image,
                                 is_follow=is_follow,
                                 follow_count= follow_count,
                                 ))
        return render(request, "Jinstagram/main.html", context=dict(feeds=feed_list, user=user, all_user=all_user))

class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                # print(chunk)
                destination.write(chunk)

        content = request.data.get('content')
        image = uuid_name
        email = request.session.get('email', None)

        # print("file :",file)
        # print("uuid_name :", uuid_name)
        # print("save_path :", save_path)
        # print("content :", content)
        # print("image :", image)
        # print("profile_image :",profile_image)
        # print("user_id :",user_id)

        Feed.objects.create(content=content, image=image, email=email)

        return Response(status=200)

class Profile(APIView):
    def get(self, request):
        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()
        # print(user.id)

        if user is None:
            return render(request, "user/login.html")

        feed_list = Feed.objects.filter(email=email)
        like_list = list(Like.objects.filter(email=email, is_like=True).values_list('feed_id', flat=True))
        like_feed_list = Feed.objects.filter(id__in=like_list)
        bookmark_list = list(Bookmark.objects.filter(email=email, is_marked=True).values_list('feed_id', flat=True))
        bookmark_feed_list = Feed.objects.filter(id__in=bookmark_list)

        feed_count = Feed.objects.filter(email=email).count()
        following_count = Follow.objects.filter(email=email, is_follow=True).count()
        follow_count = Follow.objects.filter(follow_id=user.id, is_follow=True).count()

        return render(request, 'content/profile.html', context=dict(feed_list=feed_list,
                                                                    like_feed_list=like_feed_list,
                                                                    bookmark_feed_list=bookmark_feed_list,
                                                                    user=user,
                                                                    feed_count=feed_count,
                                                                    follow_count=follow_count,
                                                                    following_count=following_count,
                                                                    ))

class UploadReply(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        reply_content = request.data.get('reply_content', None)
        email = request.session.get('email', None)

        Reply.objects.create(feed_id=feed_id, reply_content=reply_content, email=email)

        return Response(status=200,)

class ToggleLike(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        favorite_text = request.data.get('favorite_text', True)

        if favorite_text == 'favorite_border':
            is_like = True
        else:
            is_like = False
        email = request.session.get('email', None)

        like = Like.objects.filter(feed_id=feed_id, email=email).first()

        if like:
            like.is_like = is_like
            like.save()
        else:
            Like.objects.create(feed_id=feed_id, is_like=is_like, email=email)

        return Response(status=200)


class ToggleBookmark(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        bookmark_text = request.data.get('bookmark_text', True)
        print(bookmark_text)
        if bookmark_text == 'bookmark_border':
            is_marked = True
        else:
            is_marked = False
        email = request.session.get('email', None)

        bookmark = Bookmark.objects.filter(feed_id=feed_id, email=email).first()

        if bookmark:
            bookmark.is_marked = is_marked
            bookmark.save()
        else:
            Bookmark.objects.create(feed_id=feed_id, is_marked=is_marked, email=email)

        return Response(status=200)

class ToggleFollow(APIView):
    def post(self, request):
        follow_id = request.data.get('follow_id', None)
        follow_text = request.data.get('follow_text', True)
        # print(follow_text)
        if follow_text == 'person':
            is_follow = True
        else:
            is_follow = False

        email = request.session.get('email', None)
        follow = Follow.objects.filter(follow_id=follow_id, email=email).first()

        # print(follow.is_follow)

        if follow:
            follow.is_follow = is_follow
            follow.save()
        else:
            Follow.objects.create(follow_id=follow_id, is_follow=is_follow, email=email)

        return Response(status=200)