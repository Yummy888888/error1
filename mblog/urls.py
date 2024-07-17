"""
URL configuration for mblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from mysite.views import PostDetailView, homepage  # 假設你的首頁視圖為 homepage

urlpatterns = [
    path('', homepage, name='home'),  # 空路徑對應到 homepage 視圖
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    # 其他路徑設置
]
