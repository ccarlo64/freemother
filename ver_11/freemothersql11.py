#
# freemother 1.0 03/2018
#
from websocket_server import WebsocketServer
import logging
import json
import datetime
import time
import subprocess

#DB
import os
import sqlite3


print "    #####"
print "   # o o #"
print "   # \_/ #"
print "    #   #"
print "   #     #"
print "  #       #"
print " #         #"
print " #         #"
print " #         #"
print "  #       #"
print "   #######"
print "   "
print "freemother 1.1"

db_filename = 'freemotherdb.db'
schema_filename = 'freemotherdb.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print 'Creation of the scheme...'
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
    else:
        print 'The database exists, it is assumed that the schema exists.'
#


PORT=80
HOST='192.168.0.1'
#PORT=9001
#HOST='192.168.1.159'
mac='MO0004A3F9B33B'
cookieName=['one','two','three','four']
cookieNode=['6FEC200D','AA81082C','206B121A','65EB0E1C']

fase=0
sleep_state=0
cl_mother=''
cl0=''

msg_1='{"body": {"token": "hn3mnbvzkdd1pqlbzp70la81okvzlpbn"}, "resource": "login", "method": "get"}'
msg_2='{"body": {"status": 200}, "resource": "login", "method": "post"}'
msg_3='Asking for registration state'
msg_3a='{"body": 1, "type": "gateway", "resource": "registration", "method": "post", "auth": "'+mac+'"}'
msg_4='{"body": {"stateFrequency": 180, "smileLed": "255,0,0", "serverUrl": "in.sen.se", "rightLed": "60,100,240", "rfPower": 100, "leftLed": "60,100,240", "serverPort": 80, "maxConn": 24, "soundLevel": 75}, "type": "gateway", "resource": "state", "method": "post", "auth": "'+mac+'"}'
msg_5='{"body": {"version": 103, "collection": []}, "type": "gateway", "resource": "library/resident", "method": "post", "auth": "'+mac+'"}'
msg_6='{"body": {"version": 102, "collection": []}, "type": "gateway", "resource": "library/sound", "method": "post", "auth": "'+mac+'"}'
msgup='\n' #0x0a 

msgsleep='{"body": 1, "type": "gateway", "resource": "mute", "method": "post", "auth": "'+mac+'"}'
msgwakeup='{"body": 0, "type": "gateway", "resource": "mute", "method": "post", "auth": "'+mac+'"}'


