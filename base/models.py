from django.db import models

# Create your models here.

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=30, blank=True)
    avatar_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    language = models.CharField(max_length=10, blank=True)
    mentor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='mentees')

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    section = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class CourseMaterial(models.Model):
    MATERIAL_TYPES = (
        ('video', 'Video'),
        ('exercise', 'Exercise'),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    material_type = models.CharField(max_length=10, choices=MATERIAL_TYPES)
    content = models.TextField()

    def __str__(self):
        return f"{self.course.title} - {self.get_material_type_display()}"

class UserProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    material = models.ForeignKey(CourseMaterial, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
