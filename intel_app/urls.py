from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
from .auth import authViews

urlpatterns = [
                  path('', views.home, name="home"),
                  path('services', views.services, name='services'),
                  path('services/mtn', views.mtn, name='mtn'),
                  path('services/airtel-tigo/', views.airtel_tigo, name='airtel-tigo'),
                  path('services/voda/', views.voda, name='voda'),
                  path('services/afa/', views.afa_registration, name='afa'),
                  path('history/airtel-tigo', views.history, name='history'),
                  path('history/mtn', views.mtn_history, name="mtn-history"),
                  path('history/voda', views.voda_history, name="voda-history"),
                  path('history/afa', views.afa_history, name="afa-history"),
                  path('verify_transaction/<str:reference>/', views.verify_transaction, name="verify_transaction"),

                  path('history/big_time', views.big_time_history, name="bt-history"),
                  path('services/big_time/', views.big_time, name='big_time'),
                  path('bt_admin', views.admin_bt_history, name='bt_admin'),
                  path('bt_mark_as_sent/<int:pk>', views.bt_mark_as_sent, name='bt_mark_as_sent'),
                  path('big_time_pay_with_wallet/', views.big_time_pay_with_wallet, name='big_time_pay_with_wallet'),

                  path('afa_admin', views.admin_afa_history, name='afa_admin'),
                  path('voda_admin', views.admin_voda_history, name='voda_admin'),

                  path('mtn_admin/<str:status>', views.admin_mtn_history, name='mtn_admin'),
                  path('excel_status/<str:status>/<str:to_change_to>', views.change_excel_status, name='excel_status'),

                  path('import_thing', views.populate_custom_users_from_excel, name="import_users"),
                  path('delete', views.delete_custom_users, name='delete'),

                  path('mark_as_sent/<int:pk>', views.mark_as_sent, name='mark_as_sent'),
                  path('afa_mark_as_sent/<int:pk>', views.afa_mark_as_sent, name='afa_mark_as_sent'),
                  path('voda_mark_as_sent/<int:pk>', views.voda_mark_as_sent, name='voda_mark_as_sent'),
                  path('credit_user', views.credit_user, name='credit_user'),
                  path('pay_with_wallet/', views.pay_with_wallet, name='pay_with_wallet'),
                  path('mtn_pay_with_wallet/', views.mtn_pay_with_wallet, name='mtn_pay_with_wallet'),
                  path('voda_pay_with_wallet/', views.voda_pay_with_wallet, name='voda_pay_with_wallet'),
                  path('afa_pay_with_wallet/', views.afa_registration_wallet, name='afa_pay_with_wallet'),
                  path('voda_mark_as_sent/<int:pk>', views.voda_mark_as_sent, name='voda_mark_as_sent'),
                  path('topup-info', views.topup_info, name='topup-info'),
                  path("request_successful/<str:reference>", views.request_successful, name='request_successful'),
                  path('elevated/topup-list', views.topup_list, name="topup_list"),
                  path('credit/<str:reference>', views.credit_user_from_list, name='credit'),
                  path('paystack_webhook', views.paystack_webhook, name='paystack_webhook'),
                  path("password_reset/", views.password_reset_request, name="password_reset"),

                  path('query_transaction', views.query_txn, name='query_txn'),
                  path("upgrade-agent/", views.agent_upgrade, name="agent-upgrade"),

                  path('login', authViews.login_page, name='login'),
                  path('signup', authViews.sign_up, name='signup'),
                  path('logout', authViews.logout_user, name="logout")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
