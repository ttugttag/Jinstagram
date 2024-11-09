from django.shortcuts import render, redirect
from rest_framework.views import APIView
from user.models import User
from content.models import Feed, Reply, Like, Bookmark, Follow
from . models import Product, AreaModel, BarModel, PieModel, TableApp, Samsung
from . forms import ProductForm
#plotly
from plotly.offline import plot
import plotly.graph_objects as go

# # matplotlib 1
from io import BytesIO
import matplotlib.pyplot as plt
import base64
# 아래는 선택사항
import matplotlib.font_manager as fm  # 한글폰트를 사용하기 위해.
import seaborn as sns
import pandas as pd

# # matplotlib 2
from .utils import get_plot

# matplotlib.use('AGG')

# Create your views here.
class Index(APIView):
    def get(self, request):
        # products=Product.objects.all()
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        # form = ProductForm()
        # return render(request, "chart/chart.html", context=dict(user=user, products=products, form=form))
        # return render(request, "chart/index.html", context=dict(user=user))
        areamodel = AreaModel.objects.all()
        barmodel = BarModel.objects.all()
        piemodel = PieModel.objects.all()
        tableapp = TableApp.objects.all()
        return render(request, "chart/index.html", context=dict(user=user,
                                                                areamodel=areamodel,
                                                                barmodel=barmodel,
                                                                piemodel=piemodel,
                                                                tableapp=tableapp))

    def post(self, request):
        # products=Product.objects.all()
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        areamodel = AreaModel.objects.all()
        barmodel = BarModel.objects.all()
        piemodel = PieModel.objects.all()
        tableapp = TableApp.objects.all()
        return render(request, "chart/index.html", context=dict(user=user,
                                                                areamodel=areamodel,
                                                                barmodel=barmodel,
                                                                piemodel=piemodel,
                                                                tableapp=tableapp))


class AddData(APIView):
    def get(self, request):
        products=Product.objects.all()
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        form = ProductForm()
        return render(request, "chart/adddata.html", context=dict(user=user,
                                                                  products=products,
                                                                  form=form))

    def post(self, request):
        products=Product.objects.all()
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chart:AddData')
        return render(request, "chart/adddata.html", context=dict(user=user,
                                                                  products=products,
                                                                  form=form ))

class Static(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/layout-static.html", context=dict(user=user))
    def post(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/layout-static.html", context=dict(user=user))

class Light(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/layout-sidenav-light.html", context=dict(user=user))
    def post(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/layout-sidenav-light.html", context=dict(user=user))

class MultiChart(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        areamodel = AreaModel.objects.all()
        barmodel = BarModel.objects.all()
        piemodel = PieModel.objects.all()
        return render(request, "chart/multichart.html", context=dict(user=user,areamodel=areamodel,barmodel=barmodel,piemodel=piemodel))
    def post(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        areamodel = AreaModel.objects.all()
        barmodel = BarModel.objects.all()
        piemodel = PieModel.objects.all()
        return render(request, "chart/multichart.html", context=dict(user=user,areamodel=areamodel,barmodel=barmodel,piemodel=piemodel))

class ChangeChart(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        samsung = Samsung.objects.all().order_by('-id')
        return render(request, "chart/changechart.html", context=dict(user=user,samsung=samsung))
    def post(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        samsung = Samsung.objects.all().order_by('-id')
        return render(request, "chart/changechart.html", context=dict(user=user,samsung=samsung))

class Tables(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        tableapp=TableApp.objects.all()
        return render(request, "chart/tables.html", context=dict(user=user,tableapp=tableapp))
    def post(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        tableapp = TableApp.objects.all()
        return render(request, "chart/tables.html", context=dict(user=user,tableapp=tableapp))

class Setting(APIView):
    def get(self, request):
        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()
        # print(user.id)

        if user is None:
            return render(request, "user/login.html")

        feed_list = Feed.objects.filter(email=email)
        like_list = list(Like.objects.filter(email=email, is_like=True).values_list('feed_id', flat=True))
        like_feed_list = Feed.objects.filter(id__in=like_list)
        bookmark_list = list(Bookmark.objects.filter(email=email, is_marked=True).values_list('feed_id', flat=True))
        bookmark_feed_list = Feed.objects.filter(id__in=bookmark_list)

        feed_count = Feed.objects.filter(email=email).count()
        following_count = Follow.objects.filter(email=email, is_follow=True).count()
        follow_count = Follow.objects.filter(follow_id=user.id, is_follow=True).count()

        return render(request, "chart/partials/setting.html", context=dict(feed_list=feed_list,
                                                                    like_feed_list=like_feed_list,
                                                                    bookmark_feed_list=bookmark_feed_list,
                                                                    user=user,
                                                                    feed_count=feed_count,
                                                                    follow_count=follow_count,
                                                                    following_count=following_count,
                                                                    ))

    def post(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/partials/setting.html", context=dict(user=user))

class Plotly_Sample(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/plotly_sample.html", context=dict(user=user))
    def post(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/plotly_sample.html", context=dict(user=user))

class Plotly_Sample(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        def scatter():
            x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]                      # <== {% for in  %}{{ var }} {% endfor %}
            y1 = [30, 35, 25, 45, 35, 45, 25, 35, 55]             # <== {% for in  %}{{ var }} {% endfor %}

            trace = go.Scatter(
                x=x1,
                y=y1
            )
            layout = dict(
                title='Simple Graph',
                xaxis=dict(range=[min(x1)-min(x1), max(x1)]),
                yaxis=dict(range=[min(y1)-min(y1), max(y1)])
            )

            fig = go.Figure(data=[trace], layout=layout)
            plot_div = plot(fig, output_type='div', include_plotlyjs=False)
            return plot_div

        context = {
            'plot1': scatter(),
            'user' : user
        }
        # return render(request, "chart/plotly_sample.html", context=dict(user=user))
        return render(request, "chart/plotly_sample.html", context)


class Plotly_Basic(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/plotly_basic.html",context=dict(user=user))
    def post(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/plotly_basic.html",context=dict(user=user))

class Plotly_Advance(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/plotly_advance.html",context=dict(user=user))
    def post(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/plotly_advance.html",context=dict(user=user))

class Matplotlib_Sample(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        dict_s = {
            'x1' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'y1' : [30, 35, 25, 45, 35, 45, 25, 35, 55],
            'z1': [2, 1, 2, 4, 3, 4, 2, 3, 5],
        }
        df = pd.DataFrame(dict_s)
        # print(df)
        # 그림그리기.
        plt.figure(figsize=(10, 12))
        sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=plt.cm.gist_heat, linecolor='white', annot=True)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')
        ## context['graphic'] = graphic
        content = {
            'graphic': graphic,
            'user': user
        }
        # return render(request, "chart/matplotlib_sample.html", {'graphic':graphic})
        return render(request, "chart/matplotlib_sample.html", content)

    def post(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/matplotlib_sample.html",context=dict(user=user))

class Matplotlib_Basic(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        qs =  Product.objects.all()
        x = [x.catagory for x in qs]
        y = [y.num_of_products for y in qs]
        chart= get_plot(x,y)
        return render(request, "chart/matplotlib_basic.html", {'chart':chart,'user':user,'qs':qs})
    def post(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/matplotlib_basic.html", {'chart':chart,'user':user})

class Matplotlib_Advance(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/matplotlib_advance.html", context=dict(user=user))
    def post(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        return render(request, "chart/matplotlib_advance.html", context=dict(user=user))
