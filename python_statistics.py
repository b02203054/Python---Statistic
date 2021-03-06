
#Mean and median

# Subset for Belgium and USA only
be_and_usa = food_consumption[(food_consumption['country'] == "Belgium") | (food_consumption['country'] == 'USA')]

#Just mean 
be_consumption.mean()

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby('country')['consumption'].agg([np.mean, np.median]))

# Measure of spread

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], [0, 0.25, 0.5, 0.75, 1]))

# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 11)))
''' starting number, a stopping number, and a number of intervals '''

# variance and sd
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

# outliers
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)

# Probability

# Sampling

np.random.seed(24) # Set random seed
sample_without_replacement = amir_deals.sample(5) # Sample 5 deals without replacement
sample_with_replacement = amir_deals.sample(5, replace=True) # Sample 5 deals with replacement

# Discrete distributions

size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0] # Create probability distribution

size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob'] # Reset index and rename columns

expected_value = np.sum(size_dist['group_size'] * size_dist['prob']) # Expected value

groups_4_or_more = size_dist[size_dist['group_size'] >= 4] # Subset groups of size 4 or more
prob_4_or_more = np.sum(groups_4_or_more['prob']) # Sum the probabilities of groups_4_or_more

# Continous distributions
prob_between_10_and_20 = uniform.cdf(20, min_time, max_time) -uniform.cdf(10, min_time, max_time) # Calculate probability of waiting 10-20 mins


wait_times = uniform.rvs(0, 30, size=1000) # Generate 1000 wait times between 0 and 30 mins
