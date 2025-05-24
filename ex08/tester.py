from time import sleep
from tqdm import tqdm

from Loading import ft_tqdm


def main():

    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    for elem in tqdm(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
