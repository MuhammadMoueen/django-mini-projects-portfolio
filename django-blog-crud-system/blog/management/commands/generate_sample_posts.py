from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post
import random

class Command(BaseCommand):
    help = 'Generate sample blog posts for testing'

    def handle(self, *args, **kwargs):
        titles = [
            'Introduction to Django Web Development',
            'Building RESTful APIs with Python',
            'Best Practices for Database Design',
            'Understanding Authentication Systems',
            'Modern CSS Techniques',
            'JavaScript Frameworks Comparison',
            'DevOps and Continuous Integration',
            'Machine Learning Basics',
            'Cloud Computing Essentials',
            'Cybersecurity Best Practices',
        ]
        
        contents = [
            'This is a comprehensive guide exploring the fundamental concepts and advanced techniques. Learn how to build scalable applications with clean architecture and best practices.',
            'Discover the powerful features and capabilities that make development efficient and maintainable. This post covers everything from basics to advanced patterns.',
            'Deep dive into professional development practices that will elevate your coding skills. Real-world examples and practical demonstrations included.',
            'Explore the modern approaches to building robust and secure applications. This guide provides step-by-step instructions and code examples.',
            'A detailed walkthrough of implementing industry-standard solutions in your projects. Learn from experienced developers and avoid common pitfalls.',
        ]
        
        if not User.objects.filter(username='demo').exists():
            demo_user = User.objects.create_user(
                username='demo',
                email='demo@example.com',
                password='demo123456'
            )
            self.stdout.write(self.style.SUCCESS('Created demo user'))
        else:
            demo_user = User.objects.get(username='demo')
        
        for i, title in enumerate(titles):
            content = random.choice(contents)
            Post.objects.create(
                title=title,
                content=content,
                author=demo_user
            )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(titles)} sample posts'))
