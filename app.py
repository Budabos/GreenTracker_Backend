from flask import Flask
from flask_restful import Api
from resources.impact import ImpactMonitorings
from resources.carbon import CarbonFootprintCalculation
from config import app, api, bcrypt
from resources.edu_resources import EduResource
from resources.user import UserAccounts

# Add resources to the API
api.add_resource(EduResource, '/education-resources')
api.add_resource(UserAccounts, '/users')
api.add_resource(ImpactMonitorings, '/impact_monitorings')
api.add_resource(CarbonFootprintCalculation, '/calculate_footprint')


if __name__ == '__main__':
    app.run(port=5555, debug=True)