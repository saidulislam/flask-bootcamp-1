from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# Later on this will be a model call to our database!
# Right now its just a list of dictionaries
# employees = [{'name':'John Smith'},{name:'Dan Smith'},......]
# Keep in mind, its in memory, it clears with every restart!
employees = []

class EmployeeNames(Resource):
    
    def get(self, name):
        
        # Cycle through list of employees
        for emp in employees:
            if emp['name'] == name:
                return emp

        # If you request an employee not yet in the employees list
        return {'name': None}, 404

    def post(self, name):
        # Add  the dictionary to list
        emp = {'name': name}
        employees.append(emp)

        # Then return it back
        return emp

    def delete(self, name):
        # Cycle through list
        for i, emp in enumerate(employees):
            if emp['name'] == name:
                # delete the entry
                employees.pop(i)
                return {'note': 'delete successful'}
        return {'note': f'{name} not found in the list'}


class AllEmployees(Resource):

    def get(self):
        # return all. you have to return a json object
        return {'empoyees': employees}


api.add_resource(EmployeeNames, '/employee/<string:name>')
api.add_resource(AllEmployees, '/employees')

if __name__ == '__main__':
    app.run(debug=True)