#msg_rst_resident='{"body": {"version": 103, "collection": [{"url": "app-00.sen.se/mother/media/animations/00103/idle.json", "flash": 1, "id": "idle"}, {"url": "app-00.sen.se/mother/media/animations/00103/newstate.json", "flash": 1, "id": "newstate"}, {"url": "app-00.sen.se/mother/media/animations/00103/nonetwork.json", "flash": 1, "id": "nonetwork"}, {"url": "app-00.sen.se/mother/media/animations/00103/noplateform.json", "flash": 1, "id": "noplateform"}, {"url": "app-00.sen.se/mother/media/animations/00103/noregistration.json", "flash": 1, "id": "noregistration"}, {"url": "app-00.sen.se/mother/media/animations/00103/registration.json", "flash": 1, "id": "registration"}, {"url": "app-00.sen.se/mother/media/animations/00103/start.json", "flash": 1, "id": "start"}, {"url": "app-00.sen.se/mother/media/animations/00103/upgrading.json", "flash": 1, "id": "upgrading"}, {"url": "app-00.sen.se/mother/media/animations/00103/demo.json", "flash": 1, "id": "demo"}, {"url": "app-00.sen.se/mother/media/animations/00103/wakeup.json", "flash": 1, "id": "wakeup"}, {"url": "app-00.sen.se/mother/media/animations/00103/sleep.json", "flash": 1, "id": "sleep"}]}, "type": "gateway", "resource": "library/resident", "method": "post", "auth": "MO0004A3F9B33B"}'
#msg_rst_sound='{"body": {"version": 102, "collection": [{"url": "app-00.sen.se/mother/media/sounds/00102/start.wav", "flash": 1, "id": "start"}, {"url": "app-00.sen.se/mother/media/sounds/00102/registration.wav", "flash": 1, "id": "registration"}, {"url": "app-00.sen.se/mother/media/sounds/00102/wakeup.wav", "flash": 1, "id": "wakeup"}, {"url": "app-00.sen.se/mother/media/sounds/00102/asleep.wav", "flash": 1, "id": "asleep"}, {"url": "app-00.sen.se/mother/media/sounds/00102/generic.wav", "flash": 1, "id": "generic"}, {"url": "app-00.sen.se/mother/media/sounds/00102/duck.wav", "flash": 1, "id": "duck"}, {"url": "app-00.sen.se/mother/media/sounds/00102/hawaii.wav", "flash": 1, "id": "hawaii"}, {"url": "app-00.sen.se/mother/media/sounds/00102/piano.wav", "flash": 1, "id": "piano"}, {"url": "app-00.sen.se/mother/media/sounds/00102/saxo.wav", "flash": 1, "id": "saxo"}, {"url": "app-00.sen.se/mother/media/sounds/00102/xylo.wav", "flash": 1, "id": "xylo"}, {"url": "app-00.sen.se/mother/media/sounds/00102/metalo.wav", "flash": 1, "id": "metalo"}, {"url": "app-00.sen.se/mother/media/sounds/00102/ahh.wav", "flash": 1, "id": "ah"}, {"url": "app-00.sen.se/mother/media/sounds/00102/um.wav", "flash": 1, "id": "hum"}, {"url": "app-00.sen.se/mother/media/sounds/00102/mm.wav", "flash": 1, "id": "mmm"}, {"url": "app-00.sen.se/mother/media/sounds/00102/medication.wav", "flash": 1, "id": "medication"}, {"url": "app-00.sen.se/mother/media/sounds/00102/teeth.wav", "flash": 1, "id": "teeth"}, {"url": "app-00.sen.se/mother/media/sounds/00102/sleep.wav", "flash": 1, "id": "sleep"}, {"url": "app-00.sen.se/mother/media/sounds/00102/presenceout.wav", "flash": 1, "id": "presenceout"}, {"url": "app-00.sen.se/mother/media/sounds/00102/door.wav", "flash": 1, "id": "door"}, {"url": "app-00.sen.se/mother/media/sounds/00102/down.wav", "flash": 1, "id": "down"}, {"url": "app-00.sen.se/mother/media/sounds/00102/up.wav", "flash": 1, "id": "up"}, {"url": "app-00.sen.se/mother/media/sounds/00102/water.wav", "flash": 1, "id": "water"}, {"url": "app-00.sen.se/mother/media/sounds/00102/presencein.wav", "flash": 1, "id": "presencein"}, {"url": "app-00.sen.se/mother/media/sounds/00102/coffee.wav", "flash": 1, "id": "coffee"}, {"url": "app-00.sen.se/mother/media/sounds/00102/temperature.wav", "flash": 1, "id": "temperature"}, {"url": "app-00.sen.se/mother/media/sounds/00102/fridge.wav", "flash": 1, "id": "fridge"}, {"url": "app-00.sen.se/mother/media/sounds/00102/check.wav", "flash": 1, "id": "check"}, {"url": "app-00.sen.se/mother/media/sounds/00102/plant.wav", "flash": 1, "id": "plant"}, {"url": "app-00.sen.se/mother/media/sounds/00102/walk.wav", "flash": 1, "id": "walk"}]}, "type": "gateway", "resource": "library/sound", "method": "post", "auth": "MO0004A3F9B33B"}'

