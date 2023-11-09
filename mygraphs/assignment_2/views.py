# appname/views.py
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from django.http import HttpResponse
from django.conf import settings
from scipy.stats import gaussian_kde
import pandas as pd
from io import BytesIO
import os
import numpy as np


def generate_scatter_plot(request):
    # data = pd.read_csv(settings.DATASET_PATH)
    # plt.scatter(data['house_age'], data['house_price_of_unit_area'])
    # plt.title('House Age vs. Price (Scatter Plot)')
    # plt.xlabel('House Age')
    # plt.ylabel('Price (unit area)')
    # response = HttpResponse(content_type='image/png')
    # plt.savefig(response, format='png')
    # return response

     # Load the dataset
    data = pd.read_csv(settings.DATASET_PATH)

    # Generate contour plot
    contour_plot = BytesIO()
    x = data['petal_length']
    y = data['petal_width']
    z = gaussian_kde(np.vstack([x, y]))(np.vstack([x, y]))
    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]
    plt.figure(figsize=(10, 6))
    plt.tricontourf(x, y, z, levels=14, cmap="viridis")
    plt.colorbar()
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Petal Width (cm)')
    plt.title('Contour Plot of Petal Length and Width')
    plt.savefig(contour_plot, format='png')
    # plt.close()
    response = HttpResponse(content_type='image/png')
    plt.savefig(response, format='png')
    return response


def generate_bar_chart(request):
    data = pd.read_csv(settings.DATASET_PATH)
    # bar_data = data.groupby('number_of_convenience_stores')['house_price_of_unit_area'].mean().reset_index()
    # fig = px.bar(bar_data, x='number_of_convenience_stores', y='house_price_of_unit_area', title='Average Price by Convenience Stores (Bar Chart)')
    # html_div = fig.to_html(full_html=False)
    # return HttpResponse(html_div)
    # Generate area plot
    area_plot = BytesIO()
    plt.figure(figsize=(10, 6))
    plt.stackplot(range(len(data)), data['petal_length'], data['petal_width'], labels=['Petal Length', 'Petal Width'], alpha=0.5)
    plt.legend(loc='upper left')
    plt.xlabel('Sample Number')
    plt.ylabel('Measurement (cm)')
    plt.title('Area Plot of Petal Length and Width')
    plt.savefig(area_plot, format='png')
    response = HttpResponse(content_type='image/png')
    plt.savefig(response, format='png')
    plt.close()
    return response
    # html_div = fig.to_html(full_html=False)
    # return HttpResponse(html_div)


def home(request):
    # Your view logic here
    return render(request, 'home.html')  # Replace 'home.html' with the actual template you want to render
