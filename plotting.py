from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df['Start_string']= df['Start'].dt.strftime('%H:%M:%S %y-%m-%d')
df['End_string']= df['End'].dt.strftime('%H:%M:%S %y-%m-%d')



cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime', height=200, width=700, title='Motion graph')
p.yaxis.minor_tick_line_color= None
p.ygrid[0].ticker.desired_num_ticks=1 # to remove horizontal grid from the graph

hover= HoverTool(tooltips=[('Start','@Start_string'),('End','@End_string')]) # 'tooltips' is a parameter that gets argument as tuple , 'start' is the value that will show in the graph, '@start' indicates the column name 'start' and similar to 'End' 

p.add_tools(hover)

q= p.quad(left='Start' ,right='End', top=1 ,bottom=0, color='#33ccc7', source=cds ) # here 'start' and 'end' shouldn't changed as 'p' has 'datetime' x-axis

output_file('Graph.html')
show(p)