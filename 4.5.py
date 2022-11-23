import pandas as pd
import plotly.graph_objs as go
import matplotlib

matplotlib.use('TkAgg')

df = pd.read_csv('insurance.csv')

box_colormap = ["#0D8FEC", "#0479B6", "#0941CF", "#340574", "#AB63FA"]

underweight = df[df['bmi'] < 18.5]['charges'].values
underweight_trace = go.Box(y=underweight, name="Underweight", marker=dict(color=box_colormap[0]))

normal = df[df['bmi'] < 24.9]['charges'].values
normal_trace = go.Box(y=normal, name="Normal", marker=dict(color=box_colormap[1]))

overweight = df[df['bmi'] < 29.9]['charges'].values
overweight_trace = go.Box(y=overweight, name="Overweight", marker=dict(color=box_colormap[2]))

obese = df[df['bmi'] < 34.9]['charges'].values
obese_trace = go.Box(y=obese, name="Obese", marker=dict(color=box_colormap[3]))

extremly_obese = df[df['bmi'] > 34.9]['charges'].values
extremly_obese_trace = go.Box(y=extremly_obese, name="Extremly obese", marker=dict(color=box_colormap[4]))

data = [underweight_trace, normal_trace, overweight_trace, obese_trace, extremly_obese_trace]

figure = go.Figure(data)
figure.update_layout(title="Charges relation by Weight status",
                     xaxis=dict(title="Weight status"),
                     yaxis=dict(title="Charges"),
                     width=900,
                     height=400)

figure.show()
