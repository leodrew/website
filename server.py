from flask import Flask, render_template ,url_for , request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def My_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_database(data):
	email = data["email"]
	subject = data["subject"]
	message = data["message"]
	with open('database.txt', 'a') as data:
		file = data.write('\n{},{},{}'.format(email,subject,message))


def write_to_csv(data):
	email = data["email"]
	subject = data["subject"]
	message = data["message"]
	with open('database.csv','a',newline='') as data:
		csv_file = csv.writer(data,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_file.writerow([email,subject,message])



@app.route('/sumbit_form', methods=['POST', 'GET'])
def sumbit_form():
   if request.method == 'POST':
   	data = request.form.to_dict()
   	write_to_csv(data)
   	return redirect('/thankyou.html')
   else:
   	return 'something went wrong'