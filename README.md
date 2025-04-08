# API Documentation

This file provides an overview of the available endpoints for managing posts and comments in the application.

---

## **Posts Routes**

### **1. List and Create Posts**
| Method | Endpoint         | Description                           |
|--------|------------------|---------------------------------------|
| GET    | `/posts/`        | Retrieve a list of all posts.         |
| POST   | `/posts/`        | Create a new post.                    |

---

### **2. Post Details**
| Method | Endpoint             | Description                                |
|--------|----------------------|--------------------------------------------|
| GET    | `/posts/<int:pk>/`  | Retrieve details of a specific post by ID (`pk`). |
| PUT    | `/posts/<int:pk>/`  | Update the details of a specific post by ID (`pk`). |
| DELETE | `/posts/<int:pk>/`  | Delete a specific post by ID (`pk`).       |

---

## **Comments Routes**

### **1. Post Comments**
| Method | Endpoint                        | Description                                 |
|--------|---------------------------------|---------------------------------------------|
| GET    | `/posts/<int:pk>/comments`     | Retrieve comments for a specific post by ID (`pk`). |
| POST   | `/posts/<int:pk>/comments`     | Add a new comment to a specific post by ID (`pk`). |

---

### **2. Comment Details**
| Method | Endpoint                                 | Description                                 |
|--------|-----------------------------------------|---------------------------------------------|
| GET    | `/posts/<int:post_id>/comments/<int:pk>/` | Retrieve details of a specific comment by ID (`pk`) within a post (`post_id`). |
| PUT    | `/posts/<int:post_id>/comments/<int:pk>/` | Update a specific comment by ID (`pk`) within a post (`post_id`). |
| DELETE | `/posts/<int:post_id>/comments/<int:pk>/` | Delete a specific comment by ID (`pk`) within a post (`post_id`). |

---

## Notes
1. Replace `<int:pk>` and `<int:post_id>` with the actual IDs of the post or comment.
2. These routes are designed for efficient management of posts and their associated comments.
3. Proper authentication and role-based access control may be required to access these endpoints.

---

## Example Request

### Retrieve Comments for a Post
```http
GET /posts/1/comments
