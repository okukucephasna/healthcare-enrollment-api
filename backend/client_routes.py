from flask import Blueprint, request, jsonify
from db import get_connection

client_bp = Blueprint('client_bp', __name__)

@client_bp.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')

    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO clients (name, age, gender) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, age, gender))
        connection.commit()

    return jsonify({'message': 'Client created successfully'}), 201


@client_bp.route('/clients', methods=['GET'])
def get_clients():
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM clients")
            clients = cursor.fetchall()
    return jsonify(clients)


@client_bp.route('/clients/<int:client_id>', methods=['GET'])
def get_client_profile(client_id):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM clients WHERE id = %s", (client_id,))
            client = cursor.fetchone()

            if not client:
                return jsonify({'message': 'Client not found'}), 404

            cursor.execute(
                "SELECT p.id, p.name FROM enrollments e JOIN programs p ON e.program_id = p.id WHERE e.client_id = %s",
                (client_id,)
            )
            programs = cursor.fetchall()
            client['programs'] = programs

    return jsonify(client)
