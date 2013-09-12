from artifacts.models import Artifact
from data_info import *

try:
  for i in items:
    try:
      temp_art = Artifact.objects.get(title=i.title, price=i.price, description=i.description)
    except Artifact.DoesNotExist:
      print "Adding " + i.title + " to database"
      i.save()
except:
  ##that's an error
  print ":("
  ##if only it could be somebody else's problem...
  raise
