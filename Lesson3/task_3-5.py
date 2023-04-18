shopping_list: list = ['хлеб', 'апельсиновый сок', 'киви', 'молоко', 'куриный фарш', 'лимон']

def task_3() -> None:
    count: int = len(shopping_list)
    print(f'У тебя {count} продуктов\n')

def task_4() -> None:
    print(*shopping_list, sep=', ', end='\n')

def task_5() -> None:
    new_shopping_list:list = [product for product in shopping_list if len(product) % 2 == 0]
    print(*new_shopping_list, sep=', ', end='\n')

if __name__ == '__main__':
    task_3()
    task_4()
    task_5()