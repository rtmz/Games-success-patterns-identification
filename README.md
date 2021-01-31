# Games-success-patterns-identification
Analysis for online store 'Ice' which sells video games all over the world. User and expert reviews, genres, platforms (e.g. Xbox or PlayStation), and historical data on game sales are available from open sources. We need to identify patterns that determine whether a game succeeds or not. This will allow us to spot potential big winners and plan advertising campaigns. We have data going back to 2016. Let’s imagine that it’s December 2016 and we’re planning a campaign for 2017.  The dataset contains the abbreviation ESRB. The Entertainment Software Rating Board evaluates a game's content and assigns an age rating such as Teen or Mature.

# We'll go through the following steps:

- Open the data file and study the general information
- Prepare the data:
  - Replace the column names (make them lowercase).
  - Convert the data to the required types.
  - Describe the columns where the data types have been changed and why.
  - If necessary, decide how to deal with missing values:
  - Calculate the total sales (the sum of sales in all regions) for each game and put these values in a separate column.
  
- Analyze the data

  - Look at how many games were released in different years. Is the data for every period significant?
  - Look at how sales varied from platform to platform. Choose the platforms with the greatest total sales and build a distribution based on data for each year. Find platforms that used to be popular but now have zero sales. How long does it generally take for new platforms to appear and old ones to fade?
  - Determine what period we should take data for. The data should allow us to build a prognosis for 2017.
  - Work only with the data that we've decided is relevant. Disregard the data for previous years.
  - Which platforms are leading in sales? Which ones are growing or shrinking? Select several potentially profitable platforms.
  - Build a box plot for the global sales of all games, broken down by platform. Are the differences in sales significant? What about average sales on various platforms?
  - Take a look at how user and professional reviews affect sales for one popular platform. Build a scatter plot and calculate the correlation between reviews and sales. Draw conclusions.
  - Keeping the conclusions in mind, compare the sales of the same games on other platforms.
  - Take a look at the general distribution of games by genre. What can we say about the most profitable genres? Generalize about genres with high and low sales.
  
- Create a user profile for each region
For each region (NA, EU, JP), determine:

  - The top five platforms. Describe variations in their market shares from region to region.
  - The top five genres. Explain the difference.
  - Do ESRB ratings affect sales in individual regions?
  
- Test the following hypotheses:
  - Average user ratings of the Xbox One and PC platforms are the same.
  - Average user ratings for the Action and Sports genres are different.
  
# Data description
- Name
- Platform
- Year_of_Release
- Genre
- NA_sales (North American sales in USD million)
- EU_sales (sales in Europe in USD million)
- JP_sales (sales in Japan in USD million)
- Other_sales (sales in other countries in USD million)
- Critic_Score (maximum of 100)
- User_Score (maximum of 10)
- Rating (ESRB)

Data for 2016 may be incomplete.
