from django.test import TestCase
from django.urls import reverse
from .models import Task
from .forms import TaskForm

class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(
            title="Тестовая задача",
            description="Описание тестовой задачи"
        )
        self.assertEqual(task.title, "Тестовая задача")
        self.assertFalse(task.completed)

class TaskViewTest(TestCase):
    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Мои задачи")

    def test_add_task_view(self):
        response = self.client.post(reverse('add_task'), {
            'title': 'Новая задача',
            'description': 'Описание'
        })
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertEqual(Task.objects.count(), 1)

class TaskFormTest(TestCase):
    def test_valid_form(self):
        form = TaskForm(data={
            'title': 'Тестовая задача',
            'description': 'Тестовое описание'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = TaskForm(data={'title': ''})
        self.assertFalse(form.is_valid())

