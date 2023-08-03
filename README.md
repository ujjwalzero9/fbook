# Social Media App

This is a backend implementation for a social media app built using Django, providing API endpoints for user registration, posts, comments, likes, and follows.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

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

## Usage
- Use Postman or any API client to make requests to the above endpoints.
- Register users, create posts, add comments, and interact with the app's social features.

