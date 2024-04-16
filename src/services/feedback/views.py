from django.views.generic.edit import FormView
from .forms import Feedback
from django.contrib import messages


class FormView(FormView):
    template_name = 'your_template.html'
    form_class = Feedback

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def success_message(self):
        return messages.success(self.request, 'Thank you for submitting your FeedBack!')
