from flask import Flask, render_template, request
import uuid
from blockchain import Blockchain
from wallet import Wallet

app = Flask(__name__)

mac = uuid.getnode()
mac_address = ':'.join(('%012X' % mac)[i:i+2] for i in range(0, 12, 2))

blockchain = Blockchain()

wallet1 = Wallet()
wallet2 = Wallet()

print(f"Wallet 1 Public Key: {wallet1.public_key}")
print(f"Wallet 2 Public Key: {wallet2.public_key}")

@app.route('/')
def index():
    return render_template('index.html', user=mac_address)
    
"""@app.route('/send_student', methods=['POST'])
def send_student():
    name = unidecode(str(request.form['student_name']).lower())
    grade = str(request.form['grade']).lower()
    date = str(request.form['date']).lower()
    minutes = str(request.form['minutes']).lower()
    late_index = 1
    print(name)
    print(grade)
    print(date)
    print(minutes)
    for line in open("late_days.txt", "r", encoding='utf-8').readlines():
        if name in str(line):
            late_index += 1
    output = f'Name: {name}\nGrade: {grade}\nDate: {date}\nMinutes: {minutes}'
    output = output.replace("\n", "<br>")
    open("late_days.txt", "a", encoding='utf-8').write(name + ";" + grade + ";" + date + ";" + minutes + ";" + str(late_index) + "\n")
    return render_template('index.html', output=output)"""
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)