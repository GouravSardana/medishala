from django.contrib.auth.models import User, Group
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from django.views.generic import TemplateView
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.list import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from home.models import Blood_Sample, Request_button


class Home(TemplateView):
    template_name = 'home.html'

class SignUp(TemplateView):
    template_name = 'signup.html'
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            first_name = self.request.POST.get('first_name')
            last_name = self.request.POST.get('last_name')
            email=self.request.POST.get('email')
            username = self.request.POST.get('username')
            password= self.request.POST.get('password')
            form = User.objects.create_user(first_name=first_name, last_name=last_name,email=email, username=username,password=password)  # = wala model ka naam
            form.save()
            # User.groups.add(pk=1)
            return HttpResponseRedirect(reverse('user_login'))


class LogIn(TemplateView):
    template_name = 'login.html'


def user_login(request):

    if request.method == 'POST':
        # First get the username and password suppliedddfhd

        username = request.POST.get('username')
        password = request.POST.get('password')


        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)

                if user.groups.filter(name='Hospital'):
                    return HttpResponseRedirect(reverse('patient_details'))
                else:
                    return HttpResponseRedirect(reverse('patient'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'login.html', {})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('home'))


def not_in_student_group(user):
    if user:
        return user.groups.filter(name='Hospital').count() == 0
    return False



# @method_decorator(login_required, name='dispatch')
class TestMixin1(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Hospital')


class Patient_details(TestMixin1, ListView):
    model=Blood_Sample
    template_name = 'patient-details.html'
    # def get_queryset(self):
    #     return Patient.objects.filter(provider=self.request.user).order_by('-id')
    # def get_queryset(self):
    #     return User.objects.filter(groups__name='Doctor')

    # def get(self, request, *args, **kwargs):
    #     features = User.objects.filter(groups__name='Doctor')
    #     patient = Patient_Detail.objects.all()
    #     hospital=Hospital.objects.all()
    #     return render(request, 'patient-details.html', {'f': features, 'p': patient, 'hospital':hospital})


    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            user=request.user
            name = self.request.POST.get('name')
            user_email=self.request.POST.get('user_email')
            blood_group=self.request.POST.get('blood_group')
            dob=self.request.POST.get('dob')
            hospital=self.request.POST.get('hospital')
            desc=self.request.POST.get('desc')
            form = Blood_Sample(user=user, name=name, user_email=user_email, blood_group=blood_group, dob=dob, hospital=hospital, desc=desc)
            form.save()
            return HttpResponseRedirect(reverse('patient'))


class Request(ListView):
    model = Request_button
    template_name = 'request_button.html'


    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = self.request.POST.get('name')
            blood_group=self.request.POST.get('blood_group')
            dob=self.request.POST.get('dob')
            quantity=self.request.POST.get('quantity')
            desc=self.request.POST.get('desc')
            form = Request_button(name=name, blood_group=blood_group, dob=dob, quantity=quantity, desc=desc)
            form.save()
            return HttpResponseRedirect(reverse('patient'))


# class Medical_lib(ListView):
#     template_name = 'diseases.html'
#     model = Medical_Library
#
#     def get(self, request, *args, **kwargs):
#         library = Medical_Library.objects.all()
#         print(library)
#         return render(request, 'diseases.html', {'library': library})


@method_decorator(login_required, name='dispatch')
class View_Patient(ListView):
    template_name = 'view_patient.html'


    def get(self, request, *args, **kwargs):
        # features = User.objects.filter(groups__name='Doctor')
        req=Request_button.objects.all()
        return render(request, 'view_patient.html', {'req': req})


