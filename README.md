Gas Utility services Backend framework 


App Localhost URL: http://127.0.0.1:8000/

Admin Panel URL: http://localhost:8000/admin/


Login Details for Admin Panel:

URL: http://localhost:8000/admin/

Username: bynry 

Password: bynry123


Powershell Command to start server:

python manage.py runserver 


--POST cURL Commands:


1) Submit Customer Service Request
   
curl.exe -X POST "http://localhost:8000/api/service-requests/" `

  -H "Content-Type: multipart/form-data" `
  
  -F "name=Aryan Jambhale" `
  
  -F "phone=1234567890" `
  
  -F "address=Pune" `
  
  -F "request_type=leak" `
  
  -F "description=Urgent gas leak"
  

  Eg Output:
  
  {"request_id":7,"customer_id":4,"message":"Service request created. Use customer_id to upload files."}
  

2) File Upload:
   
curl.exe -X POST "http://localhost:8000/api/service-requests/upload/" `

  -H "Content-Type: multipart/form-data" `
  
  -F "attachment=@C:\Users\aryan\Downloads\22BCE3797_DA4_Software.pdf" ` (Replace with your file path)
  
  -F "customer=4"  (Replace with your customer id)
  

Eg Output:

{"request_id":7,"attachment_url":"/media/attachments/22BCE3797_DA4_Software_g8toDSU.pdf"}



--GET cURL Commands:


1) View Account Info:
   
curl.exe "http://localhost:8000/api/account/?customer_id=4" (Replace with your customer_id)


Eg Output:

{"name": "Aryan Jambhale", "email": "", "phone": "1234567899", "address": "Pune", "active_requests": 1}


2) Get Request Status:
   
curl.exe "http://localhost:8000/api/service-requests/4/" (Replace with your customer_id)


Eg Output:

[{

"id":4,

"attachment":"http://localhost:8000/media/attachments/22BCE3797_DA4_Software.pdf",

"request_type":"leak",

"description":"Urgent Gas Leak",

"status":"pending",

"created_at":"2025-03-27T17:15:20.293215Z",

"updated_at":"2025-03-27T17:15:20.293215Z",

"resolved_at":null,

"customer":3

}]
