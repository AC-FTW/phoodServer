import requests, os
from decimal import Decimal
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from metamind.api import set_api_key, food_image_classifier

def form(request):
	return render(request, 'index.html')

def labelMetamind(request):
  if 'q' in request.GET and request.GET['q']:
    url = request.GET['q']
    set_api_key('q7dR3chgj4SLJHnnbpIzvDVXLrvyQ9ncJ6ZX2Gqt9ZyyTPr7oH')
    print food_image_classifier.predict([url], input_type='urls')
  
  else:
    return HttpResponse('Please submit a image url')

  calories = 0
  carbohydrates = 0
  protein = 0
  fiber = 0
  sugar = 0
  calcium = 0
  iron = 0
  magnesium = 0
  phosphorus = 0
  pottasium = 0
  sodium = 0
  zinc = 0
  vitaminc = 0
  thiamin = 0
  riboflavin = 0
  niacin = 0
  vitaminb6 = 0
  folate = 0
  vitamina = 0
  vitamind = 0
  saturatedfat = 0
  monosaturatedfat = 0
  polyunsaturatedfat = 0
  transfat = 0
  totalfat = 0
  fatcalories = 0
  cholestrol = 0
  serving = ""

  context = {
    "serving": serving,
    "calories": calories,
    "carbohydrates": carbohydrates,
    "protein": protein,
    "fiber": fiber,
    "sugar": sugar,
    "calcium": calcium,
    "iron": iron,
    "magnesium": magnesium,
    "phosphorus": phosphorus,
    "pottasium": pottasium,
    "sodium": sodium,
    "zinc": zinc,
    "vitaminc": vitaminc,
    "thiamin": thiamin,
    "riboflavin": riboflavin,
    "niacin": niacin,
    "vitaminb6": vitaminb6,
    "folate": folate,
    "vitamina": vitamina,
    "vitamind": vitamind,
    "saturatedfat": saturatedfat,
    "monosaturatedfat": monosaturatedfat,
    "polyunsaturatedfat": polyunsaturatedfat,
    "transfat": transfat,
    "totalfat": totalfat,
    "fatcalories": fatcalories,
    "cholestrol": cholestrol,
  }
  return render(request, 'label.html', context)

