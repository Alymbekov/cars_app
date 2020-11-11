from django.urls import reverse_lazy
from django.views import generic

from tasks.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks' #object_list


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    fields = ('title', 'description', )
    success_url = reverse_lazy('tasks:task_list')

    def get_success_url(self):
        return reverse_lazy(
            'tasks:task_detail',
            kwargs={'pk': self.object.pk}
        )


class TaskEditView(generic.UpdateView):
    model = Task
    template_name = 'tasks/task_edit.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy(
            'tasks:task_detail',
            kwargs={'pk': self.object.pk}
        )


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks:task_list')



