Topic: How Companies Exploit Women's Insecurities for Profit
<hr>

Contents:


Cleaning Data

Introduction

Hypothesis

How Advertisements Prey on Women's Insecurities

Exploiting Women's Insecurities to Sell Douche Products

Impact on Women's Body Image and Self-Esteem

Alternative Marketing Strategies

Conclusion

Data Visualization

Sources
<hr>
Cleaning Data:
I broadened my search for data sources and utilized various online sources to collect data for the report. I cleaned and organized the data using Notepad and further processed and formatted it using Python3 with Pandas, NumPy, Matplotlib and Hypothesis testing. Throughout the process, I emphasized the importance of maintaining ethical standards, avoiding bias, and ensuring accuracy and reliability of research, especially when proving companies exploit women's insecurities. 
<hr>
Introduction: 
Industries such as beauty, fashion, weight loss, cosmetic surgery, and fitness use women's insecurities to sell products and make profits by setting unrealistic beauty standards and promoting the idea that women need to conform to societal norms. They perpetuate the notion that there is an ideal body image that women should strive for, which leads to exploiting women's insecurities and profiting from them.As a result, women are often left feeling dissatisfied and continue to strive for unattainable beauty standards, perpetuating a cycle of insecurity and profit for these industries.
<hr>
Hypothesis:

1.How Advertisements Prey on Women's Insecurities

2.Exploiting Women's Insecurities to Sell Douche Products

3.Impact on Women's Body Image and Self-Esteem

4.Alternative Marketing Strategies

<hr>
Hypothesis and Analysis:

How Advertisements Prey on Women's Insecurities:

Advertisements for beauty products, fashion, weight loss, cosmetic surgery, and fitness often use language and images that suggest women need to improve their appearance to be accepted by society or feel confident in themselves.
Language that reinforces insecurities around appearance includes terms like "flawless," "perfect," "ideal," and "thin."
Images often feature unrealistic beauty standards, idealized body types, and airbrushed or photoshopped models.
These industries prey on women's insecurities about their appearance to sell products.
Advertisements and marketing tactics suggest that women need to change their appearance to fit societal standards of beauty and gain acceptance and confidence.
Some tactics include using shame and guilt to make women feel bad about their appearance and creating a sense of urgency to buy products that promise to fix perceived flaws.

Exploiting Women's Insecurities to Sell Douche Products:

Companies often use marketing tactics that suggest women need to change their bodies to fit societal beauty standards and feel more confident.
This creates a sense of urgency to buy products that promise to fix perceived flaws, such as douches that claim to make women feel cleaner or more attractive.
Advertisements may also use shame or guilt to make women feel bad about their bodies and suggest that using their product is the solution.

Impact on Women's Body Image and Self-Esteem:

These industries often promote unrealistic and unhealthy beauty standards that can lead to negative body image and low self-esteem.
The cosmetic surgery industry is particularly adept at preying on women's insecurities. According to recent statistics, 95% of all cosmetic procedures are performed on women. They offer procedures that promise to fix perceived flaws and create a sense of perfection, which can be addictive. Women may feel better after the procedure but often return again and again, trying to achieve an unattainable standard.
The pressure to conform to societal beauty standards can lead to body dissatisfaction, disordered eating, and other mental health issues.
These industries can also perpetuate harmful stereotypes and contribute to discrimination based on appearance.

Alternative Marketing Strategies:

Alternative marketing strategies could focus on promoting diversity and inclusivity in advertising, embracing body positivity and self-acceptance, and celebrating individuality and uniqueness.
Brands could also promote the health benefits of their products rather than solely focusing on appearance-related benefits.
Using real people with diverse body types and appearances in advertisements could also promote positive body image and self-esteem.
However, societal beauty standards have been deeply ingrained, making it difficult to shift consumer attitudes and behaviors overnight.
<hr>

Conclusion:

The advertising and marketing strategies used by industries such as beauty, fashion, weight loss, cosmetic surgery, and fitness exploit women's insecurities for profit, perpetuate harmful stereotypes, and contribute to negative body image and low self-esteem. Alternative marketing strategies that promote diversity, inclusivity, and self-acceptance could help promote positive body image and self-esteem, but changing consumer attitudes and behaviors requires a shift away from deeply ingrained societal beauty standards.
<hr>

