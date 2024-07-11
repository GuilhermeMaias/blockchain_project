from flask import Flask, render_template, request, jsonify
from blockchain.blockchain import Blockchain
import datetime

app = Flask(__name__)
blockchain = Blockchain()

employees = {
    "3101": "gui maia da"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_employee', methods=['POST'])
def register_employee():
    try:
        data = request.get_json()
        employee_id = data.get('employeeId')
        employee_name = data.get('employeeName')

        if employee_id and employee_name:
            employees[employee_id] = employee_name
            return jsonify({"message": "Funcionário registrado com sucesso!"}), 200
        else:
            return jsonify({"error": "Dados de funcionário incompletos"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/record_entry', methods=['POST'])
def record_entry():
    try:
        data = request.get_json()
        employee_id = data.get('employeeId')

        if not employee_id:
            return jsonify({"error": "ID do funcionário não fornecido"}), 400

        if employee_id in employees:
            blockchain.add_block({
                "employee": employees[employee_id],
                "action": "Entrada",
                "timestamp": str(datetime.datetime.now()),
                "photo": "foto1.jpg"  # Lógica para captura de foto aqui
            })
            return jsonify({"message": "Entrada registrada na blockchain!"}), 200
        else:
            return jsonify({"error": "Funcionário não encontrado!"}), 400

    except KeyError:
        return jsonify({"error": "ID do funcionário inválido"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/record_exit', methods=['POST'])
def record_exit():
    try:
        data = request.get_json()
        employee_id = data.get('employeeId')

        if not employee_id:
            return jsonify({"error": "ID do funcionário não fornecido"}), 400

        if employee_id in employees:
            blockchain.add_block({
                "employee": employees[employee_id],
                "action": "Saída",
                "timestamp": str(datetime.datetime.now()),
                "photo": "foto2.jpg"  # Lógica para captura de foto aqui
            })
            return jsonify({"message": "Saída registrada na blockchain!"}), 200
        else:
            return jsonify({"error": "Funcionário não encontrado!"}), 400

    except KeyError:
        return jsonify({"error": "ID do funcionário inválido"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/fetch_records', methods=['GET'])
def fetch_records():
    try:
        records = []
        for block in blockchain.chain:
            records.append({
                "employee": block.data["employee"],
                "action": block.data["action"],
                "timestamp": block.data["timestamp"],
                "photo": block.data["photo"]
            })
        return jsonify(records), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/verify_chain', methods=['GET'])
def verify_chain():
    try:
        is_valid = blockchain.is_chain_valid()
        if is_valid:
            return jsonify({"message": "A cadeia é válida!"}), 200
        else:
            return jsonify({"error": "A cadeia não é válida!"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