def label(request):
	if 'q' in request.GET and request.GET['q']:
		url = request.GET['q']
		#payload for clarifai api to get token
		payload = {"grant_type":"client_credentials", "client_id":settings.CLARIFAI_CLIENT_ID, "client_secret":settings.CLARIFAI_CLIENT_SECRET}
		token = requests.post('https://api.clarifai.com/v1/token/', data=payload)
		#print(token.json())

		#clarifai vision api headers with image url
		headers = {'Authorization':'Bearer {}'.format(token.json()['access_token'])}
		r = requests.get('https://api.clarifai.com/v1/tag/?url=' + url, headers=headers)

		#guesses and probabilities for items found
		guesses = set(r.json()['results'][0]['result']['tag']['classes'])
		#print(guesses)
		probs = r.json()['results'][0]['result']['tag']['probs']
		#print(probs)

		#clean up guesses with known valid fruits
		fruits = []
		fruitsFile = os.path.join(settings.BASE_DIR, 'fruits.txt')
		fruits = [line.rstrip('\n') for line in open(fruitsFile)]
		fruitsFound = [val for val in fruits if val.lower() in guesses]
		#print (fruitsFound)

		#clean up guesses with known valid vegetables
		vegetables = []
		vegetablesFile = os.path.join(settings.BASE_DIR, 'vegetables.txt')
		vegetables = [line.rstrip('\n') for line in open(vegetablesFile)]
		vegetablesFound = [val for val in vegetables if val.lower() in guesses]
		#print (vegetablesFound)

		#send fruits to USDA API to get back NDBNO information
		fruitIds = []
		vegetableIds = []
		#massaging results to adjust for USDA API finickiness
		outputFile = open('output', 'w')
		for x in fruitsFound:
			x += ", raw"
			usda_headers = {"Content-Type":"application/json"}
			usda_data = {"q":x,"max":"5","offset":"0","group":"Fruits and Fruit Juices",}
			fr = requests.get('http://api.nal.usda.gov/ndb/search/?api_key=' + settings.USDA_API_KEY, usda_data, headers=usda_headers)
			#print(fr.url)
			#print (fr.json())
			fruitIds.append(fr.json()['list']['item'][0]['ndbno'])

		#send vegetables to USDA API to get back NDBNO information
		for x in vegetablesFound:
			x += ", raw"
			usda_headers = {"Content-Type":"application/json"}
			usda_data = {"q":x,"max":"5","offset":"0","group":"Vegetables and Vegetable Products",}
			fr = requests.get('http://api.nal.usda.gov/ndb/search/?api_key=' + settings.USDA_API_KEY, usda_data, headers=usda_headers)
			#print(fr.url)
			#print (fr.json())
			vegetableIds.append(fr.json()['list']['item'][0]['ndbno'])

		#send fruit NDBNO information the USDA API to get nutritional information regarding the item
		for x in fruitIds:
			usda_headers = {"Content-Type":"application/json"}
			usda_data = {"ndbno":x}
			fr = requests.get('http://api.nal.usda.gov/ndb/reports/?api_key=' + settings.USDA_API_KEY, usda_data, headers=usda_headers)
			#print(fr.json())

			#send vegetable NDBNO information the USDA API to get nutritional information regarding the item
		for x in vegetableIds:
			usda_headers = {"Content-Type":"application/json"}
			usda_data = {"ndbno":x}
			fr = requests.get('http://api.nal.usda.gov/ndb/reports/?api_key=' + settings.USDA_API_KEY, usda_data, headers=usda_headers)
			#print(fr.json())
	else:
		return HttpResponse('Please submit a image url')

	calories = 0
	carbohydrates = 0
	protein = 0
	fiber = 0
	sugar = 0
	calcium = 0
	iron = 0
	magnesium = 0
	phosphorus = 0
	pottasium = 0
	sodium = 0
	zinc = 0
	vitaminc = 0
	thiamin = 0
	riboflavin = 0
	niacin = 0
	vitaminb6 = 0
	folate = 0
	vitamina = 0
	vitamind = 0
	saturatedfat = 0
	monosaturatedfat = 0
	polyunsaturatedfat = 0
	transfat = 0
	totalfat = 0
	fatcalories = 0
	cholestrol = 0

	nutrients = fr.json()['report']['food']['nutrients']
	for val in nutrients:
		print val
		if "Energy" in val["name"]:
			calories += Decimal(val["measures"][0]["value"])
		elif "Carbohydrate" in val["name"]:
			carbohydrates += Decimal(val["measures"][0]["value"])
		elif "Protein" in val["name"]:
			protein += Decimal(val["measures"][0]["value"])
		elif "Fiber" in val["name"]:
			fiber += Decimal(val["measures"][0]["value"])
		elif "Sugars" in val["name"]:
			sugar += Decimal(val["measures"][0]["value"])
		elif "Calcium" in val["name"]:
			calcium += Decimal(val["measures"][0]["value"])
		elif "Iron" in val["name"]:
			iron += Decimal(val["measures"][0]["value"])
		elif "Magnesium" in val["name"]:
			magnesium += Decimal(val["measures"][0]["value"])
		elif "Phosphorus" in val["name"]:
			phosphorus += Decimal(val["measures"][0]["value"])
		elif "Pottasium" in val["name"]:
			pottasium += Decimal(val["measures"][0]["value"])
		elif "Sodium" in val["name"]:
			sodium += Decimal(val["measures"][0]["value"])
		elif "Zinc" in val["name"]:
			zinc += Decimal(val["measures"][0]["value"])
		elif "Vitamin C" in val["name"]:
			vitaminc += Decimal(val["measures"][0]["value"])
		elif "Thiamin" in val["name"]:
			thiamin += Decimal(val["measures"][0]["value"])
		elif "Riboflavin" in val["name"]:
			riboflavin += Decimal(val["measures"][0]["value"])
		elif "Niacin" in val["name"]:
			niacin += Decimal(val["measures"][0]["value"])
		elif "Vitamin B-6" in val["name"]:
			vitaminb6 += Decimal(val["measures"][0]["value"])
		elif "Folate" in val["name"]:
			folate += Decimal(val["measures"][0]["value"])
		elif "Vitamin A" in val["name"]:
			vitamina += Decimal(val["measures"][0]["value"])
		elif "Vitamin D" in val["name"]:
			vitamind += Decimal(val["measures"][0]["value"])
		elif "saturated" in val["name"]:
			saturatedfat += Decimal(val["measures"][0]["value"])
		elif "monosaturated" in val["name"]:
			monosaturatedfat += Decimal(val["measures"][0]["value"])
		elif "polyunsaturated" in val["name"]:
			polyunsaturatedfat += Decimal(val["measures"][0]["value"])
		elif "trans" in val["name"]:
			transfat += Decimal(val["measures"][0]["value"])
		elif "Cholestrol" in val["name"]:
			cholestrol += Decimal(val["measures"][0]["value"])

	totalfat = saturatedfat + monosaturatedfat + polyunsaturatedfat + transfat
	serving = nutrients[0]["measures"][0]["label"]

	context = {
		"serving": serving,
		"calories": calories,
		"carbohydrates": carbohydrates,
		"protein": protein,
		"fiber": fiber,
		"sugar": sugar,
		"calcium": calcium,
		"iron": iron,
		"magnesium": magnesium,
		"phosphorus": phosphorus,
		"pottasium": pottasium,
		"sodium": sodium,
		"zinc": zinc,
		"vitaminc": vitaminc,
		"thiamin": thiamin,
		"riboflavin": riboflavin,
		"niacin": niacin,
		"vitaminb6": vitaminb6,
		"folate": folate,
		"vitamina": vitamina,
		"vitamind": vitamind,
		"saturatedfat": saturatedfat,
		"monosaturatedfat": monosaturatedfat,
		"polyunsaturatedfat": polyunsaturatedfat,
		"transfat": transfat,
		"totalfat": totalfat,
		"fatcalories": fatcalories,
		"cholestrol": cholestrol,
	}

	return render(request, 'label.html', context)

