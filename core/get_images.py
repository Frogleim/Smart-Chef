import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
import os


def read_csv_file():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    files_path = os.path.join(current_directory, 'ml_models/input')
    file_path = f'{files_path}/df_recipes.csv'
    df = pd.read_csv(file_path)
    return df


def read_images_csv():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    files_path = os.path.join(current_directory, 'ml_models/input')
    file_path = f"{files_path}/update_recipe.csv"
    images_df = pd.read_csv(file_path)
    return images_df


def get_rec_description(rec_url=None):
    df = read_csv_file()
    data_list = []
    # for rec_urls in df['recipe_urls'][859:]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }
    r = requests.get(rec_url, headers=headers)
    soup = BS(r.content, "html.parser")
    main_div = soup.find_all('div', class_='loc article-content')
    for items in main_div:
        try:
            images = soup.find('img')['src']
            step_1 = items.find('p', {'id': "mntl-sc-block_2-0-2"}).text.strip()
            try:
                step_2 = items.find('p', {'id': "mntl-sc-block_2-0-6"}).text.strip()
            except Exception:
                print('No step 2')
                step_2 = None
            data = {
                'url': rec_url,
                'images url': images,
                'step_1': step_1,
                'step_2': step_2,
            }
            data_list.append(data)
        except Exception as e:
            print(e)
    new_df = pd.DataFrame(data_list)
    new_df.to_csv('./update_recipe.csv')
    return data_list



if __name__ == "__main__":
    import os

    get_rec_description(rec_url='https://www.allrecipes.com/recipe/158899/basic-spicy-tomato-sauce/')
    current_directory = os.path.dirname(os.path.abspath(__file__))
    files_path = os.path.join(current_directory, 'ml_models/input')
    file_path = f'{files_path}/df_recipes.csv'
    print(file_path)