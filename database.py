import psycopg2
def con():
	try:
		return psycopg2.connect(user='vet_admin',password='12345',host='localhost',database='vet_app',port=5432)
	except Exception as e:
		print (e)
		return None
