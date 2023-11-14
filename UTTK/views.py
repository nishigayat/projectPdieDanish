from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UTTK_Member, Lecturer, Register_Case, Disciplinary_Case
from .forms import RegisterCaseUpdateForm, DisciplinaryCaseForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def uttk_member_login(request):
    if request.method == 'POST':
        uttk_id = request.POST.get('uttkID')
        uttk_pass = request.POST.get('uttkPass')

        # Retrieve the user based on the provided UTTK ID or raise a 404 error
        user = get_object_or_404(UTTK_Member, pk=uttk_id)

        if check_password(uttk_pass, user.uttkPass):
            # Log the user in
            login(request, user)
            # Add a debug print/log statement
            print(f"Successful login attempt for UTTK ID: {uttk_id}")
            
            # Add a success message using Django messages framework
            messages.success(request, 'You have successfully logged in!')
            
            # Redirect to the uttkHome page
            return redirect('uttkHome')
        else:
            print(f"Failed login attempt for UTTK ID: {uttk_id}")
            # Add an error message using Django messages framework
            messages.error(request, 'Invalid credentials. Please try again.')

            return render(request, 'login_uttk_member.html', {'error': 'Invalid credentials'})

    return render(request, 'login_uttk_member.html')

def uttkHome(request):
    return render(request, 'uttkHome.html')

def lecturer_login(request):
    if request.method == 'POST':
        lecturer_id = request.POST.get('lecID')
        lecturer_pass = request.POST.get('lecPass')

        # Retrieve the lecturer based on the provided ID or raise a 404 error
        lecturer = get_object_or_404(Lecturer, lecID=lecturer_id)

        if check_password(lecturer_pass, lecturer.lecPass):
            # Log the lecturer in
            login(request, lecturer)
            
            # Redirect to the home page or any other page you want
            return redirect('lecHome')
        else:
            return render(request, 'login_lecturer.html', {'error': 'Invalid credentials'})

    return render(request, 'login_lecturer.html')

def lecHome(request):
    return render(request, 'lecHome.html')

def registeroffencesform(request):
    if request.method == 'POST':
        # Process and save the form data
        case_code = request.POST.get('caseCode')
        case_class = request.POST.get('caseClass')
        offenses = request.POST.get('offences')
        punishment = request.POST.get('punishment')
        comment = request.POST.get('registerText')

        # Save the data to the Register_Case model
        case = Register_Case(
            caseCode=case_code,
            caseClass=case_class,
            offences=offenses,
            punishment=punishment,
            registerText=comment
        )
        case.save()

        return redirect('registeroffences_list')

    return render(request, 'registeroffencesform.html')

def registeroffences_list(request):
    # Retrieve a list of cases from the database
    cases = Register_Case.objects.all()

    for case in cases:
        print(f"Case Code: {case.caseCode}, Case Class: {case.caseClass}, Offences: {case.offences}")

    context = {
        'cases': cases,
    }
    return render(request, 'registeroffences_list.html', context)

def update_case(request, case_code):
    case = get_object_or_404(Register_Case, caseCode=case_code)

    if request.method == 'POST':
        form = RegisterCaseUpdateForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('registeroffences_list')
    else:
        form = RegisterCaseUpdateForm(instance=case)

    context = {
        'form': form,
        'case': case,
    }
    return render(request, 'update_case.html', context)


def delete_case(request, case_code):
    case = get_object_or_404(Register_Case, caseCode=case_code)

    if request.method == 'POST':
        case.delete()
        return redirect('registeroffences_list')

    context = {
        'case': case,
    }
    return render(request, 'delete_case.html', context)

def disciplinarycase(request):
    if request.method == 'POST':
        form = DisciplinaryCaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disciplinary_case_list')
    else:
        form = DisciplinaryCaseForm()

    context = {'form': form}
    return render(request, 'disciplinarycase.html', context)

def disciplinary_case_list(request):
    cases = Disciplinary_Case.objects.all()
    context = {'cases': cases}
    return render(request, 'disciplinary_case_list.html', context)


def lec_disciplinary_case(request):
    if request.method == 'POST':
        form = DisciplinaryCaseForm(request.POST)
        if form.is_valid():
            form.save()
            # Add a success message using Django's messages framework
            messages.success(request, 'Data has been saved successfully.')
        else:
            # Add an error message if the form is not valid
            messages.error(request, 'Failed to save data. Please check the form.')

    else:
        form = DisciplinaryCaseForm()

    context = {
        'form': form,
    }
    return render(request, 'lec_disciplinary_case.html', context)


def delete_disciplinary_case(request, pk):
    case = get_object_or_404(Disciplinary_Case, pk=pk)

    if request.method == 'POST':
        case.delete()
        return redirect('disciplinary_case_list')

    context = {
        'case': case,
    }
    return render(request, 'delete_disciplinary_case.html', context)

