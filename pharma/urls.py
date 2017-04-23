from django.conf.urls import url, include
from . import views

app_name = 'pharma'

urlpatterns = [

    # /pharma/
    url(r'^$', views.index, name='index'),

    # /pharma/doctor/
    url(r'^doctor/$', views.doctor, name='doctor'),

# /pharma/doctor/
    url(r'^doctor/adddocs$', views.adddocs, name='adddocs'),

    # /pharma/doctor/
    url(r'^doctor/(?P<pk>[0-9]+)/deldocs$', views.deldocs, name='deldocs'),

    # /pharma/doctor/
    url(r'^doctor/(?P<pk>[0-9]+)/delmeds$', views.delmeds, name='delmeds'),

    # /pharma/doctor/
    url(r'^doctor/(?P<pk>[0-9]+)/delnonmeds', views.delnonmeds, name='delnonmeds'),

    # /pharma/doctor/
    url(r'^doctor/(?P<pk>[0-9]+)/delstaffs', views.delstaffs, name='delstaffs'),

    # /pharma/doctor/
    url(r'^doctor/adddocs/adddoc$', views.adddoc, name='adddoc'),

    # /pharma/doctor/
    url(r'^medicine/addmeds$', views.addmeds, name='addmeds'),

    # /pharma/doctor/
    url(r'^doctor/addmeds/addmed$', views.addmed, name='addmed'),

    # /pharma/doctor/
    url(r'^doctor/addnonmeds$', views.addnonmeds, name='addnonmeds'),

    # /pharma/doctor/
    url(r'^doctor/addnonmeds/addnonmed$', views.addnonmed, name='addnonmed'),

    # /pharma/doctor/
    url(r'^doctor/addstaffs$', views.addstaffs, name='addstaffs'),

    # /pharma/doctor/
    url(r'^doctor/addstaffs/addstaff$', views.addstaff, name='addstaff'),

    # /pharma/medicine/
    url(r'^medicine/$', views.medicine, name='medicine'),

    # /pharma/nonmedicine/
    url(r'^nonmedicine/$', views.nonmedicine, name='nonmedicine'),

    # /pharma/staff/
    url(r'^staff/$', views.staff, name='staff'),

    # /pharma/docs/Andheri
    url(r'^docs/(?P<site>[a-zA-Z]+)/$', views.dispdocs, name='dispdocs'),

    # /pharma/meds/Andheri
    url(r'^meds/(?P<site>[a-zA-Z]+)/$', views.dispmeds, name='dispmeds'),

    # /pharma/nonmeds/Andheri
    url(r'^nonmeds/(?P<site>[a-zA-Z]+)/$', views.dispnonmeds, name='dispnonmeds'),

    # /pharma/staff/Andheri
    url(r'^staff/(?P<site>[a-zA-Z]+)/$', views.dispstaff, name='dispstaff'),
# url(r'^staff/$', views.staff, name='staff'),

    url(r'^get_doctor/$', views.get_doctor),

    url(r'^get_medicine/$', views.get_medicine),

    url(r'^get_non_medicine/$', views.get_non_medicine),

    url(r'^get_staff/$', views.get_staff),

]