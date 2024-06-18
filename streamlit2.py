import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.header('Business IT2 | Python 2')
st.title('StudentsPerformance')


data = pd.read_csv('/Users/tuankiet/Downloads/StudentsPerformance.csv')
data['math score'] = data['math score'].round(0)
data['reading score'] = data['reading score'].round(0)


data['text'] = 'Group: ' + data['race/ethnicity'] + '<br>Math score: ' + data['math score'].astype(str) + '<br>Reading score: ' + data['reading score'].astype(str)


ethnicity_colors = {
    'group A': 'blue',
    'group B': 'red',
    'group C': 'green',
    'group D': 'purple',
    'group E': 'orange'
}


st.sidebar.header('User Input Features')
selected_groups = st.sidebar.multiselect(
    'Select Groups to Display',
    options=data['race/ethnicity'].unique(),
    default=data['race/ethnicity'].unique()
)

# Filter data based on user input
filtered_data = data[data['race/ethnicity'].isin(selected_groups)]

# Create the Plotly figure
fig = go.Figure()

for ethnicity, color in ethnicity_colors.items():
    if ethnicity in selected_groups:
        group_data = filtered_data[filtered_data['race/ethnicity'] == ethnicity]
        fig.add_trace(go.Scatter(
            x=group_data['math score'],
            y=group_data['reading score'],
            mode='markers',
            marker=dict(
                size=50,
                color=color,
                opacity=0.6,
                sizemode='area',
                sizeref=2.*max(group_data['math score'])/(40.**2),
                sizemin=4
            ),
            text=group_data['text'],
            hoverinfo='text',
            name=ethnicity
        ))

fig.update_layout(
    title='Achievement Gap between Groups',
    xaxis_title='Math Score',
    yaxis_title='Reading Score',
    legend_title='Race Ethnicity',
    plot_bgcolor='#E6DECE',
    paper_bgcolor='#E6DECE',
    font=dict(
        size=20
    )
)

# Display the Plotly figure in Streamlit
st.plotly_chart(fig)