<hr>
The graph illustrates that the weight loss industry is worth billions of dollars in five different countries, indicating that companies are profiting from women's insecurities. A significant percentage of women in each country report feeling insecure about their bodies, suggesting a large potential market for these products. The data sources for the graph are various surveys conducted by organizations and media outlets in each country.
<div style="display: flex;">
    <div style="flex-basis: 80%;">
        <img src="https://raw.githubusercontent.com/KamoEllen/Marketing-Data-Report/main/Increase%20in%20Risk%20Associated%20with%20Douching.png" alt="Increase in Risk Associated with Douching" width="400"/>
    </div>
    <div style="flex-basis: 30%;">
        <pre><code>
import matplotlib.pyplot as plt
import numpy as np
health_effects = ['Ectopic Pregnancy', 'Chlamydia', 'Gonorrhea', 'Cervical Cancer', 'Irregular Periods', 'Low Birth Weight', 'Preterm Birth', 'Difficulty Getting Pregnant']
risk_percentages = [76, 30, 20, 44, 25, 30, 25, 12]
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(health_effects, risk_percentages)
ax.set_title('Negative Health Effects Associated with Douching: Risks and Percentages')
ax.set_xlabel('Health Effects')
ax.set_ylabel('Percentage Increase in Risk Associated with Douching')
for i, v in enumerate(risk_percentages):
    ax.text(i, v+1, str(v)+'%', ha='center')
plt.show()
        </code></pre>
    </div>
</div>

<hr>
Douching is associated with several negative health effects, as indicated by the percentage increase in risk associated with each health effect. The U.S. Department of Health & Human Services and a study published in the National Library of Medicine both provide information on the risks associated with douching. A bar chart is used to clearly display the risks and percentages for each health effect, emphasizing the importance of avoiding douching for good reproductive and overall health.
<div style="display: flex;">
    <div style="flex-basis: 50%;">
        <img src="https://raw.githubusercontent.com/KamoEllen/Marketing-Data-Report/main/Cosmetic_Procedures_trend.png" alt="Cosmetic Procedures Trend" width="400"/>
    </div>
    <div style="flex-basis: 50%;">
        <pre><code>
import matplotlib.pyplot as plt
countries = ['United States', 'United Kingdom', 'Canada', 'Australia', 'Japan']
industry_worth = [72, 2, 7, 1.8, 4.5]
percent_women = [62, 50, 69, 75, 27.4]
plt.plot(countries, industry_worth, label='Industry Worth ($ billions)')
plt.plot(countries, percent_women, label='% of Women Feeling Insecure')
plt.xlabel('Country')
plt.ylabel('Amount')
plt.title('Purchasing Power of Products Exploiting Women Insecurities')
plt.legend()
plt.show()
        </code></pre>
    </div>
</div>
<hr>
The number of cosmetic surgeries continues to rise because the beauty industry promotes cosmetic procedures and unrealistic beauty standards, which contribute to women feeling more insecure about their bodies. This results in an increasing demand for cosmetic surgeries, leading to the industry profiting from it. Despite the lack of significant improvements in body satisfaction rates, the impact of advertising and societal pressure on women's body image remains strong.
<div style="display: flex;">
    <div style="flex-basis: 50%;">
        <img src="https://raw.githubusercontent.com/KamoEllen/Marketing-Data-Report/main/Top_Surgical_Procedures.png" alt="Top Surgical Procedures" width="400"/>
    </div>
    <div style="flex-basis: 50%;">
        <pre><code>
import matplotlib.pyplot as plt
years = [2000, 2019]
cosmetic_procedures = [7.4, 18.4]
body_image_dissatisfaction = [23, 32]
plt.plot(years, cosmetic_procedures, label='Cosmetic Procedures')
plt.plot(years, body_image_dissatisfaction, label='Body Image Dissatisfaction')
plt.xlabel('Year')
plt.ylabel('Number/Percentage')
plt.title('Cosmetic Procedures and Body Image Dissatisfaction over Time')
plt.legend()
plt.show()
        </code></pre>
    </div>
