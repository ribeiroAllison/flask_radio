from app import app, db


class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), index = True, unique = True) 
  playlist_id = db.Column(db.Integer,  db.ForeignKey('playlist.id'))
  
  #representation method
  def __repr__(self):
        return "{}".format(self.username)

class Song(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  artist = db.Column(db.String(50), index = True, unique = False)
  title = db.Column(db.String(50), index = True, unique = False)
  n = db.Column(db.Integer, index = False, unique = False)

  #representation method
  def __repr__(self):
        return "{} by {}".format(self.title, self.artist)

    
#create the Item model here + add a nice representation method
    
#create the Playlist model here + add a nice representation method
