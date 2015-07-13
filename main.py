__author__ = 'Nispand'

from bottle import route, run, template
from bottle import route, request, response, template, HTTPResponse
import json
import csv
from bottle import Bottle
from cluster_code import clusterplot
from cluster_code import getcoordi
from cluster_code import for_bargraph
bottle = Bottle()

field_names = {"time","latitude","longitude","depth","mag","magType","nst","gap","dmin","rms","net","id","updated","place","type"}

@bottle.route('/webui')
def webui():
    return template('Display_data')

@bottle.route('/plotcluster', method='POST')
def plotcluster():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posted_dict =  request.forms.dict
        print(posted_dict)
        nof = posted_dict["nof"][0]
        print nof
        tot = clusterplot(nof)
    return "done"


@bottle.route('/scatterplot',method='POST')
def scatterplot():
     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posted_dict =  request.forms.dict
        x_param = posted_dict["x_param"][0]
        y_param = posted_dict["y_param"][0]
        d_vector = getcoordi(x_param,y_param)
        data = json.dumps(d_vector)
        resp = HTTPResponse(body=data,status=200)
        return resp
     else:
        return 'This is a normal request'

@bottle.route('/bargraph', method='POST')
def bargraph():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posted_dict = request.forms.dict
        print(posted_dict)
        x_param = posted_dict["x_param"][0]
        y_param = posted_dict["y_param"][0]
        print x_param
        print y_param
        d_vector = get_decimal_vector3(x_param,y_param)
        data = json.dumps(d_vector)
        resp = HTTPResponse(body=data,status=200)
        return resp
    else:
        return 'This is a normal request'

@route('/postcomment',  method='POST')
def postcomment():
    #pdb.set_trace()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posted_dict =  request.forms.dict
        user_name = posted_dict["username"][0]
        post_id = posted_dict["postid"][0]
        comment = posted_dict["comment"][0]
        output = comment_post(user_name,post_id,comment)
        data = str(output)
        resp = HTTPResponse(body=data,status=200)
        return resp

def get_decimal_vector3(x_param,y_param):
    d_vector = []
    csvfile = open("all_month.csv","rb")
    reader = csv.reader(csvfile)
    reader.next()
    reader.next()

    if x_param == 'latitude' :
        x_param = int(1)
    elif x_param == 'longitude' :
        x_param = int(2)
    elif x_param == 'mag':
        x_param = int(3)

    if y_param == 'latitude' :
        y_param = int(1)
    elif y_param == 'longitude' :
        y_param = int(2)
    elif y_param == 'mag':
        y_param = int(3)

    datacnt = 0
    for row in reader:
        datacnt = datacnt + 1
        vector_element = {}
        print row[x_param]
        print row[y_param]
        print(row)
        x_cor = abs(int(float(row[x_param])))
        y_cor = abs(int(float(row[y_param])))
        vector_element['key'] = x_cor
        vector_element['value']= y_cor
        d_vector.append(vector_element)
        if datacnt == 100:
            break
    return d_vector

def clean(element):
    element = element.replace(",","")
    element = element.strip("+/-")
    element = element.strip()
    element = element.replace("N","")
    element = element.replace("X","")
    element = element.replace("nc","0")
    element = element.replace('','0')
    return element


bottle.run(host='0.0.0.0', port=8080, debug=True)