if __name__ == '__main__':
    for i in range(10):
        print('****', f'{i=}')
        for j in range(10):
            print(f'{j=}')
            if i == j:
                break
