import email_validation

def main():
    print("=== Welcome to Email Sender ===")
    print("1. Send single email")
    print("2. Send bulk emails from CSV")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        rec_mail = input("Enter the recipient email: ").strip()
        subject = input("Enter the subject: ").strip()
        body = input("Enter the body: ").strip()
        email_validation.send_email(rec_mail, subject, body)

    elif choice == "2":
        csv_file = input("Enter the CSV file path (first column must have emails): ").strip()
        subject = input("Enter the subject: ").strip()
        body = input("Enter the body: ").strip()
        email_validation.send_bulk_emails(csv_file, subject, body)

    else:
        print("Invalid choice. Please run again.")

if __name__ == "__main__":
    main()
