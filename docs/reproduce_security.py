import os,django,json
os.environ['DJANGO_SETTINGS_MODULE']='mcpexample.settings';django.setup()
from django.db import connection
from bird_counter.models import Bird
from mcp_server.query_tool import apply_json_mango_query
with connection.schema_editor() as e:
 from bird_counter.models import City,Location
 for m in (City,Location,Bird):e.create_model(m)
Bird.objects.create(species='secret',count=987)
import sys
if sys.argv[1]=='66':
 for fields in (set(),{'species'}):
  print('allowed_fields',fields,'output',list(apply_json_mango_query(Bird.objects.all(),[],allowed_fields=fields)))
else:
 for pipeline in ([{'$match':{'species':'secret'}}],[{'$group':{'_id':None,'leaked':{'$max':'$species'}}}],[{'$search':{'text':{'query':'secret'}}}]):
  try:print(pipeline, list(apply_json_mango_query(Bird.objects.all(),pipeline,excluded_fields={'species'})))
  except Exception as e:print(type(e).__name__,str(e))