msg_rst_resident='{"body": {"version": 103, "collection": [{"url": "192.168.0.1:8000/00103/idle.json", "flash": 1, "id": "idle"}, {"url": "192.168.0.1:8000/00103/newstate.json", "flash": 1, "id": "newstate"}, {"url": "192.168.0.1:8000/00103/nonetwork.json", "flash": 1, "id": "nonetwork"}, {"url": "192.168.0.1:8000/00103/noplateform.json", "flash": 1, "id": "noplateform"}, {"url": "192.168.0.1:8000/00103/noregistration.json", "flash": 1, "id": "noregistration"}, {"url": "192.168.0.1:8000/00103/registration.json", "flash": 1, "id": "registration"}, {"url": "192.168.0.1:8000/00103/start.json", "flash": 1, "id": "start"}, {"url": "192.168.0.1:8000/00103/upgrading.json", "flash": 1, "id": "upgrading"}, {"url": "192.168.0.1:8000/00103/demo.json", "flash": 1, "id": "demo"}, {"url": "192.168.0.1:8000/00103/wakeup.json", "flash": 1, "id": "wakeup"}, {"url": "192.168.0.1:8000/00103/sleep.json", "flash": 1, "id": "sleep"}]}, "type": "gateway", "resource": "library/resident", "method": "post", "auth": "MO0004A3F9B33B"}'
msg_rst_sound='{"body": {"version": 102, "collection": [{"url": "192.168.0.1:8000/00102/start.wav", "flash": 1, "id": "start"}, {"url": "192.168.0.1:8000/00102/registration.wav", "flash": 1, "id": "registration"}, {"url": "192.168.0.1:8000/00102/wakeup.wav", "flash": 1, "id": "wakeup"}, {"url": "192.168.0.1:8000/00102/asleep.wav", "flash": 1, "id": "asleep"}, {"url": "192.168.0.1:8000/00102/generic.wav", "flash": 1, "id": "generic"}, {"url": "192.168.0.1:8000/00102/duck.wav", "flash": 1, "id": "duck"}, {"url": "192.168.0.1:8000/00102/hawaii.wav", "flash": 1, "id": "hawaii"}, {"url": "192.168.0.1:8000/00102/piano.wav", "flash": 1, "id": "piano"}, {"url": "192.168.0.1:8000/00102/saxo.wav", "flash": 1, "id": "saxo"}, {"url": "192.168.0.1:8000/00102/xylo.wav", "flash": 1, "id": "xylo"}, {"url": "192.168.0.1:8000/00102/metalo.wav", "flash": 1, "id": "metalo"}, {"url": "192.168.0.1:8000/00102/ahh.wav", "flash": 1, "id": "ah"}, {"url": "192.168.0.1:8000/00102/um.wav", "flash": 1, "id": "hum"}, {"url": "192.168.0.1:8000/00102/mm.wav", "flash": 1, "id": "mmm"}, {"url": "192.168.0.1:8000/00102/medication.wav", "flash": 1, "id": "medication"}, {"url": "192.168.0.1:8000/00102/teeth.wav", "flash": 1, "id": "teeth"}, {"url": "192.168.0.1:8000/00102/sleep.wav", "flash": 1, "id": "sleep"}, {"url": "192.168.0.1:8000/00102/presenceout.wav", "flash": 1, "id": "presenceout"}, {"url": "192.168.0.1:8000/00102/door.wav", "flash": 1, "id": "door"}, {"url": "192.168.0.1:8000/00102/down.wav", "flash": 1, "id": "down"}, {"url": "192.168.0.1:8000/00102/up.wav", "flash": 1, "id": "up"}, {"url": "192.168.0.1:8000/00102/water.wav", "flash": 1, "id": "water"}, {"url": "192.168.0.1:8000/00102/presencein.wav", "flash": 1, "id": "presencein"}, {"url": "192.168.0.1:8000/00102/coffee.wav", "flash": 1, "id": "coffee"}, {"url": "192.168.0.1:8000/00102/temperature.wav", "flash": 1, "id": "temperature"}, {"url": "192.168.0.1:8000/00102/fridge.wav", "flash": 1, "id": "fridge"}, {"url": "192.168.0.1:8000/00102/check.wav", "flash": 1, "id": "check"}, {"url": "192.168.0.1:8000/00102/plant.wav", "flash": 1, "id": "plant"}, {"url": "192.168.0.1:8000/00102/walk.wav", "flash": 1, "id": "walk"}]}, "type": "gateway", "resource": "library/sound", "method": "post", "auth": "MO0004A3F9B33B"}'


