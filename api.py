from flask import request, Flask

app = Flask(__name__)

@app.route('/sensors', methods= ['POST'])
def sensors():
    
    data_body = request.get_json()

    abraco = data_body.pop('abraco')

    # Loop through the data_body dictionary
    data_sensors = []
    for key, value in data_body.items():
        data_sensors.append({
            'sensor': key,
            'value': value
        })

    return  f"{len(data_sensors)} sensores foram enviados com sucesso! Abraço = {abraco}"


@app.route('/test')
def test():
    return "To te escutando"



def save_database(data_sensors, abraco):

    sql = "INSERT INTO sensors (sensor, value, abraco) VALUES (%s, %s, %s)"
    print(f'SQL: {sql}')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)