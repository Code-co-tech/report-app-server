from django.urls import path
from report_app.reports.views import BobView, TypeOfWorkView
from report_app.report_user.views import UserReportReceivedView, UserReportReturnView, UserReportsView, UserReportView
from report_app.report_contractor.views import ContractorReporNewView, ContractorReporReceivedView, ContractorReportReturnView, ContractorReportsView, ContractorReportView
from report_app.report_customer.views import CustomerReporNewView, CustomerReporReceivedView, CustomerReportReturnView, CustomerReportsView, CustomerReportView


urlpatterns = [
    # Reports
    path('report/section/', BobView.as_view()),
    path('report/type_work/', TypeOfWorkView.as_view()),
    # User Reports
    path('report/user/received/', UserReportReceivedView.as_view()),
    path('report/user/returned/', UserReportReturnView.as_view()),
    path('report/user/', UserReportsView.as_view()),
    path('report/user/<int:pk>/', UserReportView.as_view()),
    # Contractor Reports
    path('report/contractor/new/', ContractorReporNewView.as_view()),
    path('report/contractor/received/', ContractorReporReceivedView.as_view()),
    path('report/contractor/returned/', ContractorReportReturnView.as_view()),
    path('report/contractor/', ContractorReportsView.as_view()),
    path('report/contractor/<int:pk>/', ContractorReportView.as_view()),
    # Customer Reports
    path('report/customer/new/', CustomerReporNewView.as_view()),
    path('report/customer/received/', CustomerReporReceivedView.as_view()),
    path('report/customer/returned/', CustomerReportReturnView.as_view()),
    path('report/customer/', CustomerReportsView.as_view()),
    path('report/customer/<int:pk>/', CustomerReportView.as_view()),


]