from django.shortcuts import render, get_object_or_404
from .forms import QuestionForm
from .models import Question

def question_view(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            # Process the form data
            question_text = form.cleaned_data['question_text']
            # Perform any additional actions with the question text
            # ...
            return render(request, 'success.html')
    else:
        form = QuestionForm(instance=question)
    
    return render(request, 'question.html', {'form': form})