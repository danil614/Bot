import sqlite3
import requests
from bs4 import BeautifulSoup


def remove_spaces(text, start=0):
    return ' '.join(text.split()[start:])


if __name__ == '__main__':
    for i in range(1, 100):
        url = "https://povar.ru/random"
        r = requests.get(url)

        link = r.request.url  # получаем ссылку

        soup = BeautifulSoup(r.text, "html.parser")
        # dish_name = soup.find('h1', class_='detailed').text  # ищем название блюда

        # general_description = remove_spaces(soup.find('span', class_='detailed_full', itemprop='description').text)
        # получаем общее описание

        # description = remove_spaces(soup.find('h2', class_='span').parent.text, 2)
        # получаем описание приготовления

        ingredients_code = soup.find_all('li', itemprop='recipeIngredient')  # ингредиенты
        # full_ingredients = ''  # полное описание ингредиентов с количеством
        # ingredients = []  # только ингредиенты

        connection = sqlite3.connect("database.sqlite")

        try:
            with connection:
                cursor = connection.cursor()
                for ingredient in ingredients_code:
                    # full_ingredients += remove_spaces(ingredient.text) + '\n'
                    name = remove_spaces(ingredient.attrs['rel']).lower()
                    cursor.execute("""SELECT name FROM ingredients WHERE name=:name""", {"name": name})
                    result = cursor.fetchall()

                    if len(result) == 0:
                        cursor.execute("""insert into ingredients(name) values(:name)""", {"name": name})
        finally:
            connection.close()

    # tags_code = soup.find_all('span', class_='detailed_tags')[0].find_all('a')  # теги
    # tags = []
    #
    # for tag in tags_code:
    #     tags.append(remove_spaces(tag.text))

    # number_of_servings = soup.find_all('em', itemprop='recipeYield')[0].text  # количество порций

    # image = soup.find('div', class_='bigImgBox').find('img').attrs['src']  # картинка