'''# {"body": 1, "type": "gateway", "resource": "mute", "method": "post", "auth": "MO0004A3F9B33B"}
    {"resource": "status", "method": "get", "auth": "MO0004A3F9B33B"}
{"body": {"stateFrequency": 180, "smileLed": "255,0,0", "serverUrl": "in.sen.se", "rightLed": "60,100,240", "rfPower": 100, "leftLed": "60,100,240", "serverPort": 80, "maxConn": 24, "soundLevel": 75}, "type": "gateway", "resource": "state", "method": "post", "auth": "MO0004A3F9B33B"}



{"body": {"smileLed": "0,255,0", "rightLed": "60,100,240",  "leftLed": "60,100,240"}, "type": "gateway", "resource": "state", "method": "post", "auth": "MO0004A3F9B33B"}

{"body": {"rfPower": 100}, "type": "gateway", "resource": "state", "method": "post", "auth": "MO0004A3F9B33B"}
{"body": {"Nb Cookie": 1}, "type": "gateway", "resource": "events", "method": "post", "auth": "MO0004A3F9B33B"}

'''

def getCookies(client, server):
    global db_filename
    with sqlite3.connect(db_filename) as conn:
      cursor = conn.cursor()
      query = """ select node, name from cookies"""
      cursor.execute(query) #, {'n':node})
      i=0
      elenco=''
      message=''
      for row in cursor.fetchall():
        nodo, nome = row
        if i==0:
          elenco=nodo
          elenco='{"resource" : "command", "method":"post", "type": "name", "body" : [{"node":"'+nodo+'"}'
        else:
          #elenco=elenco + ","+nodo
          elenco=elenco+', {"node":"'+nodo+'"}'
        i=i+1
        message=elenco+']}'
#        message="RESPONSE"+elenco
      print "response",message     
      server.send_message_to_all(message)
      
def convData( d ):
    s='' #20180330111741
    #d[0:4] [4:6] [6:8] [8:10] [10:12] [12:14]
    s=d[6:8]+"/"+d[4:6]+"/"+d[0:4]+" "+d[8:10]+":"+d[10:12]+":"+d[12:14]
    return s
      #server.send_message(client, message)
def getHistory(client, server,n,f):
    global db_filename
    with sqlite3.connect(db_filename) as conn:
      cursor = conn.cursor()
      query = """ select date_events, signal, val from cookies_events where node= :n and feed_type=:f order by date_events desc limit 10"""
      print query
      cursor.execute(query,{'n': n,'f':f})
      i=0
      elenco=''
      message=''
      
      for row in cursor.fetchall():
        de, signal, val = row
        if i==0:
          elenco='{"resource" : "command", "method":"post", "type": "history", "body" : [{"node":"'+n+'","date":"'+convData(de)+'","signal":"'+signal+'","value":"'+val+'","feed_type":"'+f+'"}'
        else:
          elenco=elenco+', {"node":"'+n+'","date":"'+convData(de)+'","signal":"'+signal+'","value":"'+val+'","feed_type":"'+f+'"}'
        i=i+1
        message=elenco+']}'
#        message="RESPONSE"+elenco
      print "response",message     
      if message!='':
        server.send_message_to_all(message)

      
