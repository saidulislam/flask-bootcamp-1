from flask import Flask, request
from flask_restful import Resource, Api
from secure_check import authenticate,identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somesecretkey'
api = Api(app)

jwt = JWT(app, authenticate, identity)


# Later, this will be a model call to our database
# Right now its just a list of dictionaries
# employees = [{'name':'John Smith'},{name:'Jason Burt'},......]
# Keep in mind, its in memory, it clears with every restart.

employees = []

class EmployeeNames(Resource):
    def get(self, name):
        print(employees)

        # cycle through list employees
        for emp in employees:
            if emp['name'] == name:
                return emp

        # If you request a employee not yet in the employees list
        return {'name': None}, 404

    def post(self, name):
        # Add  the dictionary to list
        emp = {'name': name}
        employees.append(emp)
        # Then return it back
        print(employees)
        return emp

    def delete(self, name):

        # cycle through the list of employees
        for i, emp in enumerate(employees):
            if emp['name'] == name:
                employees.pop(i)
                return {'note': 'delete successful'}


class AllEmployees(Resource):

    @jwt_required()
    def get(self):
        # return all the employees
        return {'employees': employees}


api.add_resource(EmployeeNames, '/employee/<string:name>')
api.add_resource(AllEmployees, '/employees')

if __name__ == '__main__':
    app.run(debug=True)