</div>
<hr>
The popularity of these procedures and indicates that the demand for cosmetic surgery continues to rise, emphasizing the influence of societal beauty standards and the desire for physical perfection.(The American Society of Plastic Surgeons (ASPS) reveals 2020 Annual Plastic Surgery Statistics Report)
<div style="display: flex;">
    <div style="flex-basis: 50%;">
        <img src="https://raw.githubusercontent.com/KamoEllen/Marketing-Data-Report/main/body_confidence_decline.png" alt="Body Confidence Decline" width="400"/>
    </div>
    <div style="flex-basis: 50%;">
        <pre><code>
        import matplotlib.pyplot as plt

        procedures = ['Nose Reshaping', 'Eyelid Surgery', 'Facelift', 'Liposuction', 'Breast Augmentation']
        counts = [352555, 325112, 234374, 211067, 193073]

        plt.bar(procedures, counts, color='purple')
        plt.title('2020 Top 5 Cosmetic Surgical Procedures')
        plt.ylabel('Procedure Count')
        plt.xlabel('Procedure')

        plt.show()
        </code></pre>
    </div>
</div>
<hr>
Nine out of 10 women say they will actually not eat and risk putting their health at stake when they feel bad about their body image (Dove Global Beauty and Confidence Report)
<div style="display: flex;">
    <div style="flex-basis: 50%;">
        <img src="https://github.com/KamoEllen/Marketing-Data-Report/blob/main/health_risk.png" alt="Health Risk" width="400">
    </div>
    <div style="flex-basis: 50%;">
        <pre><code>
import matplotlib.pyplot as plt
yes_percentage = 90
no_percentage = 10
labels = ['Yes, I have done this', 'No, I have not done this']
colors = ['blue', 'red']
plt.pie([yes_percentage, no_percentage], labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Women at Risk of Health Due to Body Image')
plt.show()
        </code></pre>
    </div>
</div>
<hr>

Approximately 7 in 10 women and girls report a decline in body confidence and increase in beauty and appearance anxiety, which they say is driven by the pressure for perfection from media and advertising’s unrealistic standard of beauty (Dove Global Beauty and Confidence Report).)  
<div style="display: flex;">
    <div style="flex-basis: 50%;">
        <img src="https://raw.githubusercontent.com/KamoEllen/Marketing-Data-Report/main/purchase_power.png" alt="Purchase Power" width="400"/>
    </div>
    <div style="flex-basis: 50%;">
        <pre><code>
        import matplotlib.pyplot as plt   
    yes_percentage = 70
    no_percentage = 30
    labels = ['Reported Decline', 'No Decline']
    colors = ['red', 'blue']
    plt.pie([yes_percentage, no_percentage], labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title('Women and Girls Reporting a Decline \n in Body Confidence and Increase in Appearance Anxiety')
    plt.show()
    </code></pre>
</div>
</div>

<hr>

Sources:

Dove Global Beauty and Confidence Report
The American Society of Plastic Surgeons (ASPS) 2020 Annual Plastic Surgery Statistics Report
U.S. Department of Health & Human Services (https://www.womenshealth.gov/a-z-topics/douching)
American Society of Plastic Surgeons (ASPS) for total number of cosmetic procedures performed in the United States (https://www.plasticsurgery.org/news/press-releases/new-statistics-reveal-the-shape-of-plastic-surgery)
University of Central Florida survey on college students' body dissatisfaction (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3447047/)
Aesthetic Surgery Journal study on positive correlation between body dissatisfaction and likelihood of seeking cosmetic surgery (https://academic.oup.com/asj/article/29/4/345/191362)
National Eating Disorders Association (NEDA) and MarketResearch.com for the United States survey
Mental Health Foundation and The Guardian for the United Kingdom survey
Flare Magazine and CBC News for the Canada survey
Butterfly Foundation and SBS News for the Australia survey
Ministry of Health, Labour, and Welfare and Japan Today for the Japan survey
