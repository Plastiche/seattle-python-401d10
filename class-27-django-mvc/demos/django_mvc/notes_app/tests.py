from django.test import TestCase, RequestFactory
from .models import Note


class TestNoteModel(TestCase):
    """
    """
    def setUp(self):
        """
        """
        Note.objects.create(title='Feed the cat', detail='She\'s hangry.')
        Note.objects.create(title='Get groceries', detail='We have none.')
        Note.objects.create(title='Change diaper', detail='It stanky.', status='complete')

    # def setUpClass(cls):
    #     """
    #     """
    #     pass

    def test_note_titles(self):
        """
        """
        one = Note.objects.get(title='Feed the cat')
        self.assertEqual(one.title, 'Feed the cat')

    def test_note_descriptions(self):
        """
        """
        notes = Note.objects.all()
        self.assertEqual(notes[2].detail, 'It stanky.')

    def test_note_status(self):
        """
        """
        one = Note.objects.get(title='Feed the cat')
        two = Note.objects.get(title='Change diaper')
        self.assertEqual(one.status, 'incomplete')
        self.assertEqual(two.status, 'complete')

    def test_create_new_note(self):
        """
        """
        new_note = Note.objects.create(title='new', detail='')
        self.assertEqual(new_note.title, 'new')


class TestNoteViews(TestCase):
    """
    """
    def setUp(self):
        """
        """
        self.request = RequestFactory()

        self.note = Note.objects.create(title='Feed the cat', detail='She\'s hangry.')
        Note.objects.create(title='Get groceries', detail='We have none.')
        Note.objects.create(title='Change diaper', detail='It stanky.', status='complete')

    def test_list_view_context(self):
        """
        """
        from .views import note_list_view
        request = self.request.get('')
        response = note_list_view(request)
        self.assertIn(b'Feed the cat', response.content)

    def test_list_view_status(self):
        """
        """
        from .views import note_list_view
        request = self.request.get('')
        response = note_list_view(request)
        self.assertEqual(200, response.status_code)

    def test_detail_view_context(self):
        """
        """
        from .views import note_detail_view
        request = self.request.get('')
        response = note_detail_view(request, self.note.id)
        self.assertIn(b'hangry.', response.content)

    def test_detail_view_status_code_failure(self):
        """
        """
        from .views import note_detail_view
        from django.http import Http404
        request = self.request.get('')

        with self.assertRaises(Http404):
            note_detail_view(request, '0')
