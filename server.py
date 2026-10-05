from http.server import HTTPServer, BaseHTTPRequestHandler 
import json 
from main import saveBrowserPassword
 
class PasswordRequestHandler(BaseHTTPRequestHandler): 
 
    def do_OPTIONS(self): 
        self.send_response(200) 
        self.send_header("Access-Control-Allow-Origin", "*") 
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS") 
        self.send_header("Access-Control-Allow-Headers", "Content-Type") 
        self.end_headers() 
 
    def do_POST(self): 
 
        if self.path != "/save-password": 
            self.send_response(404) 
            self.end_headers() 
            return 
 
        content_length = int(self.headers["Content-Length"]) 
 
        data = self.rfile.read(content_length) 
 
        password_data = json.loads(data) 
 
        website = password_data.get("website") 
        username = password_data.get("username") 
        password = password_data.get("password") 

        saveBrowserPassword(website,username,password)
 
        print("\nNew password received from browser!") 
        print("Website:", website) 
        print("Username:", username) 
        print("Password received successfully.") 
 
        self.send_response(200) 
        self.send_header("Content-Type", "application/json") 
        self.send_header("Access-Control-Allow-Origin", "*") 
        self.end_headers() 
 
        response = { 
            "success": True, 
            "message": "Password received successfully" 
        } 

         
        self.wfile.write(json.dumps(response).encode()) 
 
 
server = HTTPServer(("127.0.0.1", 5000), PasswordRequestHandler) 
 
print("Password manager server is running...") 
print("Waiting for browser passwords...") 
 
server.serve_forever() 

 