from django.shortcuts import render , redirect
from .forms import CalcForm

# Create your views here.

def index(request):
    result = None  # default value for result

    #check whether the user has submitted the form or is just viewing it
    if request.method == 'POST':

        # get the form
        form = CalcForm(request.POST)

        if form.is_valid():
            # access cleaned data
            first_num = form.cleaned_data['first_number']
            second_num = form.cleaned_data['second_number']
            operation = form.cleaned_data['operation']

            # math logic
            if operation == 'Add':
                result = first_num + second_num

            elif operation == 'Subtract':
                result = first_num - second_num
            elif operation == 'Multiply':
                result = first_num * second_num
            elif operation == 'divide':
                if second_num != 0:
                    result = first_num / second_num

                else:
                    result = "Cannot divide by zero!"


    else  :
        form = CalcForm()
    return render(request , 'calculator.html' , {'form' : form ,
                                                 'result' : result})