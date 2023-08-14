import requests


class PlaceInfo:
	def __init__(self, data):
		self.data = data

	def __repr__(self):
		place_id = self.data['id']
		place_name = self.data['name']
		return f'PlaceInfo(\'{place_id}\', \'{place_name}\')'

	def get_info(self):
		place_id = self.data['id']
		url = f'https://map.naver.com/v5/api/sites/summary/{place_id}?lang=ko'
		
		response = requests.get(url)
		if response.status_code != requests.codes.ok:
			raise RuntimeError(f'response is not 200 OK (status_code: {requests.status_code})')

		return response.json()


class SearchPlace:
	def __init__(self, query, page = 1, position = None):
		self.query = query
		self.page = page
		self.position = position
		self.result = None

		self.request()
	
	def request(self):
		url = 'https://map.naver.com/v5/api/search'

		payload = {
			'caller': 'pcweb',
			'type': 'all',
			'displayCount': '20',
			'isPlaceRecommendationReplace': True,
			'long': 'ko',
		}
		payload["query"] = self.query
		payload["page"] = self.page
		if self.position is not None:
			payload["searchCoord"] = f'{self.position[0]};{self.position[1]}'

		response = requests.get(url, params=payload)
		if response.status_code != requests.codes.ok:
			raise RuntimeError(f'response is not 200 OK (status_code: {requests.status_code})')

		self.result = response.json()

	def get_places(self):
		try:
			place_list = self.result['result']['place']['list']
			return [PlaceInfo(item) for item in place_list]
		except:
			return []
