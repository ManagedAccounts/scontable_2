from django.shortcuts import render
from django.views.generic import FormView, TemplateView, RedirectView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse


# Create your views here.

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
    success_url =  reverse_lazy("inicio")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('login'))
        else:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class ControlPanelView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(ControlPanelView, self).get_context_data(**kwargs)
        #context['pedidos_pendientes'] = Nombre.objects.name()
        # ....
        # Recopilar resto de la informacion
        # ....

        return context


