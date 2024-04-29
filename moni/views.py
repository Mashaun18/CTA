from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TradingSection, TradeCommand

@login_required
def cta_dashboard(request):
    trading_sections = TradingSection.objects.filter(trader=request.user)
    return render(request, 'moni/dashboard.html', {'trading_sections': trading_sections})
@login_required
def add_section(request):
    return render(request, 'moni/add_section.html')

@login_required
def create_section(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        new_section = TradingSection(name=name, description=description, trader=request.user)
        new_section.save()
        return redirect('/ctadashboard')
    else:
        return render(request, 'moni/add_section.html')

@login_required
def delete_section(request, section_id):
    section = TradingSection.objects.get(pk=section_id)
    section.delete()
    return redirect('moni_dashboard')


@login_required
def execute_command(request):
    if request.method == 'POST':
        section_id = request.POST.get('section_id')
        command = request.POST.get('command')
        section = TradingSection.objects.get(pk=section_id)
        trade_command = TradeCommand.objects.create(section=section, command=command)
        return redirect('moni_dashboard')
    else:
        return render(request, 'moni/execute_command.html')
    
