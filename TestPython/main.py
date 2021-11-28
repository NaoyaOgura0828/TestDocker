def main():
    try:
        raise ValueError("error!")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
  main()