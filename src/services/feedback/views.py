from django.views.generic.edit import FormView
from .forms import CustomFeedbackForm
from django.contrib import messages


class FormView(FormView):
    template_name = 'feedback/feedback.html'
    form_class = CustomFeedbackForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you for submitting your Feedback!')
        return super().form_valid(form)
