import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

data = pd.read_csv('NBA_2004_2023_Shots.csv', usecols=['SEASON_2', 'TEAM_NAME', 'LOC_X', 'LOC_Y'])

st.title('NBA shot charts (most common locations)')

# Select boxes
selected_season = st.selectbox('Select the season:', data['SEASON_2'].unique())
selected_team = st.selectbox('Select the team:', data['TEAM_NAME'].unique())

# Filter data
season_filter = (data['SEASON_2'] == selected_season)
team_filter = (data['TEAM_NAME'] == selected_team)
data_filtered = data[season_filter & team_filter]

if not data_filtered.empty:
    data_filtered['COORDINATE'] = data_filtered['LOC_X'].astype(str) + '_' + data_filtered['LOC_Y'].astype(str)
    data_filtered_locs = data_filtered.groupby(['COORDINATE', 'LOC_X', 'LOC_Y']).agg({'COORDINATE': 'count'})
    data_filtered_locs = data_filtered_locs.rename(columns={'COORDINATE': 'COUNT'})
    data_filtered_locs = data_filtered_locs.reset_index()
    locs_top5k = data_filtered_locs.sort_values(by='COUNT', ascending=False).head(5000)

    fig = plt.figure(figsize=(5, 4.7))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)
    ax.set_xticks([])
    ax.set_yticks([])

    color = "#0b5c5e"

    # Short corner 3PT lines
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
    ax.plot([220, 220], [0, 140], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, lw=2, color=color))
    # Lane and Key
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
    ax.plot([80, 80], [0, 190], linewidth=2, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
    ax.plot([60, 60], [0, 190], linewidth=2, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, lw=2, color=color))
    
    ax.scatter(locs_top5k['LOC_X']*10, locs_top5k['LOC_Y']*10, color='brown', marker='o', s=10, alpha=0.75)

    st.pyplot(fig)
else:
    st.warning('No data found for the selection.')
