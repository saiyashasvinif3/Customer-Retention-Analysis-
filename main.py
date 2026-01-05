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
        plt.bar(churn_count.index,churn_count.values)
        plt.xlabel('Churn')
        plt.ylabel('Count')
        plt.title('Churn Distribution')
        plt.xticks([0,1])
        plt.bar_label(plt.gca().containers[0])
        plt.savefig("churn_distribution.png")
        plt.show()
        
        #Box plot for monthly charges
        plt.figure(figsize=(6,4))
        plt.boxplot(self.df['MonthlyCharges'])
        plt.ylabel('Monthly Charges')
        plt.savefig("monthly_charges_boxplot.png")
        plt.show()
        
        #Histogram for tenure 
        plt.figure(figsize=(6,4))
        plt.hist(self.df['tenure'], bins=30, edgecolor='k')
        plt.xlabel('Tenure (months)')
        plt.ylabel('Number of Customers')
        plt.title('Distribution of Customer Tenure')
        plt.savefig("tenure_distribution.png")
        plt.show()

        #Scatter plot for monthly charges vs total charges
        plt.figure(figsize=(6,4))
        plt.scatter(self.df['MonthlyCharges'], self.df['TotalCharges'], alpha=0.5)
        plt.xlabel('Monthly Charges')
        plt.ylabel('Total Charges')
        plt.title('Monthly Charges vs Total Charges')
        plt.savefig("monthly_vs_total_charges.png")
        plt.show()

        #Piechart for knowing which internet service is observed more
        plt.figure(figsize=(6,4))
        plt.pie(self.df['InternetService'].value_counts(), labels=self.df['InternetService'].value_counts().index, autopct='%1.1f%%')
        plt.title('Internet Service Distribution')
        plt.savefig("internet_service_distribution.png")
        plt.show()
        
        #Heatmap for visualizing correlation between all the numerical columns
        plt.figure(figsize=(6,4))
        numeric_df = self.df.select_dtypes(include=['int64', 'float64'])
        sns.heatmap(numeric_df.corr(method='pearson'), annot=True, fmt=".2f", cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.savefig("correlation_heatmap.png")
        plt.show()

        #countplot to visualizing which gender causes more churn
        plt.figure(figsize=(6,4))
        sns.countplot(x=self.df['gender'], hue=self.df['Churn'])
        plt.title("Gender Distribution by churn")
        plt.savefig("gender_churn_distribution.png")
        plt.show()

        #countplot to whethere senior citizen cause more churn
        plt.figure(figsize=(6,4))
        sns.countplot(x=self.df['SeniorCitizen'], hue=self.df['Churn'])
        plt.title("Senior Citizen Distribution by churn")
        plt.savefig("senior_citizen_churn_distribution.png")
        plt.show()

        # Countplot to visualize which internet service causes more churn
        plt.figure(figsize=(7,5))
        sns.countplot(x='InternetService', hue='Churn', data=self.df)
        plt.title("Internet Service vs Churn")
        plt.xlabel("Internet Service")
        plt.ylabel("Number of Customers")
        plt.savefig("internet_service_churn_distribution.png")
        plt.show()

if __name__ == "__main__":
    data = "WA_Fn-UseC_-Telco-Customer-Churn.csv"
    obj =  CUSTOMER_RETENTION(data)

    



