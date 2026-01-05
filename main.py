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
        print(self.df['TotalCharges'].dtype)
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
        plt.show()
        plt.savefig("churn_distribution.png")
        
       #Box plot for monthly charges
        plt.figure(figsize=(6,4))
        plt.boxplot(self.df['MonthlyCharges'])
        plt.ylabel('Monthly Charges')
        plt.show()
        plt.savefig("monthly_charges_boxplot.png")
      #Histogram for tenture 
        plt.figure(figsize=(6,4))
        plt.hist(self.df['tenure'], bins=30, edgecolor='k')
        plt.xlabel('Tenure (months)')
        plt.ylabel('Number of Customers')
        plt.title('Distribution of Customer Tenure')
        plt.show()
        plt.savefig("tenure_distribution.png")

        #Scatter plot for monthly charges vs total charges
        plt.figure(figsize=(6,4))
        plt.scatter(self.df['MonthlyCharges'], self.df['TotalCharges'], alpha=0.5)
        plt.xlabel('Monthly Charges')
        plt.ylabel('Total Charges')
        plt.title('Monthly Charges vs Total Charges')
        plt.show()
        plt.savefig("monthly_vs_total_charges.png")

        #Piechart for knowing which internet service is observed more
        plt.figure(figsize=(6,4))
        plt.pie(self.df['InternetService'].value_counts(), labels=self.df['InternetService'].value_counts().index, autopct='%1.1f%%')
        plt.title('Internet Service Distribution')
        plt.show()
        plt.savefig("internet_service_distribution.png")
        
        #Heatmap for visualizing correlation between all the numerical columns
        plt.figure(figsize=(6,4))
        numeric_df = self.df.select_dtypes(include=['int64', 'float64'])
        sns.heatmap(numeric_df.corr(method='pearson'), annot=True, fmt=".2f", cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.show()
        plt.savefig("correlation_heatmap.png")

        #countplot to visualizing which gender causes more churn
        plt.figure(figsize=(6,4))
        sns.countplot(x=self.df['gender'], hue=self.df['Churn'])
        plt.title("Gender Distribution by churn")
        plt.show()
        plt.savefig("gender_churn_distribution.png")

        #countplot to whethere senior citien cause more churn
        plt.figure(figsize=(6,4))
        sns.countplot(x=self.df['SeniorCitizen'], hue=self.df['Churn'])
        plt.title("Senior Citizen Distribution by churn")
        plt.show()
        plt.savefig("senior_citizen_churn_distribution.png")

        # Countplot to visualize which internet service causes more churn
        plt.figure(figsize=(7,5))
        sns.countplot(x='InternetService', hue='Churn', data=self.df)
        plt.title("Internet Service vs Churn")
        plt.xlabel("Internet Service")
        plt.ylabel("Number of Customers")
        plt.show()
        plt.savefig("internet_service_churn_distribution.png")

if __name__ == "__main__":
    data = "WA_Fn-UseC_-Telco-Customer-Churn.csv"
    obj =  CUSTOMER_RETENTION(data)

    
