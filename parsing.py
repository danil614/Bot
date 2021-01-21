import requests
from bs4 import BeautifulSoup

def remove_spaces(text):
    return ' '.join(text.split())


if __name__ == '__main__':
    # url = "https://povar.ru/random"
    url = 'https://povar.ru/recipes/salat_s_blinami_i_gribami-79753.html'
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    dishes_names = soup.find_all('h1', class_='detailed')  # ищем название блюда
    dish_name = dishes_names[0].text

    new_url = r.request.url  # получаем ссылку

    general_description = soup.find_all('span', class_='detailed_full', itemprop='description')
    # получаем общее описание
    general_description = ' '.join(general_description[0].text.split())

    description = ' '.join(soup.find_all('h2', class_='span')[0].parent.text.split()[2:])
    # получаем описание приготовления

    ingredients_code = soup.find_all('li', itemprop='recipeIngredient')  # ингредиенты
    full_ingredients = []  # полное описание ингредиентов с количеством
    ingredients = []  # только ингредиенты

    for ingredient in ingredients_code:
        full_ingredients.append(remove_spaces(ingredient.text))
        ingredients.append(remove_spaces(ingredient.attrs['rel']))

    print('')
