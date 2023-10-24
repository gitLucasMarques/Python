import requests

BASE_URL = 'https://fakestoreapi.com'

#GET
#response = requests.get(f'{BASE_URL}/products')

query_params = {"limit": 3}
#response = requests.get(f'{BASE_URL}/products', params=query_params)

#response = requests.get(f'{BASE_URL}/products/18')

#POST
new_product = {
  "title": 'test product',
  "price": 13.5,
  "description": 'lorem ipsum set',
  "image": 'https://i.pravatar.cc',
  "category": 'eletronic'
}
#response = requests.post(f'{BASE_URL}/products', json=new_product)


#PUT
#updated_product = {"title": 'updated_product', "category": 'clothing'}
#response = requests.put(f'{BASE_URL}/products/21', json=updated_product)


#PATCH
updated_product = {"category": 'eletronic'}
response = requests.patch(f'{BASE_URL}/products/21', json=updated_product)

#DElETE
response = requests.delete(f'{BASE_URL}/products/21')


print(response.json())
#print(response.status_code)
