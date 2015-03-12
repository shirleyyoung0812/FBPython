import facebook;
import requests;
import urllib;
import urlparse;
import subprocess;
import warnings;
from django.utils.encoding import smart_str

warnings.filterwarnings('ignore',category=DeprecationWarning);

FACEBOOK_APP_ID="568241156611151";
FACEBOOK_APP_SECRET="6923a517d7fb37e94c4947eaf2dcd7ec";

oauth_args=dict(client_id=FACEBOOK_APP_ID,
		client_secret = FACEBOOK_APP_SECRET,
		grant_type    = 'client_credentials');
	#	fb_exchange_token='CAACEdEose0cBAA0iQg0wE2TytAr0CZBOWTP9aqleELawJqF2ZBzXLG3HtPmIuzgEXHl4dYgU2BREV2ogLYNCN8IiaUpXh3ucfknTeUs3Lxcv5QPUPgyIXiZC313HoWUwOo5Qpbt881Y8FL5n2TvZBIuP2yUzRvp2IZBo3tKX7axjGGYmd8C1N0ukX5VgM7JZCVG44llbawSv5DvHcnmuoSPZCmN9zOR2zYZD');

#oauth_curl_cmd = ['curl',
 #                 "http://graph.facebook.com/endpoint?key=value&access_token=FACEBOOK_APP_ID|FACEBOOK_APP_SECRET"];
#oauth_curl_cmd = ['curl',
 #                 'https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)];

#oauth_response = subprocess.Popen(oauth_curl_cmd,
  #                                stdout = subprocess.PIPE,
  #                                stderr = subprocess.PIPE).communicate()[0];

#try:
 #   oauth_access_token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
#except KeyError as e:
#	print ("Unable to grab an access token! -reason '%s' " % str(e))
#	exit()
oauth_access_token='CAACEdEose0cBADvuGShWWijlhuwbrzuP39wEj0PXp2v6bqk6KTZBnIfZBPqXOQ69a9lnpxxMyjJULnUhP1Goea3WH7JTGeASIznwqlJWsBwJsR5llKnSJt8NE5ZApLnbq9owpISy1zhg0ZA7z9SJYxtwVYykThaVLF1YV0nR49wQzND7xV5QkOhGCNRVVKuj1W3lWCUqAyhr3WEti6xq2XbC58bImzcZD'
er=open('errorcompany.txt','a');

with open('company.txt','r') as companies:
	for line in companies:
		user = line.split("\n")[0]
		if user != '':
			graph = facebook.GraphAPI(oauth_access_token);
			profile = graph.get_object(user);
			print (profile['name']);
			#fi=open(str(line +'.txt'),'w');
			fi=open(str(profile['name']+'.txt'),'w');
			#fi.write('{} has {} likes.\n'.format(line, profile['likes']));
			fi.write('{} has {} likes.\n'.format(profile['name'], profile['likes']));
			datalist = ['posts'];
			for dataneeded in datalist:
			#print dataneeded;
				posts = graph.get_connections(user,dataneeded);
				while True:
					try:
						if "data" in posts:
							lengthp=len(posts["data"]);
							if lengthp==0:
								break;
							elif lengthp>1:
								for i in range(0,lengthp):
									fi.write(str(posts["data"][i]["created_time"]).encode('utf-8') + '\n');
									if "message" in posts["data"][i]:
										fi.write(smart_str(posts["data"][i]["message"]) + '\n');
									if "link" in posts["data"][i]:
										fi.write(smart_str(posts["data"][i]["link"]));
									fi.write( "\n\n");
							else:
								fi.write(str(posts["data"][0]["created_time"]).encode('utf-8') + '\n');
								if "message" in posts["data"][0]:
									fi.write(smart_str(posts["data"][0]["message"]));
								if "link" in posts["data"][0]:
									fi.write(str(posts["data"][0]["link"]).encode('utf-8'));
								fi.write("\n\n");
						if "next" in posts["paging"]: 
							posts=requests.get(posts["paging"]["next"]).json();
					except KeyError as end:
						print ("Error -reason '%s' " % str(end));
						er.write(str(profile['name']) + '\n');
						break; 

		fi.close();
		print ("*********\n");
er.close();


