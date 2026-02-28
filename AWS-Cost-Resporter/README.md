# EC2 Static Cost Report Generator

This project is a Python script that fetches EC2 instances from AWS and generates a CSV report with estimated monthly costs using predefined static pricing.

The script connects to AWS using Boto3, retrieves instance details (ID, type, state, launch time), calculates estimated cost based on hourly rates defined in the code, and exports the results to a CSV file.

---

## 🔮 Future Updates

- Replace static pricing with AWS Cost Explorer API for real billing data  
- Add CLI arguments (e.g., `--days`, `--output`)  
- Improve cost accuracy and filtering options  
- Enhance logging and error handling  
