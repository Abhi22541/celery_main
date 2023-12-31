from django import forms
from feedback.tasks import send_feedback_email_task

class FeedbackForm(forms.Form):
    email=forms.EmailField(label='email')
    messages=forms.CharField(label='message', widget=forms.Textarea(attrs={"row":5}))
    def send_email(self):
         send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["messages"]
        )