from django.test import TestCase, Client
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note content."
        )
    
    def test_note_creation(self):
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is a test note content.")
        self.assertIsNotNone(self.note.created_at)
    
    def test_note_string_representation(self):
        self.assertEqual(str(self.note), "Test Note")
    
    def test_get_short_content(self):
        long_content = "A" * 150
        note = Note.objects.create(title="Long Note", content=long_content)
        short_content = note.get_short_content(100)
        self.assertEqual(len(short_content), 103)
        self.assertTrue(short_content.endswith("..."))


class NoteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.note = Note.objects.create(
            title="Test Note",
            content="Test content"
        )
    
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
    
    def test_add_note_view(self):
        response = self.client.post(reverse('add_note'), {
            'title': 'New Note',
            'content': 'New content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title='New Note').exists())
    
    def test_delete_note_view(self):
        response = self.client.post(reverse('delete_note', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())
