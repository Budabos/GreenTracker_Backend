from flask_restful import Resource, fields, marshal, reqparse 
from models import TrackGoals
from config import db
from datetime import datetime
from flask import request

track_goals_fields={
    "user_id": fields.Integer,
    "id": fields.Integer,
    "title": fields.String,
    "description": fields.String,
    "category": fields.String,
    "start_date": fields.DateTime,
    "end_date": fields.DateTime,
    "target_metric": fields.String,
    "target_value": fields.String,
    "current_value": fields.String,
    "status": fields.String,
    "note": fields.String,
    "reminder": fields.String,
    "created_at": fields.DateTime
}

class TrackGoalsResource(Resource):
    profile_parser = reqparse.RequestParser()
    profile_parser.add_argument("title", type=str, required=True, help="Title is required")
    profile_parser.add_argument("user_id", type=int, required=True, help="Title is required")
    profile_parser.add_argument("description", type=str, required=True, help="Description is required")
    profile_parser.add_argument("category", type=str, required=True, help="Category is required")
    profile_parser.add_argument("start_date", type=str, required=True, help="Start date is required")
    profile_parser.add_argument("end_date",type=str, required=True, help="End date is required")
    profile_parser.add_argument("target_metric", type=str, required=True, help="Target metric is required")
    profile_parser.add_argument("target_value", type=str, required=True, help="Target value is required")
    profile_parser.add_argument("current_value", type=str, required=True, help="Current value is required")
    profile_parser.add_argument("status", type=str, required=True, help="Status is required")
    profile_parser.add_argument("note", type=str, required=True, help="Note is required")
    profile_parser.add_argument("reminder", type=str, required=True, help="Reminder is required")

    def get(self, id=None):
        if id:
            track_goals = TrackGoals.query.filter_by(id=id).first()
            if track_goals:
                return marshal(track_goals, track_goals_fields), 200
            else:
                return {'message': 'No track goals found'}, 404
        else:
            track_goals = TrackGoals.query.all()
            if track_goals:
                return marshal(track_goals, track_goals_fields), 200
            else:
                return {'message': 'No track goals found'}, 404
            
    def post(self):
        data= self.profile_parser.parse_args()
        
        # trackgoals the model
        goal = TrackGoals(**data)

        try:
            db.session.add(goal)
            db.session.commit()
            return {"message":"Goal created successfully"}
        except:
            return {"message":"Goal not created"}
        

    def patch(self, id):
        goal = TrackGoals.query.get(id)

        if goal:
            for attr in request.json:
                setattr(goal, attr, request.json[attr])
            
            try:
                db.session.add(goal)
                db.session.commit()
                db.session.refresh(goal)

                return {"message":"Goal updated successfully", "goal":goal.to_dict()}, 200
            except:
                return {"message":"Goal not updated"},500
            
        else:
            return {"message":"Goal not found"}, 404
        

    def delete(self, id):

        goal = TrackGoals.query.get(id)
        if goal:
            try:
                db.session.delete(goal)
                db.session.commit()
                return {"message":"Goal deleted successfully"}
            except:
                return {"message":"Goal not deleted"}
        else:
            return {"message":"Goal not found"}, 404