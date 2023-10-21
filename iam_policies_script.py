import csv
import boto3

def list_iam_policies():
    # Initialize the IAM client
    iam = boto3.client('iam')
    
    # List IAM policies using the 'list_policies' method
    response = iam.list_policies()
    
    # Extract the policies from the response
    policies = response['Policies']
    return policies

def write_policies_to_csv(policies, csv_filename):
    # Open the CSV file for writing
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Policy Name', 'PolicyId', 'Arn']
        
        # Create a CSV writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header row to the CSV file
        writer.writeheader()
        
        # Iterate through the IAM policies and write them to the CSV
        for policy in policies:
            writer.writerow({
                'Policy Name': policy['PolicyName'],
                'PolicyId': policy['PolicyId'],
                'Arn': policy['Arn']
            })

if __name__ == "__main__":
    # Call the list_iam_policies function to retrieve IAM policies
    policies = list_iam_policies()
    
    # Call the write_policies_to_csv function to write policies to a CSV file
    write_policies_to_csv(policies, 'iam_policies.csv')
