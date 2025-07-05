from flask import Flask, request, jsonify
from flask_cors import CORS
from db import init_db

app = Flask(__name__)
CORS(app)

mysql = init_db(app)

@app.route('/')
def home():
    return "Backend is working"

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    message = data.get('message')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO feedback (message) VALUES (%s)", (message,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"status": "Feedback submitted"}), 200

@app.route('/reservation', methods=['POST'])
def reservation():
    data = request.json
    name = data['name']
    email = data['email']
    date = data['date']
    time = data['time']
    guests = data['guests']

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO reservations (name, email, date, time, guests) VALUES (%s, %s, %s, %s, %s)",
        (name, email, date, time, guests)
    )
    mysql.connection.commit()
    cur.close()
    return jsonify({"status": "Reservation confirmed"}), 200

@app.route('/order', methods=['POST'])
def order():
    data = request.json
    full_name = data.get('name')
    phone = data.get('phone')
    order_details = data.get('order')
    address = data.get('address')

    # Debugging: Check if the data is received correctly
    print(f"Received Order: {full_name}, {phone}, {order_details}, {address}")

    # Ensure the cursor and connection are properly handled
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO orders (fullName, phone, orderDetails, address) VALUES (%s, %s, %s, %s)",
        (full_name, phone, order_details, address)
    )
    mysql.connection.commit()
    cur.close()

    # Return a response indicating success
    return jsonify({"status": "Order placed successfully!"}), 200


if __name__ == '__main__':
    app.run(debug=True)
