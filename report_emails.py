import os, datetime
import reports
import emails

date = datetime.datetime.now().strftime('%Y-%m-%d')
path = "supplier-data/descriptions/"

def generate_pdf(path):
  pdf = ""
  files = os.listdir(path)
  for file in files:
    if "txt" in file:
      with open(path+file, 'r') as f:
        lines = f.readlines()
        name = lines[0].strip()
        weight = lines[1].strip()
        pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
  return pdf

if __name__ == "__main__":
  title = "Process Updated on " + current_date 
  #generate the package for pdf body
  package = generate_pdf(path)
  reports.generate_report("/tmp/processed.pdf", title, package)

  #generate email information
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"
  
  #generate email for the online fruit store report and pdf attachment
  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(message)
