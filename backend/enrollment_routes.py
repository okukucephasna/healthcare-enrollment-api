from flask import Blueprint, request, jsonify
from db import get_connection

enrollment_bp = Blueprint('enrollment_bp', __name__)

@enrollment_bp.route('/enrollments', methods=['POST'])
def enroll_client():
    data = request.json
    client_id = data.get('client_id')
    program_id = data.get('program_id')

    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM clients WHERE id = %s", (client_id,))
            if not cursor.fetchone():
                return jsonify({'message': 'Client not found'}), 404

            cursor.execute("SELECT id FROM programs WHERE id = %s", (program_id,))
            if not cursor.fetchone():
                return jsonify({'message': 'Program not found'}), 404

            cursor.execute("SELECT id FROM enrollments WHERE client_id = %s AND program_id = %s", (client_id, program_id))
            if cursor.fetchone():
                return jsonify({'message': 'Client already enrolled in this program'}), 400

            sql = "INSERT INTO enrollments (client_id, program_id) VALUES (%s, %s)"
            cursor.execute(sql, (client_id, program_id))
        connection.commit()

    return jsonify({'message': 'Client enrolled successfully'}), 201


@enrollment_bp.route('/enrollments', methods=['GET'])
def get_enrollments():
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM enrollments")
            enrollments = cursor.fetchall()
    return jsonify(enrollments)