def image (request):
	if request.POST:
		# url = request.GET['q']
		#payload for clarifai api to get token
		payload = {"grant_type":"client_credentials", "client_id":settings.CLARIFAI_CLIENT_ID, "client_secret":settings.CLARIFAI_CLIENT_SECRET}
		token = requests.post('https://api.clarifai.com/v1/token/', data=payload)
		#print(token.json())

		# url = 'http://api.clarifai.com/v1/tag/url=?'
		# client = requests.session()
		# client.get(url)
		# csrftoken = client.cookies['csrf']
		#clarifai vision api headers with image url
		headers = {'Authorization':'Bearer {}'.format(token.json()['access_token'])}
		files = {'encoded_image':open('/Users/prabhaav/phood!/mediaRoot/images/image.jpeg')}
		# data = {csrfmiddlewaretoken: csrftoken}
		r = requests.post('https://api.clarifai.com/v1/tag/', headers=headers, files=files)
		print r.json()
		#guesses and probabilities for items found
		guesses = set(r.json()['results'][0]['result']['tag']['classes'])
		#print(guesses)
		probs = r.json()['results'][0]['result']['tag']['probs']
		#print(probs)

		#clean up guesses with known valid fruits
		fruits = []
		fruitsFile = os.path.join(settings.BASE_DIR, 'fruits.txt')
		fruits = [line.rstrip('\n') for line in open(fruitsFile)]
		fruitsFound = [val for val in fruits if val.lower() in guesses]
		#print (fruitsFound)

		#clean up guesses with known valid vegetables
		vegetables = []
		vegetablesFile = os.path.join(settings.BASE_DIR, 'vegetables.txt')
		vegetables = [line.rstrip('\n') for line in open(vegetablesFile)]
		vegetablesFound = [val for val in vegetables if val.lower() in guesses]
		#print (vegetablesFound)

		#send fruits to USDA API to get back NDBNO information
		fruitIds = []
		vegetableIds = []
		#massaging results to adjust for USDA API finickiness
		outputFile = open('output', 'w')
		for x in fruitsFound:
			x += ", raw"
			usda_headers = {"Content-Type":"application/json"}
			usda_data = {"q":x,"max":"5","offset":"0","group":"Fruits and Fruit Juices",}
			fr = requests.get('http://api.nal.usda.gov/ndb/search/?api_key=' + settings.USDA_API_KEY, usda_data, headers=usda_headers)
			#print(fr.url)
			#print (fr.json())
			fruitIds.append(fr.json()['list']['item'][0]['ndbno'])

		#send vegetables to USDA API to get back NDBNO information
		for x in vegetablesFound:
			x += ", raw"
			usda_headers = {"Content-Type":"application/json"}
			usda_data = {"q":x,"max":"5","offset":"0","group":"Vegetables and Vegetable Products",}
			fr = requests.get('http://api.nal.usda.gov/ndb/search/?api_key=' + settings.USDA_API_KEY, usda_data, headers=usda_headers)
			#print(fr.url)
			#print (fr.json())
			vegetableIds.append(fr.json()['list']['item'][0]['ndbno'])

		#send fruit NDBNO information the USDA API to get nutritional information regarding the item
		for x in fruitIds:
			usda_headers = {"Content-Type":"application/json"}
			usda_data = {"ndbno":x}
			fr = requests.get('http://api.nal.usda.gov/ndb/reports/?api_key=' + settings.USDA_API_KEY, usda_data, headers=usda_headers)
			#print(fr.json())

			#send vegetable NDBNO information the USDA API to get nutritional information regarding the item
		for x in vegetableIds:
			usda_headers = {"Content-Type":"application/json"}
			usda_data = {"ndbno":x}
			fr = requests.get('http://api.nal.usda.gov/ndb/reports/?api_key=' + settings.USDA_API_KEY, usda_data, headers=usda_headers)
			#print(fr.json())
	else:
		return HttpResponse('Please submit a image url')

	calories = 0
	carbohydrates = 0
	protein = 0
	fiber = 0
	sugar = 0
	calcium = 0
	iron = 0
	magnesium = 0
	phosphorus = 0
	pottasium = 0
	sodium = 0
	zinc = 0
	vitaminc = 0
	thiamin = 0
	riboflavin = 0
	niacin = 0
	vitaminb6 = 0
	folate = 0
	vitamina = 0
	vitamind = 0
	saturatedfat = 0
	monosaturatedfat = 0
	polyunsaturatedfat = 0
	transfat = 0
	totalfat = 0
	fatcalories = 0
	cholestrol = 0

	nutrients = fr.json()['report']['food']['nutrients']
	for val in nutrients:
		print val
		if "Energy" in val["name"]:
			calories += Decimal(val["measures"][0]["value"])
		elif "Carbohydrate" in val["name"]:
			carbohydrates += Decimal(val["measures"][0]["value"])
		elif "Protein" in val["name"]:
			protein += Decimal(val["measures"][0]["value"])
		elif "Fiber" in val["name"]:
			fiber += Decimal(val["measures"][0]["value"])
		elif "Sugars" in val["name"]:
			sugar += Decimal(val["measures"][0]["value"])
		elif "Calcium" in val["name"]:
			calcium += Decimal(val["measures"][0]["value"])
		elif "Iron" in val["name"]:
			iron += Decimal(val["measures"][0]["value"])
		elif "Magnesium" in val["name"]:
			magnesium += Decimal(val["measures"][0]["value"])
		elif "Phosphorus" in val["name"]:
			phosphorus += Decimal(val["measures"][0]["value"])
		elif "Pottasium" in val["name"]:
			pottasium += Decimal(val["measures"][0]["value"])
		elif "Sodium" in val["name"]:
			sodium += Decimal(val["measures"][0]["value"])
		elif "Zinc" in val["name"]:
			zinc += Decimal(val["measures"][0]["value"])
		elif "Vitamin C" in val["name"]:
			vitaminc += Decimal(val["measures"][0]["value"])
		elif "Thiamin" in val["name"]:
			thiamin += Decimal(val["measures"][0]["value"])
		elif "Riboflavin" in val["name"]:
			riboflavin += Decimal(val["measures"][0]["value"])
		elif "Niacin" in val["name"]:
			niacin += Decimal(val["measures"][0]["value"])
		elif "Vitamin B-6" in val["name"]:
			vitaminb6 += Decimal(val["measures"][0]["value"])
		elif "Folate" in val["name"]:
			folate += Decimal(val["measures"][0]["value"])
		elif "Vitamin A" in val["name"]:
			vitamina += Decimal(val["measures"][0]["value"])
		elif "Vitamin D" in val["name"]:
			vitamind += Decimal(val["measures"][0]["value"])
		elif "saturated" in val["name"]:
			saturatedfat += Decimal(val["measures"][0]["value"])
		elif "monosaturated" in val["name"]:
			monosaturatedfat += Decimal(val["measures"][0]["value"])
		elif "polyunsaturated" in val["name"]:
			polyunsaturatedfat += Decimal(val["measures"][0]["value"])
		elif "trans" in val["name"]:
			transfat += Decimal(val["measures"][0]["value"])
		elif "Cholestrol" in val["name"]:
			cholestrol += Decimal(val["measures"][0]["value"])

	totalfat = saturatedfat + monosaturatedfat + polyunsaturatedfat + transfat
	serving = nutrients[0]["measures"][0]["label"]

	context = {
		"serving": serving,
		"calories": calories,
		"carbohydrates": carbohydrates,
		"protein": protein,
		"fiber": fiber,
		"sugar": sugar,
		"calcium": calcium,
		"iron": iron,
		"magnesium": magnesium,
		"phosphorus": phosphorus,
		"pottasium": pottasium,
		"sodium": sodium,
		"zinc": zinc,
		"vitaminc": vitaminc,
		"thiamin": thiamin,
		"riboflavin": riboflavin,
		"niacin": niacin,
		"vitaminb6": vitaminb6,
		"folate": folate,
		"vitamina": vitamina,
		"vitamind": vitamind,
		"saturatedfat": saturatedfat,
		"monosaturatedfat": monosaturatedfat,
		"polyunsaturatedfat": polyunsaturatedfat,
		"transfat": transfat,
		"totalfat": totalfat,
		"fatcalories": fatcalories,
		"cholestrol": cholestrol,
	}

	return render(request, 'label.html', context)
