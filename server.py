import http.server
import socketserver
import json
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from urllib.parse import parse_qs, urlparse

PORT = 8080
TARGET_EMAIL = 'grilledog296@gmail.com'
SUBMISSIONS_FILE = 'rsvp_submissions.json'

class WeddingHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        parsed_url = urlparse(self.path)
        if parsed_url.path in ['/api/rsvp', '/api/wish']:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            data = {}
            content_type = self.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                try:
                    data = json.loads(post_data)
                except Exception:
                    data = {}
            else:
                parsed_form = parse_qs(post_data)
                data = {k: v[0] if len(v) == 1 else v for k, v in parsed_form.items()}

            name = data.get('name', '').strip()
            message = data.get('message', '').strip()
            attending = data.get('form_item6') or data.get('attending', '').strip()
            if not attending and 'attendance' in data:
                attending = data['attendance']
            if not attending:
                attending = 'Chưa xác nhận'

            submission = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'name': name,
                'message': message,
                'attending': attending,
                'ip': self.client_address[0]
            }

            # 1. Save locally to JSON file
            all_submissions = []
            if os.path.exists(SUBMISSIONS_FILE):
                try:
                    with open(SUBMISSIONS_FILE, 'r', encoding='utf-8') as f:
                        all_submissions = json.load(f)
                except Exception:
                    all_submissions = []
            
            all_submissions.append(submission)
            with open(SUBMISSIONS_FILE, 'w', encoding='utf-8') as f:
                json.dump(all_submissions, f, ensure_ascii=False, indent=2)

            print(f'[RSVP SUCCESS] {name} | Tham du: {attending} | Loi nhan: {message}')

            # 2. Attempt email dispatch to TARGET_EMAIL
            email_status = self.send_rsvp_email(submission)

            # Response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            resp = {
                'success': True,
                'message': f'Cam on {name} da gui loi chuc va xac nhan!',
                'email_sent': email_status
            }
            self.wfile.write(json.dumps(resp, ensure_ascii=False).encode('utf-8'))
        else:
            self.send_error(404, 'Endpoint not found')

    def send_rsvp_email(self, submission):
        smtp_user = os.environ.get('SMTP_USER')
        smtp_pass = os.environ.get('SMTP_PASSWORD')
        
        name = submission['name']
        attending = submission['attending']
        msg_text = submission['message']
        timestamp = submission['timestamp']

        subject = f'[Thiep Cuoi Khang & Linh] Khach moi xac nhan: {name}'
        body = f'''Xin chao Khang & Linh,

Ban vua nhan duoc mot loi chuc & xac nhan tham du moi tu website thiep cuoi:

- Ho va ten khach: {name}
- Trang thai tham du: {attending}
- Loi chuc phuc: {msg_text}
- Thoi gian gui: {timestamp}

---------------------------------------------------
Thong tin duoc luu tru tu dong trong rsvp_submissions.json tren may chu.
'''
        if not smtp_user or not smtp_pass:
            print(f'[EMAIL LOG] Gui toi: {TARGET_EMAIL}')
            print(f'[EMAIL LOG] Tieu de: {subject}')
            print(f'[EMAIL LOG] (De gui email truc tiep qua Gmail SMTP, dat bien moi truong SMTP_USER va SMTP_PASSWORD)')
            return False

        try:
            msg = MIMEMultipart()
            msg['From'] = smtp_user
            msg['To'] = TARGET_EMAIL
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(smtp_user, smtp_pass)
                server.send_message(msg)
            print(f'[EMAIL DISPATCHED] Email successfully sent to {TARGET_EMAIL}!')
            return True
        except Exception as e:
            print(f'[EMAIL ERROR] Failed to send email via SMTP: {e}')
            return False

if __name__ == '__main__':
    handler = WeddingHandler
    with socketserver.TCPServer(('', PORT), handler) as httpd:
        print(f'Wedding Server with RSVP Backend running at http://localhost:{PORT}/')
        httpd.serve_forever()
