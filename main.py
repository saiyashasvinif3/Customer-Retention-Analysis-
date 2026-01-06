import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class CUSTOMER_RETENTION:
    def __init__(self, file_path):
        self.file_path = file_path 
        self.df = pd.read_csv(self.file_path)
        print(self.df.shape)
        print(self.df.isnull().sum())
        self.df.drop(columns=['customerID'], inplace=True)
        self.df['TotalCharges'] = pd.to_numeric(self.df['TotalCharges'], errors='coerce')
        print(self.df['TotalCharges'].dtype)
        print(self.df.info())
       # Bar chart visualiation for churn count
        self.df['Churn']= self.df['Churn'].map({'Yes':1, 'No': 0})
        churn_count = self.df['Churn'].value_counts().sort_index()
        plt.figure(figsize=(6,4))
        plt.bar(churn_count.index,churn_count.values, color=['blue','orange'])
        plt.xlabel('Churn')
        plt.ylabel('Count')
        plt.title('Churn Distribution')
        plt.xticks([0,1])
        plt.bar_label(plt.gca().containers[0])
        plt.savefig("churn_distribution.png")
        plt.show()
        # Countplot to visualize senior citizen churn distribution
        plt.figure(figsize=(6,4))
        ax = sns.countplot( x=self.df['SeniorCitizen'], hue=self.df['Churn'])
        plt.title("Citizens Distribution by Churn")
        plt.xlabel("Senior Citizen")
        plt.ylabel("Count")
        for container in ax.containers:
           ax.bar_label(container, label_type='edge')
        plt.xticks([0, 1], ['Non-Senior Citizen', 'Senior Citizen'])
        plt.savefig("senior_citizen_churn_distribution.png")
        plt.show()
        #barplot for gender churn analysis
        churned = self.df[self.df['Churn'] == 1]
        gender_counts = churned['gender'].value_counts() 
        plt.figure(figsize=(6,4))
        plt.bar(gender_counts.index, gender_counts.values, color=['skyblue', 'salmon']) # individual colors)
        plt.title("Churned Customers by Gender")
        plt.xlabel("Gender")
        plt.ylabel("Number of Churned Customers")
        plt.bar_label(plt.gca().containers[0])
        plt.savefig("gender_chruned_customers.png")
        plt.show()
       
       # Filter churned senior citizens
        senior_churned = self.df[(self.df['SeniorCitizen'] == 1) & (self.df['Churn'] == 1)]
        gender_counts = senior_churned['gender'].value_counts()
        plt.figure(figsize=(6,4))
        plt.bar(gender_counts.index,gender_counts.values,color=['skyblue', 'salmon'])
        plt.title("Churned Senior Citizens by Gender")
        plt.xlabel("Gender")
        plt.ylabel("Number of Churned Senior Citizens")
        plt.bar_label(plt.gca().containers[0])
        plt.savefig("churned_senior_gender.png")
        plt.show()

        #barplot to visualize sim usage by gender among senior citizens
        senior_df = self.df[self.df['SeniorCitizen'] == 1]
        sim_counts = senior_df.groupby(['gender', 'sim']).size().reset_index(name='count')
        plt.figure(figsize=(10,6))
        sns.barplot(data=sim_counts, x='sim', y='count', hue='gender', palette='Set2')
        plt.title("SIM Usage by Gender in Senior Citizens")
        plt.xlabel("SIM Provider")
        plt.ylabel("Number of Users")
        for container in plt.gca().containers:
            plt.bar_label(container)
        plt.savefig("senior_citizen_sim_usage.png")    
        plt.show()

        #Piechart for knowing which internet service is observed more
        plt.figure(figsize=(6,4))
        plt.pie(self.df['InternetService'].value_counts(), labels=self.df['InternetService'].value_counts().index, autopct='%1.1f%%')
        plt.title('Internet Service Distribution')
        plt.savefig("internet_service_distribution.png")
        plt.show()
        
        plt.figure(figsize=(6,4))
        plt.pie(self.df['sim'].value_counts(), labels=self.df['sim'].value_counts().index, autopct='%1.1f%%')
        plt.title('SIM Distribution')
        plt.savefig("sim_distribution.png")
        plt.show()
        
        plt.figure(figsize=(6,4))
        plt.pie(self.df['Contract'].value_counts(), labels=self.df['Contract'].value_counts().index, autopct='%1.1f%%')
        plt.title('Contract Distribution')
        plt.savefig("contract_distribution.png")
        plt.show()
      
        internetcounts = self.df.groupby(['InternetService', 'Churn']).size().reset_index(name='count')
        plt.figure(figsize=(10,6))
        ax = sns.barplot(data=internetcounts, x='InternetService', y='count', hue='Churn', palette='Set2')
        plt.title("Internet Service vs Churn Distribution")
        plt.xlabel("Internet Service Provider")
        plt.ylabel("Number of Users")
        for container in ax.containers:
            ax.bar_label(container)
        plt.savefig("internetservice_churn_distribution.png")
        plt.show()

        contractcounts = self.df.groupby(['Contract', 'Churn']).size().reset_index(name='count')
        plt.figure(figsize=(10,6))
        ax = sns.barplot(data=contractcounts, x='Contract', y='count', hue='Churn', palette='Set2')
        plt.title("Contract vs Churn Distribution")
        plt.xlabel("Contract Type")
        plt.ylabel("Number of Users")
        for container in ax.containers:
            ax.bar_label(container)
        plt.savefig("contract_churn_distribution.png")
        plt.show()

        simcounts = self.df.groupby(['sim', 'Churn']).size().reset_index(name='count')
        plt.figure(figsize=(10,6))
        ax = sns.barplot(data=simcounts, x='sim', y='count', hue='Churn', palette='Set2')
        plt.title("SIM vs Churn Distribution")
        plt.xlabel("SIM Provider")
        plt.ylabel("Number of Users")
        for container in ax.containers:
            ax.bar_label(container)
        plt.savefig("sim_churn_distribution.png")
        plt.show()

     

