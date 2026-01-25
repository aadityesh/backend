from models.posts import Posts
from models.users import User
import json


def create_post(data):
    try:
        user = User.objects.get(username=data.username)
        new_post = Posts()
        new_post.username = user
        new_post.post_content = data.post_content
        new_post.save()
        return {
            "msg": "Post created successfully"
        }
    except Exception as e:
        print(f"Error in create_post: {e}")
        return {
            "msg": "Post creation failed"
        }


def fetch_all_posts():
    try:
        print("- Printing all the posts:")
        posts = Posts.objects()

        response = [{
            "id": str(p.id),
            "username": str(p.username),
            "post_content": str(p.post_content),
        } for p in posts]

        return response

    except Exception as e:
        print(f"Error in fetch_all_posts: {e}")
        return {
            "msg": "Fetching all posts failed"
        }


# def fetch_post_by_user(username):
#     try:
#         print(f"- Printing posts for {username}:")
#         # posts_ls = []
#         # for p in Posts.objects.get(username=username):
#         #     posts_ls.append(p)
#         return Posts.objects.get(username=username)

#     except Exception as e:
#         print(f"Error in fetch_all_posts: {e}")
#         return {
#             "msg": "Fetching post by user failed"
#         }

def fetch_post_by_user(username: str):
    try:
        print(f"- Printing posts for {username}")
        user = User.objects.get(username=username)
        posts = Posts.objects(username=user)

        response = [{
            "id": str(p.id),
            "username": str(p.username),
            "post_content": str(p.post_content),
        } for p in posts]

        return response

    except Exception as e:
        print(f"Error in fetch_post_by_user: {e}")
        return []


def delete_post(data):
    try:
        Posts.objects(id=data.id).delete()
        return {
            "msg": "Post deleted successfully"
        }
    except Exception as e:
        print(f"Error in delete_post: {e}")
        return {
            "msg": "delete_post by id failed"
        }


def update_post(data):
    try:
        post = Posts.objects.get(id=data.id)
        post.post_content = data.post_content
        post.save()
        return {
            "msg": "Post updated successfully"
        }
    except Exception as e:
        print(f"Error in delete_post: {e}")
        return {
            "msg": "update_post by id failed"
        }
