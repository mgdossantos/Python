from pandas import *
import numpy

#################
# Syntax Reminder:
#
# The following code would create a two-column pandas DataFrame
# named df with columns labeled 'name' and 'age':
#
# people = ['Sarah', 'Mike', 'Chrisna']
# ages  =  [28, 32, 25]
# df = DataFrame({'name' : Series(people),
#                 'age'  : Series(ages)})

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
         'Netherlands', 'Germany', 'Switzerland', 'Belarus',
         'Austria', 'France', 'Poland', 'China', 'Korea', 
         'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
         'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
         'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
olympic_medal_counts_df = DataFrame({'country_name': countries,
	'gold': gold,
	'silver': silver,
	'bronze': bronze}) 

avg_medal_count= olympic_medal_counts_df[['gold','silver','bronze']].apply(numpy.mean)

medal_counts=olympic_medal_counts_df[['gold','silver','bronze']]
points=numpy.dot(medal_counts,[4,2,1])
olympic_points={'country name':Series(countries),'points':Series(points)}
olympic_points_df=DataFrame(olympic_points)

print(olympic_medal_counts_df)
print(avg_medal_count)
print(olympic_points_df)
