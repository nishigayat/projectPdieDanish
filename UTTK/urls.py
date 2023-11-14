from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("uttk_member_login/", views.uttk_member_login, name="uttk_member_login"),
    path('uttkHome/', views.uttkHome, name='uttkHome'),
    path("lecturer_login/", views.lecturer_login, name="lecturer_login"),
    path("lecHome/", views.lecHome, name="lecHome"),
    path('registeroffencesform/', views.registeroffencesform, name='registeroffencesform'),
    path("registeroffences_list/", views.registeroffences_list, name="registeroffences_list"),
    path("disciplinarycase/", views.disciplinarycase, name="disciplinarycase"),
    path("disciplinary_case_list/", views.disciplinary_case_list, name="disciplinary_case_list"),
    path('lec_disciplinary_case/', views.lec_disciplinary_case, name='lec_disciplinary_case'),
    path("update_case/<str:case_code>/", views.update_case, name="update_case"),
    path("delete_case/<str:case_code>/", views.delete_case, name="delete_case"),
    path("delete_disciplinary_case/<int:pk>/", views.delete_disciplinary_case, name="delete_disciplinary_case"),
]
