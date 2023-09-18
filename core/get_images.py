import pandas as pd
import requests
from bs4 import BeautifulSoup as BS


def read_csv_file():
    file_path = './ml_models/input/df_recipes.csv'
    df = pd.read_csv(file_path)
    return df


def get_rec_description(rec_url=None):
    df = read_csv_file()
    print(df)
    data_list = []

    for rec_urls in df['recipe_urls'][859:]:
        print(rec_urls)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }

        r = requests.get(rec_urls, headers=headers)
        soup = BS(r.content, "html.parser")
        main_div = soup.find_all('div', class_='loc article-content')

        # Initialize an empty list to store the data
        for items in main_div:
            try:
                images = soup.find('img')['src']
                print(images)
                step_1 = items.find('p', {'id': "mntl-sc-block_2-0-2"})
                print(step_1.text.strip())
                step_2 = items.find('p', {'id': "mntl-sc-block_2-0-6"})
                print(step_2.text.strip())

                # Create a dictionary with the data
                data = {
                    'url': images,
                    'step_1': step_1.text.strip(),
                    'step_2': step_2.text.strip(),
                }

                # Append the dictionary to the data_list
                data_list.append(data)

            except Exception as e:
                print(e)

    # Read the CSV file once outside the loop
    new_df = pd.DataFrame(data_list)
    new_df.to_csv('./update_recipe.csv')






if __name__ == "__main__":

    get_rec_description()
