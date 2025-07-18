from flask import Blueprint, request, jsonify
from db import get_connection

program_bp = Blueprint('program_bp', __name__)

@program_bp.route('/programs', methods=['POST'])
def create_program():
    data = request.json
    name = data.get('name')

    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM programs WHERE name = %s", (name,))
            if cursor.fetchone():
                return jsonify({'message': 'Program already exists'}), 400

            sql = "INSERT INTO programs (name) VALUES (%s)"
            cursor.execute(sql, (name,))
        connection.commit()

    return jsonify({'message': 'Program created successfully'}), 201


@program_bp.route('/programs', methods=['GET'])
def get_programs():
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM programs")
            programs = cursor.fetchall()
    return jsonify(programs)
