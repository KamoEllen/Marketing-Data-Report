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