def getInfo(client, server,n):
    global db_filename
    with sqlite3.connect(db_filename) as conn:
      cursor = conn.cursor()
      query = """ select max(date_events), signal, val from cookies_events where node= :n and feed_type='5' """
      print query
      cursor.execute(query,{'n': n})
      i=0
      elenco=''
      message=''
      try:
        row = cursor.fetchone()
        de, signal, val = row
        if i==0:
          elenco='{"resource" : "command", "method":"post", "type": "info", "body" : [{"node":"'+n+'","date":"'+convData(de)+'","signal":"'+signal+'","value":"'+val+'","feed_type":"5"}'
        message=elenco+']}'
      except TypeError as e:
        print "no feed_type 5" #(e)
      if message!='':
        server.send_message_to_all(message)
        
      print "response 5",message     
      print "-"      
      print "-"      
      print "-"      
      query = """ select max(date_events), signal, val from cookies_events where node= :n and feed_type='4' """
      print query,n
      cursor.execute(query,{'n': n})
      i=0
      elenco=''
      message=''
      try:
        row = cursor.fetchone()
        de, signal, val = row
        if i==0:
          elenco='{"resource" : "command", "method":"post", "type": "info", "body" : [{"node":"'+n+'","date":"'+convData(de)+'","signal":"'+signal+'","value":"'+val+'","feed_type":"4"}'
        message=elenco+']}'
      except TypeError as e:
        print "no feed_type 4" #(e)
      if message!='':
        server.send_message_to_all(message)

      query = """ select max(date_events), signal, val from cookies_events where node= :n and feed_type='3' """
      print query
      cursor.execute(query,{'n': n})
      i=0
      elenco=''
      message=''
      try:
        row = cursor.fetchone()
        de, signal, val = row
        if i==0:
          elenco='{"resource" : "command", "method":"post", "type": "info", "body" : [{"node":"'+n+'","date":"'+convData(de)+'","signal":"'+signal+'","value":"'+val+'","feed_type":"3"}'
        message=elenco+']}'
      except TypeError as e:
        print "no feed_type 3" #(e)
      if message!='':
        server.send_message_to_all(message)
        
      query = """ select max(date_events), signal, val from cookies_events where node= :n and feed_type='2' """
      print query
      cursor.execute(query,{'n': n})
      i=0
      elenco=''
      message=''
      try:
        row = cursor.fetchone()
        de, signal, val = row
        if i==0:
          elenco='{"resource" : "command", "method":"post", "type": "info", "body" : [{"node":"'+n+'","date":"'+convData(de)+'","signal":"'+signal+'","value":"'+val+'","feed_type":"2"}'
        message=elenco+']}'
      except TypeError as e:
        print "no feed_type 2" #(e)
      if message!='':
        server.send_message_to_all(message)
                
'''
    global db_filename
    with sqlite3.connect(db_filename) as conn:
      cursor = conn.cursor()
      query = """ select max(date_events), signal, val from cookies_events where node= :n and feed_type='5' """
      print query
      cursor.execute(query,{'n': n})
      i=0
      elenco=''
      message=''
      for row in cursor.fetchall():
        de, signal, val = row
        if i==0:
          elenco='{"resource" : "command", "method":"post", "type": "info", "body" : [{"node":"'+n+'","date":"'+de+'","signal":"'+signal+'","value":"'+val+'","feed_type":"5"}'
#          elenco='{"resource" : "command", "method":"post", "type": "info", "body" : [{"node":"'+n+'"},{"signal":"'+signal+'"},{"value":"'+val+'"}'
        else:
          #elenco=elenco + ","+nodo
          elenco=elenco+', {"node":"'+n+'","date":"'+de+'","signal":"'+signal+'","value":"'+val+'","feed_type":"5"}'
#          elenco=elenco+', {"node":"'+n+'"},{"signal":"'+signal+'"},{"value":"'+val+'"}'
        i=i+1
        message=elenco+']}'
#        message="RESPONSE"+elenco
      print "response 5",message     
      server.send_message_to_all(message)
      query = """ select max(date_events), signal, val from cookies_events where node= :n and feed_type='4' """
      print query
      cursor.execute(query,{'n': n})
      i=0
      elenco=''
      message=''
      for row in cursor.fetchall():
        de, signal, val = row
        if i==0:
          elenco='{"resource" : "command", "method":"post", "type": "info", "body" : [{"node":"'+n+'","date":"'+de+'","signal":"'+signal+'","value":"'+val+'","feed_type":"4"}'
#          elenco='{"resource" : "command", "method":"post", "type": "info", "body" : [{"node":"'+n+'"},{"signal":"'+signal+'"},{"value":"'+val+'"}'
        else:
          #elenco=elenco + ","+nodo
          elenco=elenco+', {"node":"'+n+'","date":"'+de+'","signal":"'+signal+'","value":"'+val+'","feed_type":"4"}'
#          elenco=elenco+', {"node":"'+n+'"},{"signal":"'+signal+'"},{"value":"'+val+'"}'
        i=i+1
        message=elenco+']}'
#        message="RESPONSE"+elenco
      print "response 4",message     
      server.send_message_to_all(message)
'''
def debugLog( txt ): 
    n = "( " + time.strftime("%c") + " ) "
    logFile = 'srvlog.log'
    subprocess.call( 'echo "'+n+txt+'" >> '+logFile, shell=True )  
    return

