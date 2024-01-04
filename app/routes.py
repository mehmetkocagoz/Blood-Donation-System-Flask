from flask import request, jsonify
from app import app
from app.user_validation import checkUser
from app.blooddatabase import addBloodToDatabase,createDonorInDatabase,requestBloodFromDatabase
from app.donordatabase import requestDonorListFromDatabase

# Works on localhost!
# Works on azure deployment!
# Works with API GATEWAY
@app.route("/login", methods = ['POST'])
def login():
    # If request method is POST, it comes froms the form, check database and validate user
    if request.method == 'POST':
        try:
            # Assuming the client sends a JSON object in the request body
            user_data = request.json

            # Now you can access the JSON data in user_data dictionary
            username = user_data.get('username')
            password = user_data.get('password')

            # Perform authentication logic here (check credentials, etc.)
            validation = checkUser(username,password)
            if validation:
                response_data = {"status": "TRUE", "message": "Login successful","user_name" : username }
                return jsonify(response_data)
            else:
                response_data = {"status": "FALSE", "message": "Login not successful"}
                return jsonify(response_data)

        except Exception as e:
            # Handle exceptions (e.g., JSON parsing error)
            error_message = str(e)
            response_data = {"status": "error", "message": error_message}
            return jsonify(response_data), 400


# Works on localhost!
# Works on azure deployment!
# Works with API GATEWAY
@app.route("/request",methods = ['POST'])
def requestblood():
    if request.method == 'POST':
        try:
            form_data = request.json

            requestor = form_data.get('requestor')
            bloodType = form_data.get('bloodType')
            city = form_data.get('city')
            town = form_data.get('town')
            email = form_data.get('email')
            units = int(form_data.get('units'))
            duration = int(form_data.get('duration'))
            reason = form_data.get('reason')
            donor_list = requestBloodFromDatabase(requestor,bloodType,city,town,email,units,duration)

            response_data ={"status":"TRUE","donor_list":donor_list}
            return jsonify(response_data)
        
        except Exception as e:
            # Handle exceptions (e.g., JSON parsing error)
            error_message = str(e)
            response_data = {"status": "error", "message": error_message}
            return jsonify(response_data), 400
    

# Works on localhost!
# Works on azure deployment!
# Works with API GATEWAY
@app.route("/add", methods = ['POST','GET'])
def addBlood():
    if request.method == 'POST':
        try:
            form_data = request.json

            blood_type = form_data.get('bloodType')
            unit = int(form_data.get('unit'))
            donor_name = form_data.get('donorName')

            messageFromDatabase = addBloodToDatabase(donor_name,blood_type,unit)

            response_data ={"status":"TRUE","Message":messageFromDatabase}
            return jsonify(response_data)
        except Exception as e:
            # Handle exceptions (e.g., JSON parsing error)
            error_message = str(e)
            response_data = {"status": "error", "message": error_message}
            return jsonify(response_data), 400
    else:
        # GET REQUEST
        # We will return donor_name list
        form_data = request.json
        print(form_data)
        branch_name = form_data.get('branch_name')
        print(branch_name)
        donor_list = requestDonorListFromDatabase(branch_name)
        response_data = {"status":"TRUE","donor_list":donor_list}
        return jsonify(response_data)


# Works on localhost!
# Works on azure deployment!
# Works with API GATEWAY
@app.route("/create",methods = ['POST'])
def createDonor():
    if request.method == 'POST':
        try:
            form_data = request.json

            donor_name = form_data.get('donorName')
            blood_type = form_data.get('bloodType')
            city = form_data.get('city')
            town = form_data.get('town')
            email = form_data.get('email')
            phone = form_data.get('phone')

            message = createDonorInDatabase(donor_name,blood_type,city,town,email,phone)
            response_data = {"status":"TRUE","message":message}
            return jsonify(response_data)

        except Exception as e:
            # Handle exceptions (e.g., JSON parsing error)
            error_message = str(e)
            response_data = {"status": "error", "message": error_message}
            return jsonify(response_data), 400
        