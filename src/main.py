from pprint import pprint
from NaverPlaceInfo import *


def main():
	# 1. 네이버 지도 검색
	search = SearchPlace('맘스터치', position=(14119794.435436185,4518158.037596846)) # (위도, 경도) 생략 가능

	# 2. 검색 결과 받아오기
	places = search.get_places()
	print('places:')
	pprint(places)

	# 3. 첫번째 검색 결과의 정보 받아오기
	place_info = places[0].get_info()

	# 4. 운영시간 출력 (데이터에 따라 Key가 없을 수도 있음)
	try:
		print('\nbizHour:')
		pprint(place_info["bizHour"])
	except KeyError:
		print('NO DATA')

	try:
		print('\nbizhourInfo:')
		pprint(place_info["bizhourInfo"])
	except KeyError:
		print('NO DATA')


if __name__ == '__main__':
	main()