# Called for every client connecting (after handshake)
def new_client(client, server):
    global cl_mother
    global cl0
    h=client['address'][0]
    print("New client connected and was given id %d %s" % (client['id'], h))
    
    if client['id']==1:
      cl_mother=client
    if client['id']==2:
      cl0=client
    ##server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
    global cl0
    print("Client(%d) disconnected" % client['id'])
    if client['id']==2:
      cl0=''


# Called when a client sends a message
def message_received(client, server, message):
    global sleep_state
    global cl_mother
    global cl0
    global db_filename
    global newc
    
    j = json.loads(message)
    
    debugLog(chr(48+client['id'])+" "+message)
    #debugLog(message)
    if len(message) > 200:
      message = message[:200]+'..'
    print("Client(%d) said: %s" % (client['id'], message))
    if client['id']!=1:
      print("send to Client(%d) " % (cl_mother['id']))
      print "test ",message
      server.send_message(cl_mother, message)
      
    if client['id']!=1:
      cmd=''
      try:
        cmd=j['resource']
      except KeyError:
         print "no command"
      if cmd=='command':
         method=j['method']
         n=j['body']['node']
         t=j['type']
         if t=='name' and method=='get' and n=='all':
           getCookies( client, server )
           print "******",method,n
         if t=='info' and method=='get' and n!='all':
           getInfo( client, server, n )
           print "leggo valori"
         if t=='history' and method=='get' and n!='all':
           f=j['body']['feed_type']
           getHistory( client, server, n, f)
           print "leggo la storia di ", f
         

      
      '''      
      try:
        cmd=j['command']
      except KeyError:
         print "no command"
      if cmd=='get':
         o=j['object']
         if o=='node':
           getCookies( client, server )

           elenco=''
           with sqlite3.connect(db_filename) as conn:
             cursor = conn.cursor()
             query = """ select node, name from cookies"""
             cursor.execute(query) #, {'n':node})
             i=0
             for row in cursor.fetchall():
               nodo, nome = row
               if i==0:
                 elenco=nodo
               else:
                 elenco=elenco + ","+nodo
               i=i+1
             message="RESPONSE"+elenco
             print "response"     
             server.send_message(client, message)
            '''
      
      
      
       
     




      
    #controlli
    if client['id']==1:
     #j = json.loads(message)
     
     
     
     
     
     if j['resource']=='auth':
      print("Client(%d) " % (client['id']))
      print "auth request"
      fase=1
      server.send_message(client, msg_1)
      print "SRV:",msg_1

     if j['resource']=='login':
      print("Client(%d) " % (client['id']))
      print "auth request 2"
      fase=2
      server.send_message(client, msg_2)
      print "SRV:",msg_2
      
     if j['resource']=='registration':
      print("Client(%d) " % (client['id']))
      print "auth request 3"
      fase=3
      server.send_message(client, msg_3)
      print "SRV:",msg_3
      server.send_message(client, msg_3a)
      print "SRV:",msg_3a
      
     if j['resource']=='planning':
      print("Client(%d) " % (client['id']))
      print "auth request 4"
      fase=4
      server.send_message(client, msg_4)
      print "SRV:",msg_4
      
     if j['resource']=='library/sound' and j['method']=='get' and j['body']['version']!='0':
      print("Client(%d) " % (client['id']))
      print "auth request 6"
      fase=5
      server.send_message(client, msg_6)
      print "SRV:",msg_6          

     if j['resource']=='library/resident' and j['method']=='get' and j['body']['version']!='0':
      print("Client(%d) " % (client['id']))
      print "auth request 5"
      fase=6
      server.send_message(client, msg_5)
      print "SRV:",msg_5        

     #reset !!
     if j['resource']=='library/resident' and j['method']=='get' and j['body']['version']=='0':
      print("Client(%d) " % (client['id']))
      print "send url for reset resident"
      fase=99
      server.send_message(client, msg_rst_resident)
      print "SRV: reset"       
      
     if j['resource']=='library/sound' and j['method']=='get' and j['body']['version']=='0':
      print("Client(%d) " % (client['id']))
      print "send url for reset"
      fase=99
      server.send_message(client, msg_rst_sound)
      print "SRV: reset sound"          
      

     if j['resource']=='events':
      print("Client(%d) " % (client['id']))
      print "events "
      node=''
      try:
        node=j['body'][0]['node']
      except KeyError:
        print "no node"
      ## cerca il nodo tra i biscotti
      co=''
      idx=0
      for x in cookieNode:
        if x==node:
          co=cookieName[idx]
          break
        idx+=1
      if node!='':
      #if co!='':
        #print "cookie ", node, 
        print "COOKIE: ",node
        ft=j['body'][0]['feed_type']
        si=j['body'][0]['signal']
        va=j['body'][0]['value']
        #a=datetime.datetime.now()
        #t=a.strftime('%d-%m-%Y %H:%M:%S.%f')
        t = "( " + time.strftime("%c") + " ) "
        tt= time.strftime('%Y%m%d%H%M%S')
        #find test existent
        
        with sqlite3.connect(db_filename) as conn:

          cursor = conn.cursor()
          
          if ft=='99': #new cookie
          
           query = """ select node, name from cookies where node = :n """
           cursor.execute(query, {'n':node})
           nodo=''
           newc=0
           for row in cursor.fetchall():
             nodo, nome = row
             print '%s %s' % (nodo, nome)
           if nodo=='':
             print "insert new cookie"
            
             conn.execute(""" insert into cookies (node, name) values ('""" + node + """', 'biscotto!')""")
             conn.commit();
             newc=1
             getCookies( client, server )
            
            
          #node, name = cursor.fetchone()
          #print "node ",node," name", name
          # insert events...
          if ft!='99' and ft !='1': #new events
           cursor.execute("insert into cookies_events (node, date_events, feed_type, signal, val ) values (?,?,?,?,?)",(node,tt,ft,si,va))
          #print time.strftime('%Y%m%d%H%M%S')
    
        
        
        #tmp="_"+t+"_feed_=" + ft + "_signal_=" +si+ "_value_="+va
        tmp=t+";"+ft+";"+si+";"+va;
        print tmp
        #send to browser
        if cl0!='':
          server.send_message(cl0, "COOKIE"+chr(49+idx)+tmp)
#          server.send_message(cl0, "COOKIE"+node+tmp)
        else:
          print "not dbg redirection"
                
      if j['body'][0]['feed_type']=='6':
        print "feed 6 "
        if j['body'][0]['value']>='5000' and sleep_state<2:
           print "sleep fase 1"
           sleep_state+=1
           if sleep_state==2:
              print "sleep fase 2"
              server.send_message(client, msgsleep)
        else:
           if sleep_state>1:
              print "wake up "
              sleep_state=0
              server.send_message(client, msgwakeup)
      if j['body'][0]['feed_type']=='1' and j['body'][0]['value']=='1':
        print "ping!? "
        server.send_message(client, msgup)
          
      
#PORT=80
#HOST='192.168.0.1:8000'
server = WebsocketServer(PORT,HOST,logging.INFO)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
