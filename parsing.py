import requests
from bs4 import BeautifulSoup


def remove_spaces(text, start=0):
    return ' '.join(text.split()[start:])


if __name__ == '__main__':
    # url = "https://povar.ru/random"
    url = 'https://povar.ru/recipes/salat_s_blinami_i_gribami-79753.html'
    r = requests.get(url)

    link = r.request.url  # получаем ссылку

    soup = BeautifulSoup(r.text, "html.parser")
    dish_name = soup.find('h1', class_='detailed').text  # ищем название блюда

    general_description = remove_spaces(soup.find('span', class_='detailed_full', itemprop='description').text)
    # получаем общее описание

    description = remove_spaces(soup.find('h2', class_='span').parent.text, 2)
    # получаем описание приготовления

    ingredients_code = soup.find_all('li', itemprop='recipeIngredient')  # ингредиенты
    full_ingredients = ''  # полное описание ингредиентов с количеством
    ingredients = []  # только ингредиенты

    for ingredient in ingredients_code:
        full_ingredients += remove_spaces(ingredient.text) + '\n'
        ingredients.append(remove_spaces(ingredient.attrs['rel']))

    tags_code = soup.find_all('span', class_='detailed_tags')[0].find_all('a')  # теги
    tags = []

    for tag in tags_code:
        tags.append(remove_spaces(tag.text))

    number_of_servings = soup.find_all('em', itemprop='recipeYield')[0].text  # количество порций

    image = soup.find('div', class_='bigImgBox').find('img').attrs['src']  # картинка

    test = True
