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


def generate_countour_plot(request):
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


def generate_area_chart(request):
    data = pd.read_csv(settings.DATASET_PATH)
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

def home(request):
    # Your view logic here
    return render(request, 'home.html')  # Replace 'home.html' with the actual template you want to render
