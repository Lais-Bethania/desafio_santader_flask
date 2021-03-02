from flask_restful import Resource

class WebService(Resource):

    # prints Santander
    def get(self):
        try:
            # String to print
            data = "Santander"

            return data
        except (Exception) as error:
            print(error)
            return error