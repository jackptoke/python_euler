from die import Die
from plotly.graph_objs import Bar, Layout 
from plotly import offline

#Create a D6
# die = Die()
die_1 = Die()
die_2 = Die()

#make some rolls and store the result in the list
results = []

for roll_num in range(1000):
    # result = die.roll()
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualise the result
x_values = list(range(1, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Results'}

my_layout = Layout(title='Results of Rolling 2 D6 Dice 1000 Times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
# print(frequencies)