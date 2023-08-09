import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading dataset and cleanning the data
df = pd.read_csv('D:/New folder/pyhton/dataset/owid-co2-data.csv')
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
#print data head
print(df.head())

# Computing summary statistics
co2_mean = np.mean(df['co2'])
gdp_median = np.median(df['gdp'])
correlation = df['co2'].corr(df['gdp'])

# Set up GridSpec for dashboard visualisation
fig = plt.figure(figsize=(16, 8))
gs = fig.add_gridspec(3, 6)

# Title to the figure
fig.suptitle('Climate Change and Its Effect on CO2 Emissions and Energy Consumption', fontsize=20, fontweight='bold')

# text box to explain the purpose of the visualizations
text_box = '''
This dashboard visualizes the relationship between climate change, 
CO2 emissions, and energy consumption. 
-The first plot shows the distribution of CO2 emissions and its mean value. 
-The second plot displays the relationship between GDP and CO2 emissions. 
-The third plot lists the top 10 CO2 emitters by country. 
-The fourth, fifth, and sixth plots show the trend of CO2 emissions 
from coal, oil, and gas consumption over time, respectively.
'''

fig.text(.83, 0.1, text_box, ha='center',fontsize=9.5) 

# Plot One: Distribution of CO2 Emissions
ax1 = fig.add_subplot(gs[0, :2])
sns.histplot(data=df, x='co2', bins=20, ax=ax1)
ax1.axvline(x=co2_mean, color='red', linestyle='--')
ax1.set_xlabel('CO2 Emissions')
ax1.set_ylabel('Frequency')
ax1.set_title('Distribution of CO2 Emissions')

# Plot Two: Relationship between GDP and CO2 emissions
ax2 = fig.add_subplot(gs[0, 2:])
sns.scatterplot(data=df, x='gdp', y='co2', ax=ax2)
ax2.annotate(text=f"Correlation: {correlation:.2f}", xy=(0.1, 0.9), xycoords='axes fraction', fontsize=14)
ax2.set_xlabel('GDP')
ax2.set_ylabel('CO2 Emissions')
ax2.set_title('Relationship between GDP and CO2 Emissions')

# Plot Three: Top CO2 emitters by country
ax3 = fig.add_subplot(gs[1, :2])
top_emitters = df.groupby('iso_code').agg({'co2_per_capita':'mean'}).sort_values(by='co2_per_capita', ascending=False).head(10)
sns.barplot(data=top_emitters, x=top_emitters.index, y='co2_per_capita', ax=ax3)
ax3.set_xlabel('Country')
ax3.set_ylabel('CO2 emissions per capita')
ax3.set_title('Top CO2 Emitters by Country')
ax3.tick_params(axis='x', labelrotation=45)

# Plot Four: CO2 emissions from coal consumption over time
ax4 = fig.add_subplot(gs[1, 2:4])
sns.lineplot(data=df, x='year', y='coal_co2_per_capita', ax=ax4, color='orange')
ax4.set_xlabel('Year')
ax4.set_ylabel('Coal CO2 emissions per capita')
ax4.set_title('Climate Change and its Effect on Coal CO2 Emissions')

# Plot Five: CO2 emissions from oil consumption over time
ax5 = fig.add_subplot(gs[1, 4:])
sns.lineplot(data=df, x='year', y='oil_co2_per_capita', ax=ax5, color='green')
ax5.set_xlabel('Year')
ax5.set_ylabel('Oil CO2 emissions per capita')
ax5.set_title('Climate Change and its Effect on Oil CO2 Emissions')

# Plot Six: CO2 emissions from gas consumption over time
ax6 = fig.add_subplot(gs[2, 1:4])
sns.lineplot(data=df, x='year', y='gas_co2_per_capita', ax=ax6, color='purple')
ax6.set_xlabel('Year')
ax6.set_ylabel('Gas CO2 emissions per capita')
ax6.set_title('Climate Change and its Effect on Gas CO2 Emissions')

# Adjust legend and layout
fig.tight_layout()
plt.subplots_adjust(top=0.9)

# Saving in png and show the figure
plt.savefig('dashboard_infographics.png', dpi=300)
plt.show()