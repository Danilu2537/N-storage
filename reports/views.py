import plotly
import plotly.graph_objects as go
from django.shortcuts import render

from movement.models import Units
from storages.models import Storage, Technic


def index(request):
    return render(request, 'index.html')


def storages(request):
    storages = Storage.objects.all()
    tables = []
    if ids := request.GET.getlist('id'):
        for id in ids:
            units = Units.objects.filter(
                storage=(storage := Storage.objects.get(id=id))
            )
            table = [
                [unit.technic.model for unit in units],
                [unit.count for unit in units],
            ]
            fig = go.Figure(
                layout={'title': {'text': f'{storage.title}'}},
                data=[
                    go.Table(
                        header=dict(
                            values=['Модель', 'Количество'], align='left', font_size=16
                        ),
                        cells=dict(
                            height=30,
                            values=table,
                            fill_color=['bisque'],
                            align='left',
                            font_size=16,
                        ),
                    )
                ],
            )
            tables.append(
                plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
            )
    return render(
        request, 'storages.html', context={'storages': storages, 'tables': tables}
    )


def technics(request):
    technics = sorted(Technic.objects.all(), key=lambda x: x.model)
    tables = []
    if ids := request.GET.getlist('id'):
        units = []
        for id in ids:
            units += Units.objects.filter(technic=Technic.objects.get(id=id))
        counts = {}
        for unit in units:
            if unit.technic.model in counts:
                counts[unit.technic.model] += unit.count
            else:
                counts[unit.technic.model] = unit.count
        table = [[key for key in counts.keys()], [value for value in counts.values()]]
        print(table)
        fig = go.Figure(
            data=[
                go.Table(
                    header=dict(
                        values=['Модель', 'Количество'], align='left', font_size=16
                    ),
                    cells=dict(
                        height=30,
                        values=table,
                        fill_color=['bisque'],
                        align='left',
                        font_size=16,
                    ),
                )
            ]
        )
        tables.append(
            plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
        )
    return render(
        request, 'technics.html', context={'technics': technics, 'tables': tables}
    )


def hist(request):
    technics = [{'model': 'По всей технике', 'id': -1}] + sorted(
        Technic.objects.all(), key=lambda x: x.model
    )
    hist = ''
    if id := request.GET.get('select'):
        if id == '-1':
            units = Units.objects.all()
            counts = {}
            for unit in units[1:]:
                if unit.technic.model in counts:
                    counts[unit.technic.model] += unit.count
                else:
                    counts[unit.technic.model] = unit.count
            fig = go.Figure(
                layout={'title': {'text': 'Кумулятивная гистограмма'}},
                data=[
                    go.Histogram(
                        x=[count for count in counts.values()], cumulative_enabled=True
                    )
                ],
            )
        else:
            units = Units.objects.filter(
                technic=(technic := Technic.objects.get(id=id))
            )
            fig = go.Figure(
                layout={'title': {'text': f'{technic.model}'}},
                data=[go.Histogram(x=[unit.count for unit in units])],
            )
        hist = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    return render(request, 'hist.html', context={'technics': technics, 'hist': hist})
