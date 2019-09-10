from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from plab.models import Profile, Institutions, Donations
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import SignUpForm, AddInstitutionsForm, AddDonationsForm
from django.contrib.auth import login, authenticate


def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm()
        return render(request, 'register.html', {'form': form})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class HomePageView(View):
    def get(self, request):
        return render(request, "index.html")


class LoginPageView(View):
    def get(self, request):
        return render(request, "login.html")


class RegisterPageView(View):
    def get(self, request):
        return render(request, "register.html")


class FormPageView(View):
    def get(self, request):
        return render(request, "form.html")


class ProfileList(ListView):
    model = Profile

class ProfileView(DetailView):
    model = Profile

class ProfileCreate(CreateView):
    model = Profile
    fields = ['user','bio','location']
    success_url = reverse_lazy('profile_new')

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['user','bio','location']
    success_url = reverse_lazy('profile_list')

class ProfileDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('proflie_list')


class ShowTrustedInstitutionsView(View):

    def get(self, request, id):
        get_institutions = get_object_or_404(Institutions, pk=id)
        ctx = {"institutions": get_institutions}
        return render(request, "trusted_institutions.html", ctx)


class AddInstitutionsView(View):

    def get(self, request):
        form = AddInstitutionsForm()
        ctx = {"form": form}
        return render(request, "add_institution.html", ctx)

    def post(self, request):
        form = AddInstitutionsForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data['name']
            c1 = form.cleaned_data['city']
            t1 = form.cleaned_data['target']
            a1 = form.cleaned_data['address']

            new_institutions = Institutions.objects.create(
                name=n1,
                city=c1,
                target=t1,
                address=a1)

            return redirect('/institution/{}'.format(new_institutions.pk))

        ctx = {"form": form}
        return render(request, "add_institution.html", ctx)

class DeleteInstitutionsView(DeleteView):

    model = Institutions
    template_name = 'institution_delete.html'

    def get_success_url(self, *args, **kwargs):
        return self.request.GET.get('next', reverse_lazy('institution_list'))


class InstitutionsUpdate(UpdateView):
    model = Institutions
    fields = ['name','city','target','address']
    success_url = reverse_lazy('institution_edit')


class InstitutionsList(ListView):
    model = Institutions

"""
class DonationsList(ListView):
    model = Donations

class AddDonationsView(View):

    def get(self, request):
        form = AddDonationsForm()
        ctx = {"form": form}
        return render(request, "add_donation.html", ctx)

    def post(self, request):
        form = AddDonationsForm(request.POST)
        if form.is_valid():
            u1 = form.cleaned_data['user']
            dt1 = form.cleaned_data['donation_type']
            nob1 = form.cleaned_data['number_of_bags']
            rt1 = form.cleaned_data['recipient_type']
            i1 = form.cleaned_data['institution']
            c1 = form.cleaned_data['city']
            dd1 = form.cleaned_data['donation_date']
            pa1 = form.cleaned_data['pickup_address']
            p1 = form.cleaned_data['phone']
            pd1 = form.cleaned_data['pickup_date']
            tn1 = form.cleaned_data['transport_notes']
            ts1 = form.cleaned_data['transfer_status']

            new_donations = Donations.objects.create(
                user=u1,
                donation_type=dt1,
                number_of_bags=nob1,
                recipient_type=rt1,
                institution=i1,
                city=c1,
                donation_date=dd1,
                pickup_address=pa1,
                phone=p1,
                pickup_date=pd1,
                transport_notes=tn1,
                transfer_status=ts1)

            return redirect('/donations/{}'.format(new_donations.pk))

        ctx = {"form": form}
        return render(request, "add_donation.html", ctx)
"""
