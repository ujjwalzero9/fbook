# Social Media App

This is a backend implementation for a social media app built using Django, providing API endpoints for user registration, posts, comments, likes, and follows.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)


## Features
- User registration and authentication.
- Creating, updating, and deleting posts.
- Adding, updating, and deleting comments on posts.
- Liking and unliking posts and comments.
- Following and unfollowing other users.
- API endpoints for accessing and managing data.

## Requirements
- Python 3.6+
- Django 3.2+
- Django REST framework

## Installation
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Django development server using `python manage.py runserver`.

## API Endpoints
- `/api/users/`: API endpoint for listing and creating users.
- `/api/users/{user_id}/`: API endpoint for retrieving, updating, and deleting a specific user.
- `/api/posts/`: API endpoint for listing and creating posts.
- `/api/posts/{post_id}/`: API endpoint for retrieving, updating, and deleting a specific post.
- `/api/posts/{post_id}/comments/`: API endpoint for listing and creating comments on a post.
- `/api/posts/{post_id}/likes/`: API endpoint for listing and creating likes on a post.
- `/api/comments/{comment_id}/`: API endpoint for retrieving, updating, and deleting a specific comment.
- `/api/comments/{comment_id}/likes/`: API endpoint for listing and creating likes on a comment.
- `/api/follows/`: API endpoint for listing and creating follows between users.
- `/api/follows/{follow_id}/`: API endpoint for retrieving and deleting a specific follow.

- ## POSTMAN API Collection
- https://lively-crater-762071.postman.co/workspace/New-Team-Workspace~e2e64a87-fe96-480f-b9ca-88f791f78492/collection/28732463-dce7387f-34e2-42eb-907f-72cec918c832?action=share&creator=28732463

## Usage
- Use Postman or any API client to make requests to the above endpoints.
- Register users, create posts, add comments, and interact with the app's social features.


---

**Ujjwal Kumar**
Email: ujjwalzero9@gmail.com
