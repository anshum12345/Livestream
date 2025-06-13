from datetime import datetime
from bson import ObjectId

class Overlay:
    @staticmethod
    def create_overlay(db, data):
        data['created_at'] = datetime.utcnow()
        data['updated_at'] = datetime.utcnow()
        return db.overlays.insert_one(data)
    
    @staticmethod
    def get_overlay(db, overlay_id):
        return db.overlays.find_one({'_id': ObjectId(overlay_id)})
    
    @staticmethod
    def get_all_overlays(db):
        return list(db.overlays.find({}))
    
    @staticmethod
    def update_overlay(db, overlay_id, data):
        data['updated_at'] = datetime.utcnow()
        return db.overlays.update_one(
            {'_id': ObjectId(overlay_id)},
            {'$set': data}
        )
    
    @staticmethod
    def delete_overlay(db, overlay_id):
        return db.overlays.delete_one({'_id': ObjectId(overlay_id)})