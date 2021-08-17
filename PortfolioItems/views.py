from django.shortcuts import render
from .models import Portfolio

# Create your views here.

def PortfolioItems(request):
    portfolio_items = Portfolio.objects.all()
    return  render(request,'PortfolioDjango/index.html', {'portfolio_items':portfolio_items})
