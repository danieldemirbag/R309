import time, multiprocessing, concurrent.futures, requests


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__ == '__main__':
    img_urls = [
        'https://cdn.pixabay.com/photo/2015/10/25/10/25/bridge-1005571_960_720.jpg',
        'https://cdn.pixabay.com/photo/2016/11/19/15/20/dog-1839808_960_720.jpg',
        'https://cdn.pixabay.com/photo/2022/11/05/22/00/the-path-7572857_960_720.jpg',
    ]

    p1 = multiprocessing.Process(target=download_image(img_urls[0]))
    p1.start()
    p2 = multiprocessing.Process(target=download_image(img_urls[1]))
    p2.start()
    p3 = multiprocessing.Process(target=download_image(img_urls[2]))
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")
