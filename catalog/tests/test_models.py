from django.test import TestCase

from catalog.models import Author, Language, Genre, Book, BookInstance

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        au = Author(first_name='Big', last_name='Bob')
        au.save()

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(pk=1)
        field_lab = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_lab, 'last name')

    def test_date_of_birth_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.first_name} {author.last_name}'
        self.assertEqual(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')

class LanguageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Language.objects.create(name='Yorùbá')

    def test_language_name(self):
        lang = Language.objects.get(id=1)
        lang_label = lang._meta.get_field('name').verbose_name
        self.assertEqual(lang_label, 'name')

    def test_lang_length(self):
        lang = Language.objects.get(id=1)
        lang_len = lang._meta.get_field('name').max_length
        self.assertEqual(lang_len, 50)

class GenreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name='Horror')

    def test_genre_name(self):
        genre = Genre.objects.get(id=1)
        genre_label = genre._meta.get_field('name').verbose_name
        self.assertEqual(genre_label, 'name')

    def test_genre_length(self):
        genre = Genre.objects.get(id=1)
        genre_len = genre._meta.get_field('name').max_length
        self.assertEqual(genre_len, 200)

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(first_name='Fidimaye',
                              last_name='Saheed')
        author.save()
        genre = Genre.objects.create(name='Action')
        genre.save()
        lang = Language.objects.create(name='English')
        lang.save()
        book = Book.objects.create(title='Godsend',
                            author=author,
                            isbn='hsjavskagsj3g',
                            summary='Oluwaranmi',
                           # genre=genre,
                            language=lang)
        book.genre.add(genre)

    def test_title_label(self):
        book = Book.objects.get(id=1)
        book_lab = book._meta.get_field('title').verbose_name
        self.assertEqual(book_lab, 'title')

    def test_title_length(self):
        book = Book.objects.get(id=1)
        book_len = book._meta.get_field('title').max_length
        self.assertEqual(book_len, 200)

    def test_summary_length(self):
        book = Book.objects.get(id=1)
        summary = book._meta.get_field('summary').verbose_name
        self.assertEqual(summary, 'summary')

    def test_summary_length(self):
        book = Book.objects.get(id=1)
        summ_len = book._meta.get_field('summary').max_length
        self.assertEqual(summ_len, 1000)

class BookInstanceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(first_name='Fidimaye',
                               last_name='Saheed')
        author.save()
        genre = Genre.objects.create(name='Action')
        genre.save()
        lang = Language.objects.create(name='English')
        lang.save()
        book = Book.objects.create(title='Godsend',
                                author=author,
                                isbn='hsjavskagsj3g',
                                summary='Oluwaranmi',
                             # genre=genre,
                                language=lang)
        book.genre.add(genre)
        BookInstance.objects.create(book=book)

    def test_id_label(self):
        book = BookInstance.objects.get()
        b_lab = book._meta.get_field('id').verbose_name
        self.assertEqual(b_lab, 'id')

    def test_imprint(self):
        book = BookInstance.objects.get()
        b_len, b_lab = (book._meta.get_field('imprint').max_length,
                        book._meta.get_field('imprint').verbose_name)
        self.assertEqual(b_len, 200)
        self.assertEqual(b_lab, 'imprint')
