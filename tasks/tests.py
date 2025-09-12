from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from tasks.models import Task

class TaskTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_tasks(self):
        response = self.client.get(reverse('task-list-create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_add_task(self):
        response = self.client.post(reverse('task-list-create'), {'title': 'Test Task'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['title'], 'Test Task')

    def test_add_task_missing_title(self):
        response = self.client.post(reverse('task-list-create'), {}, format='json')
        self.assertEqual(response.status_code, 400)

    def test_update_task(self):
        task = Task.objects.create(title='Update Me')
        response = self.client.put(reverse('task-detail', args=[task.id]), {'title': 'Updated', 'done': True}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['done'])

    def test_delete_task(self):
        task = Task.objects.create(title='Delete Me')
        response = self.client.delete(reverse('task-detail', args=[task.id]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Task.objects.count(), 0)