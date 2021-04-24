from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


class TaskListView(ListView):
    model = Task
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        if 'sort_field' in self.request.GET:
            context['sort_field'] = self.request.GET.get('sort_field')
            context['sort_direction'] = self.request.GET.get('sort_direction')
        else:
            context['sort_field'] = 'id'
            context['sort_direction'] = 'asc'
        return context

    def get_ordering(self):
        if 'sort_field' in self.request.GET:
            sort_field = self.request.GET.get('sort_field')
            sort_direction = self.request.GET.get('sort_direction')
            if sort_direction == 'desc':
                sort_field = f'-{sort_field}'
            return [sort_field]


class TaskCreate(CreateView, SuccessMessageMixin):
    model = Task
    fields = ['username', 'email', 'text']
    success_message = 'Task successfully created!'
    success_url = reverse_lazy('tasks')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['text', 'status']
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