# Count of customers for each tenure value
        tenurecounts = self.df['tenure'].value_counts().sort_index()
        plt.figure(figsize=(10,6))
        plt.plot(tenurecounts.index, tenurecounts.values, marker='o', color='blue', linewidth=2)
# Add labels and title
        plt.xlabel("Tenure (Months)")
        plt.ylabel("Number of Customers")
        for container in ax.containers:
            ax.bar_label(container)
        plt.title("Customer Distribution by Tenure")
        plt.grid(True)
        plt.savefig("tenure_line_chart.png")
        plt.show()

        plt.figure(figsize=(6,4))
        techcounts = self.df.groupby(['TechSupport', 'Churn']).size().unstack()
        ax=techcounts.plot(kind='bar', figsize=(8,5), color=['skyblue','salmon'])
        plt.xlabel("Tech Support Subscription")
        plt.ylabel("Number of Customers")
        for container in ax.containers:
            ax.bar_label(container)
        plt.title("Influence of Tech Support on Churn")
        plt.xticks(rotation=0) 
        plt.legend(title='Churn')
        plt.savefig("techsupport_churn_distribution_simple.png")
        plt.show()
       

        plt.figure(figsize=(6,4))
        tech_counts = self.df.groupby(['TechSupport', 'sim']).size().unstack()
        ax=tech_counts.plot(kind='bar', figsize=(8,5), color=['skyblue','salmon','lightgreen'])
        plt.xlabel("Tech Support Subscription")
        plt.ylabel("Number of Customers")
        for container in ax.containers:
            ax.bar_label(container)
        plt.title("Influence of Tech Support on SIM ")
        plt.xticks(rotation=0) 
        plt.legend(title='SIM')
        plt.savefig("techsupport_sim_distribution.png")
        plt.show()
       
        monthlycharge = self.df.groupby('Churn')['MonthlyCharges'].mean()
        plt.figure(figsize=(6,4))
        plt.plot(monthlycharge.index, monthlycharge.values, marker='o')
        plt.xlabel('Churn (0 = No, 1 = Yes)')
        plt.ylabel('Average Monthly Charges')
        plt.title('Impact of Monthly Charges on Churn')
        plt.grid(True)
        plt.savefig("monthly_charges_vs_churn.png")
        plt.show()
        
        tenurecount = self.df['tenure'].value_counts().sort_index()
        plt.figure(figsize=(7,4))
        plt.fill_between(tenurecount.index, tenurecount.values, alpha=0.6)
        plt.xlabel('Tenure (Months)')
        plt.ylabel('Number of Customers')
        plt.title('Customer Distribution by Tenure')
        plt.savefig("tenure_area_chart.png")
        plt.show()

if __name__ == "__main__":
    data = "Telco_Churn.csv"
    obj =  CUSTOMER_RETENTION(data)

    





    





    




    



