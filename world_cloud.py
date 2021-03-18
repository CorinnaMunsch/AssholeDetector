import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def word_cloud(param):

    with open("resources/" + param + '.txt', 'r', encoding="utf-8") as file:
        text = file.read().replace('\n', ' ')
    print(text)

    mask = np.array(Image.open('resources/' + param + '.png'))
    wc = WordCloud(stopwords=STOPWORDS,
                   mask=mask, background_color='#AEE0FD',
                   # #CB6CE6, #AEE0FD, #F14F33
                   max_words=2000, max_font_size=256,
                   random_state=42, width=mask.shape[1],
                   height=mask.shape[0], contour_width=10,
                   contour_color='firebrick')
    wc.generate(text)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    # plt.savefig('results/' + param + ' wordcloud.png')


if __name__ == '__main__':
    # word_cloud('Asshole_20')
    # word_cloud('Everyone Sucks_20')
    word_cloud('Not the A-hole_20')
