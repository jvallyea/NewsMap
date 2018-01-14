# NewsMap
Hi there! NewsMap was borne out of HackMIT 2017. Zixuan, David and I realized that the way we perceive news and the world around us is largely shaped by our friends and family, geography, and interests. We saw this as potentially contributing to bias in our scrutiny of everything from foreign governments to financial markets. What if we had a way to visualize the world's news through a map? What if we could translate news articles published in over 65 languages  and analyze them using algorithms, rather than our minds? Now, with the advent of NewsMap, this is possible.
# Preview 
![alt text](https://www.vallyeason.com/Projects/NewsMap/Images/slide1.JPG)
With NewsMap, we can map the locations mentioned in news articles across the world mentioning a specific topic - in this case, **water risk**. 
![alt text](https://www.vallyeason.com/Projects/NewsMap/Images/slide2.JPG)
With NewsMap, we can perform analyses on the correlation between news articles and a company's economic performance. Here, we see differently colored nodes representing **sentiment analysis toward and article's tone**. On the sidebar, time-dependent functionality is added, allowing for visualizations of **company stock performance** over time to be correlated with news tone.
# Engineering
NewsMap was built using Python - the Flask library was used to integrate the front-end into the platform. Data was extracted from the GDELT database (sponsored through Google Jigsaw). Following data extraction from the GDELT GKG (Global Knowledge Graph) database, coordinates and sentiment analysis was conducted to extract the tone - this underlying data was visualized using Carto and the MapBox API. 
<br/> <br/>
Stock data presented along the sidebar is extracted from the NASDAQ API; several static examples use downloaded CSV files to display the data. Companies can be searched using the search bar at the top. However, the search bar has a limited time functionality of 2-24 hours prior to the search due to data and rate-limiting constraints. 
# Future Steps
We are beginning to look into using machine learning to study the data and make predictions and performance analytics for risk factors and regions for growth. We hope to one day provde NewsMap as a tool to help companies, governments, and the active hobbyist study the news using a quantitative, data-driven approach.
# Website
**Hackathon Demo Website**: http://newsmap2017.herokuapp.com
<br/>
**Personal Project Portfolio**: http://www.vallyeason.com/Projects/NewsMap
<br/>
We hope to have our initial beta launch of NewsMap early in the spring of 2018. Stay tuned for details!
